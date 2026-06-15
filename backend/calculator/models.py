from datetime import date

from django.db import models
from django.db.models import Sum, Avg
from django.db.models.functions import TruncMonth
from django.utils import timezone


# ====================================================================
# MODEL 1: SINGLETON FOR CURRENT TARIFF
# ====================================================================

class CurrentTariffModel(models.Model):
    power_tariff = models.FloatField(verbose_name='Актуальна вартість за Кв', default=4.32)
    last_updated = models.DateTimeField(auto_now=True, verbose_name='Дата оновлення')

    class Meta:
        verbose_name = 'Актуальний Тариф'
        verbose_name_plural = 'Актуальний Тариф'

    def __str__(self):
        return f"Актуальний тариф: {self.power_tariff} UAH/Кв"

    def save(self, *args, **kwargs):
        self.pk = 1
        super().save(*args, **kwargs)

    @classmethod
    def load(cls):
        try:
            return cls.objects.get(pk=1)
        except cls.DoesNotExist:
            return cls.objects.create(pk=1)


# ====================================================================
# MODEL 2: ENTRIES
# ====================================================================

class DataEntryLineModel(models.Model):
    # ============================================================
    # --------------------- CONSTANTS ---------------------------
    # ============================================================
    POWER = [
        ('200', '200'), ('400', '400'), ('600', '600'), ('800', '800'),
    ]

    ONE_POWER_UNIT = 20.48
    CHARGE_DIFFERENCE_THRESHOLD = 10
    MORNING_CORRECTION_CHARGE = 6
    MORNING_CORRECTION_PRICE = 0.6

    DEFAULT_COST_LOW = 0.86
    DEFAULT_COST_HIGH = 0.43
    FALLBACK_COST = 0.0

    POWER_LOW = 200
    POWER_HIGH = 100

    # --- ПОЛЯ ---
    date = models.DateField(verbose_name='Дата')
    power = models.CharField(choices=POWER, max_length=3, default='600', verbose_name='Потужність системи')
    weather = models.ManyToManyField('WeatherConditionModel', db_index=True, related_name='weather',
                                     verbose_name='Погода')

    morning_data_charge = models.IntegerField(verbose_name='Ранковий рівень заряду')
    morning_data_price = models.FloatField(verbose_name='Вартість використаної енергії на ранок')

    afternoon_data_charge = models.IntegerField(default=0, verbose_name='Денний рівень заряду')
    afternoon_data_price = models.FloatField(default=0, verbose_name='Вартість використаної енергії на день')

    evening_data_charge = models.IntegerField(verbose_name='Вечірній рівень заряду')
    evening_data_price = models.FloatField(verbose_name='Вартість використаної енергії на вечір')

    default_day_energy_formula = models.BooleanField(default=False)
    extra_power = models.IntegerField(default=0, verbose_name='Приблизна потужність використана на USB', null=True,
                                      blank=True)

    full_day_power = models.FloatField(blank=True, verbose_name='Вироблена потужність за день')
    full_day_cost = models.FloatField(blank=True, null=True, verbose_name='Вартість виробленої енергії за день')

    power_tariff = models.FloatField(verbose_name='Вартість за Кв')

    def _calculate_power_delta_based_on_price(self, start_cost, end_cost):
        price_diff = end_cost - start_cost

        if self.power_tariff == 0:
            return 0

        return round(((price_diff * 100) / self.power_tariff) * 100, 2)

    def _handle_charge_difference(self, charge_diff):
        if charge_diff <= self.CHARGE_DIFFERENCE_THRESHOLD:
            return self.POWER_HIGH
        else:
            return self.POWER_LOW

    def _day_charge_equal(self):
        return self.morning_data_charge == self.afternoon_data_charge == self.evening_data_charge == 0

    def _morning_price_equal_evening_price(self):
        return self.morning_data_price == self.evening_data_price

    def _afternoon_price_equal_evening_price(self):
        return self.afternoon_data_price == self.evening_data_price

    def _afternoon_charge_bigger_zero(self):
        return 0 < self.afternoon_data_charge

    def _afternoon_charge_equal_zero(self):
        return self.afternoon_data_charge == 0

    def _evening_afternoon_power_result(self, evening_data_charge, afternoon_data_charge):
        return (evening_data_charge - afternoon_data_charge) * self.ONE_POWER_UNIT

    def _power_to_price(self, bigger_charge, lower_charge):
        return (((bigger_charge - lower_charge) * self.ONE_POWER_UNIT) / 1000) * self.power_tariff

    def _price_to_power(self, bigger_price, lower_price):
        return round(
            (((bigger_price - lower_price) * 100) / 43.2) * 100, 2)

    def _evening_to_afternoon_price(self, evening_price, afternoon_price):
        power_dif = evening_price - afternoon_price
        curren_tariff_unit = (CurrentTariffModel.power_tariff * 100) / 100

        return round(((power_dif * 100) / curren_tariff_unit) * 100, 2)

    def _calculate_full_day_power(self):
        try:
            usb_power = self.extra_power if self.extra_power is not None else 0

            if self.morning_data_charge == self.afternoon_data_charge == self.evening_data_charge == 0:
                return 0

            base_power = 0

            if self.afternoon_data_price == self.evening_data_price or self.morning_data_price == self.evening_data_price:
                base_power = (self.evening_data_charge - self.afternoon_data_charge) * self.ONE_POWER_UNIT
                return base_power + usb_power

            if 0 < self.afternoon_data_charge < self.evening_data_charge:
                base_power = (self.evening_data_charge - self.afternoon_data_charge) * self.ONE_POWER_UNIT + round(
                    (((self.evening_data_price - self.afternoon_data_price) * 100) / 43.2) * 100, 2)
                return base_power + usb_power

            # IF AFTERNOON CHARGE BIGGER THEN EVENING
            if 0 < self.afternoon_data_charge > self.evening_data_charge:
                if 0 < self.afternoon_data_charge > self.evening_data_charge:
                    if self.evening_data_charge < self.afternoon_data_charge:
                        power_meters = self._price_to_power(self.evening_data_price, self.afternoon_data_price)
                        power_battery = (self.afternoon_data_charge - self.evening_data_charge) * self.ONE_POWER_UNIT
                        base_power = power_meters - power_battery
                        return base_power + usb_power

            # IF AFTERNOON CHARGE IS EGUAL ZERO
            if self.afternoon_data_charge == 0:
                raw_meters_power = round((((
                                                   self.evening_data_price - self.morning_data_price - self.MORNING_CORRECTION_PRICE) * 100) / 43.2) * 100,
                                         2)
                battery_power = (
                                        self.evening_data_charge - self.morning_data_charge - self.MORNING_CORRECTION_CHARGE) * self.ONE_POWER_UNIT

                if self.morning_data_charge > self.evening_data_charge:
                    base_power = raw_meters_power - battery_power

                if self.morning_data_charge < self.evening_data_charge:
                    base_power = raw_meters_power + battery_power

                return base_power + usb_power

            return self.FALLBACK_COST
        except(TypeError, ZeroDivisionError):
            return self.FALLBACK_COST

    def _calculate_full_day_cost(self):
        try:
            if self.morning_data_charge == self.afternoon_data_charge == self.evening_data_charge == 0:
                return 0.0

            day_power_watts = self._calculate_full_day_power()
            return round((day_power_watts / 1000) * self.power_tariff, 2)
        except(TypeError, ZeroDivisionError):
            return self.FALLBACK_COST

    @classmethod
    def get_current_month(cls):
        current_month = date.today().month

        return current_month

    @classmethod
    def get_count_of_sun_days(cls):
        current_month = cls.get_current_month()
        current_month_weather = cls.objects.filter(date__month=current_month)
        sunny_days = current_month_weather.filter(weather__name__icontains="sunny")
        if sunny_days:
            return sunny_days.count()
        return 0

    @classmethod
    def get_count_of_month_average_temperature(cls):
        current_month = cls.get_current_month()
        current_month_average_temperature = WeatherDataModel.objects.filter(
            timestamp__month=current_month
        )
        average_temperature = current_month_average_temperature.aggregate(
            average_temperature=Avg('temperature')
        )
        if average_temperature['average_temperature'] is not None:
            return round(average_temperature['average_temperature'], 2)
        return 0

    @classmethod
    def get_count_of_month_average_power(cls):
        current_month = cls.get_current_month()
        current_month_average_power = cls.objects.filter(date__month=current_month)
        average_power = current_month_average_power.aggregate(
            average_power=Avg('full_day_power')
        )
        if average_power['average_power'] is not None:
            return round(average_power['average_power'], 2)
        return 0

    @classmethod
    def get_count_of_month_total_power(cls):
        current_month = cls.get_current_month()
        current_month_total_power = cls.objects.filter(date__month=current_month).aggregate(
            total_power=Sum('full_day_power'))

        return current_month_total_power['total_power'] or 0

    @classmethod
    def get_count_of_month_total_savings(cls):
        current_month = cls.get_current_month()
        current_month_savings = cls.objects.filter(date__month=current_month).aggregate(
            total_power=Sum('full_day_cost'))

        return round(current_month_savings['total_power'], 2) or 0

    @classmethod
    def get_monthly_comparison_data(cls):
        monthly_stats = (
            cls.objects.annotate(month=TruncMonth('date'))
            .values('month')
            .annotate(
                total_power=Sum('full_day_power'),
                total_cost=Sum('full_day_cost')
            )
            .order_by('month')
        )

        result = []
        for stat in monthly_stats:
            if stat['month']:
                result.append({
                    "month": stat['month'].strftime("%Y-%m"),
                    "total_power": round(stat['total_power'], 2) if stat['total_power'] else 0,
                    "total_cost": round(stat['total_cost'], 2) if stat['total_cost'] else 0
                })
        return result

    @classmethod
    def get_power_difference(cls):
        current_month = cls.get_current_month()
        previous_month = current_month - 1 if current_month > 1 else 12

        current_total = cls.objects.filter(date__month=current_month).aggregate(
            total=Sum('full_day_power')
        )['total'] or 0

        previous_total = cls.objects.filter(date__month=previous_month).aggregate(
            total=Sum('full_day_power')
        )['total'] or 0

        if previous_total == 0:
            return None
        difference_power_percentage = ((current_total - previous_total) / previous_total) * 100

        return int(difference_power_percentage)

    @classmethod
    def get_empty_day_message(cls):
        if cls.morning_data_charge == cls.afternoon_data_charge == cls.evening_data_charge == 0:
            return '0% - 0.0 UAH'
        return None

    @classmethod
    def total_generated_power(cls):
        return cls.objects.aggregate(total=Sum('full_day_power'))['total'] or 0

    @classmethod
    def total_cost_power(cls):
        return cls.objects.aggregate(total=Sum('full_day_cost'))['total'] or 0

    def save(self, *args, **kwargs):
        if not self.pk:
            current_tariff_obj = CurrentTariffModel.load()
            self.power_tariff = current_tariff_obj.power_tariff

        self.full_day_power = self._calculate_full_day_power()
        self.full_day_cost = self._calculate_full_day_cost()

        super().save(*args, **kwargs)

    class Meta:
        ordering = ['-date']
        verbose_name = 'entry'
        verbose_name_plural = 'Entries'


class WeatherConditionModel(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class SolarForecastRecordModel(models.Model):
    date = models.DateField(verbose_name="Forecast date", unique=True, default=timezone.now)
    predicted_kwh = models.FloatField(verbose_name="Forecast (kWh)")
    predicted_savings = models.FloatField(verbose_name="Projected savings (UAH)")
    peak_hour = models.IntegerField(verbose_name="Rush hour")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date']
        verbose_name = "forecast record"
        verbose_name_plural = "Forecasts history"

    def __str__(self):
        return f"Forecast for {self.date}: {self.predicted_kwh} kWh"

    def get_actual_data(self):
        return DataEntryLineModel.objects.filter(date=self.date).first()

    @property
    def accuracy_percentage(self):
        actual = self.get_actual_data()
        if not actual or actual.full_day_power == 0:
            return None

        diff = abs(self.predicted_kwh - (actual.full_day_power / 1000))
        accuracy = max(0, 100 - (diff / (actual.full_day_power / 1000) * 100))
        return round(accuracy, 1)


class WeatherDataModel(models.Model):
    # Дата та час виміру/прогнозу
    timestamp = models.DateTimeField(db_index=True)

    # Основні показники для Pandas
    temperature = models.FloatField(help_text="Celsius")
    cloud_cover = models.IntegerField(help_text="Cloud percentage 0-100")
    pressure = models.FloatField(null=True, blank=True)
    humidity = models.IntegerField(null=True, blank=True)

    # Опади (важливо для очищення панелей або їх забруднення)
    precipitation_prob = models.FloatField(default=0, help_text="Chance of precipitation")
    condition_code = models.CharField(max_length=20, help_text="For example: 'sunny', 'rain'")

    class Meta:
        ordering = ['-timestamp']
        verbose_name_plural = "Weather Data Records"

    def __str__(self):
        return f"{self.timestamp.strftime('%d.%m %H:%M')} - {self.temperature}°C"


class SystemMessage(models.Model):
    LEVEL_CHOICES = (
        ('info', 'Info'),
        ('warning', 'Warning'),
        ('danger', 'Danger'),
        ('success', 'Success'),
    )

    created_at = models.DateTimeField(auto_now_add=True)
    level = models.CharField(max_length=10, choices=LEVEL_CHOICES, default='info')
    title = models.CharField(max_length=150)
    text = models.TextField()

    # Зв'язок з конкретним типом події (для іконок у Vue)
    msg_type = models.CharField(max_length=50, default='weather')

    # Поле для зв'язку з календарем (щоб швидко фільтрувати повідомлення за день)
    event_date = models.DateField(db_index=True, auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
