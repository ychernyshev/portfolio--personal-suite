from django.db import models
from django.db.models import Sum
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
    # --- КОНСТАНТИ ---
    POWER = [
        ('200', '200'), ('400', '400'), ('600', '600'), ('800', '800'),
    ]

    UNIT_CONVERSION_FACTOR = 20.48  # Коефіцієнт перетворення заряду в потужність
    CHARGE_DIFFERENCE_THRESHOLD = 10  # Порогова різниця заряду
    MORNING_CORRECTION_CHARGE = 6  # Корекція ранкового заряду
    MORNING_CORRECTION_PRICE = 0.6  # Корекція ранкової ціни

    DEFAULT_COST_LOW = 0.86  # дефолтна формула при низькій різниці
    DEFAULT_COST_HIGH = 0.43  # дефолтна формула при високій різниці
    FALLBACK_COST = 0.0  # запасне значення

    POWER_LOW = 200  # дефолтна потужність при низькій різниці
    POWER_HIGH = 100  # дефолтна потужність при високій різниці

    date = models.DateField(verbose_name='Дата')
    power = models.CharField(choices=POWER, max_length=3, default='600', verbose_name='Потужність системи')
    weather = models.ManyToManyField('WeatherConditionModel', db_index=True, related_name='weather', verbose_name='Погода')
    morning_data_charge = models.IntegerField(verbose_name='Ранковий рівень заряду')
    morning_data_price = models.FloatField(verbose_name='Вартість використаної енергії на ранок')
    afternoon_data_charge = models.IntegerField(verbose_name='Денний рівень заряду', default=0)
    afternoon_data_price = models.FloatField(verbose_name='Вартість використаної енергії на день', default=0)
    evening_data_charge = models.IntegerField(verbose_name='Вечірній рівень заряду')
    evening_data_price = models.FloatField(verbose_name='Вартість використаної енергії на вечір')
    default_day_energy_formula = models.BooleanField(default=False)
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

    def _calculate_full_day_power(self):
        try:
            if self.morning_data_charge == self.afternoon_data_charge == self.evening_data_charge == 0:
                return 0
            if self.afternoon_data_price == self.evening_data_price or self.morning_data_price == self.evening_data_price:
                return (self.evening_data_charge - self.afternoon_data_charge) * self.UNIT_CONVERSION_FACTOR
            if 0 < self.afternoon_data_charge < self.evening_data_charge:
                return (self.evening_data_charge - self.afternoon_data_charge) * self.UNIT_CONVERSION_FACTOR + round(
                    (((self.evening_data_price - self.afternoon_data_price) * 100) / 43.2) * 100, 2)
            if 0 < self.afternoon_data_charge > self.evening_data_charge:
                if self.afternoon_data_charge - self.evening_data_charge <= self.CHARGE_DIFFERENCE_THRESHOLD:
                    return self.POWER_HIGH
                if self.afternoon_data_charge - self.evening_data_charge > self.CHARGE_DIFFERENCE_THRESHOLD:
                    return self.POWER_LOW
            if self.afternoon_data_charge == 0:
                if self.morning_data_charge < self.evening_data_charge:
                    return (
                                   self.evening_data_charge - self.morning_data_charge - self.MORNING_CORRECTION_CHARGE) * self.UNIT_CONVERSION_FACTOR + round(
                        (((
                                  self.evening_data_price - self.morning_data_price - self.MORNING_CORRECTION_PRICE) * 100) / 43.2) * 100,
                        2)
                if self.morning_data_charge - self.evening_data_charge <= self.CHARGE_DIFFERENCE_THRESHOLD:
                    return self.POWER_HIGH
                if self.morning_data_charge - self.evening_data_charge > self.CHARGE_DIFFERENCE_THRESHOLD:
                    return self.POWER_LOW
            return self.FALLBACK_COST
        except(TypeError, ZeroDivisionError):
            return self.FALLBACK_COST

    def _calculate_full_day_cost(self):
        try:
            if self.morning_data_charge == self.afternoon_data_charge == self.evening_data_charge == 0:
                return 0.0
            if self.afternoon_data_price == self.evening_data_price or self.morning_data_price == self.evening_data_price:
                return (((
                                 self.evening_data_charge - self.afternoon_data_charge) * self.UNIT_CONVERSION_FACTOR) / 1000) * self.power_tariff
            if 0 < self.afternoon_data_charge < self.evening_data_charge:
                return (((
                                 self.evening_data_charge - self.afternoon_data_charge) * self.UNIT_CONVERSION_FACTOR) / 1000) * self.power_tariff + (
                               self.evening_data_price - self.afternoon_data_price)
            if 0 < self.afternoon_data_charge > self.evening_data_charge and self.default_day_energy_formula:
                if self.afternoon_data_charge - self.evening_data_charge <= self.CHARGE_DIFFERENCE_THRESHOLD:
                    return self.DEFAULT_COST_LOW
                if self.afternoon_data_charge - self.evening_data_charge > self.CHARGE_DIFFERENCE_THRESHOLD:
                    return self.DEFAULT_COST_HIGH
            if 0 < self.afternoon_data_charge > self.evening_data_charge:
                return (((
                                 self.evening_data_charge - self.afternoon_data_charge) * self.UNIT_CONVERSION_FACTOR) / 1000) * self.power_tariff + (
                               self.evening_data_price - self.afternoon_data_price)
            if self.afternoon_data_price == 0:
                if self.morning_data_charge < self.evening_data_charge:
                    return (((
                                     self.evening_data_charge - self.morning_data_charge - self.MORNING_CORRECTION_CHARGE) * self.UNIT_CONVERSION_FACTOR) / 1000) * self.power_tariff + (
                                   self.evening_data_price - self.morning_data_price - self.MORNING_CORRECTION_PRICE)
                if self.morning_data_charge - self.evening_data_charge <= self.CHARGE_DIFFERENCE_THRESHOLD:
                    return self.DEFAULT_COST_LOW
                if self.morning_data_charge - self.evening_data_charge > self.CHARGE_DIFFERENCE_THRESHOLD:
                    return self.DEFAULT_COST_HIGH
            return self.FALLBACK_COST
        except(TypeError, ZeroDivisionError):
            return self.FALLBACK_COST

    def get_empty_day_message(self):
        if self.morning_data_charge == self.afternoon_data_charge == self.evening_data_charge == 0:
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


class SolarForecastRecord(models.Model):
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
