# SPDX-License-Identifier: AGPL-3.0-or-later


from rest_framework import serializers

from calculator.models import (DataEntryLineModel,
                               CurrentTariffModel,
                               WeatherConditionModel,
                               WeatherDataModel,
                               SolarForecastRecordModel,
                               GeolocationModel,
                               PanelsArrayModel,
                               UserTimezoneModel)


class WeatherConditionSerializer(serializers.ModelSerializer):
    class Meta:
        model = WeatherConditionModel
        fields = ['id', 'name']

class CurrentTariffSerializer(serializers.ModelSerializer):
    class Meta:
        model = CurrentTariffModel
        fields = ['power_tariff', 'last_updated']

class DataEntrySerializer(serializers.ModelSerializer):
    empty_day_message = serializers.ReadOnlyField(source='get_empty_day_message')
    weather_details = WeatherConditionSerializer(source='weather', many=True, read_only=True)

    class Meta:
        model = DataEntryLineModel
        fields = '__all__'
        read_only_fields = ['full_day_power', 'full_day_cost', 'power_tariff']


class WeatherDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = WeatherDataModel
        fields = '__all__'


class SolarForecastRecordSerializer(serializers.ModelSerializer):
    day_length = serializers.ReadOnlyField(source='get_day_length')
    wind_speed_alert = serializers.ReadOnlyField(source='check_wind_speed')

    class Meta:
        model = SolarForecastRecordModel
        fields = '__all__'
        read_only_fields = ['sunrise', 'sunset']


class GeolocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = GeolocationModel
        fields = '__all__'


class PanelsArraySerializer(serializers.ModelSerializer):
    class Meta:
        model = PanelsArrayModel
        fields = '__all__'
        extra_kwargs = {
            'user': {'required': False},
            'peak_power_kwp': {'required': False}
        }

    def validate_efficiency(self, value):
        if value > 1.0:
            return value / 100.0
        return value


class UserTimezoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserTimezoneModel
        fields = '__all__'