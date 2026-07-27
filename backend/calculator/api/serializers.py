# SPDX-License-Identifier: AGPL-3.0-or-later
from rest_framework import serializers

from calculator.models import (DataEntryLineModel,
                               CurrentTariffModel,
                               WeatherConditionModel,
                               WeatherDataModel,
                               SolarForecastRecordModel,
                               PanelsArrayModel,
                               UserProfileSettingsModel,
                               SystemEventModel,
                               PeakEventModel,
                               WindEventModel, )


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


class UserProfileSettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfileSettingsModel
        fields = '__all__'
        read_only_fields = ['user']


class PeakEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = PeakEventModel
        fields = '__all__'
        read_only_fields = ['user']


class WindEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = WindEventModel
        fields = '__all__'
        read_only_fields = ['user']


class SystemEventSerializer(serializers.ModelSerializer):
    wind_records = WindEventSerializer(many=True, read_only=True)
    peak_records = PeakEventSerializer(many=True, read_only=True)

    title = serializers.SerializerMethodField()
    text = serializers.SerializerMethodField()
    level = serializers.SerializerMethodField()
    msg_type = serializers.SerializerMethodField()

    class Meta:
        model = SystemEventModel
        fields = ['id', 'date', 'payload', 'created_at', 'updated_at',
                  'title', 'text', 'level', 'msg_type',
                  'wind_records', 'peak_records']
        read_only_fields = ['user']

    def get_title(self, obj):
        wind = obj.wind_records.first()
        return wind.title if wind else obj.payload.get('title', 'Notification')

    def get_text(self, obj):
        wind = obj.wind_records.first()
        return wind.message if wind else obj.payload.get('message', '')

    def get_level(self, obj):
        wind = obj.wind_records.first()
        return wind.category.lower() if wind else obj.payload.get('level', 'info')

    def get_msg_type(self, obj):
        peak = obj.peak_records.first()
        return peak.status.lower() if peak else obj.payload.get('category', 'info')

    def get_peak_hour(self, obj):
        peak = obj.peak_records.first()
        return peak.peak_hour if peak else obj.payload.get('peak_hour', None)

# DEPRECATED
# class GeolocationSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = GeolocationModel
#         fields = '__all__'
#
#
# class UserTimezoneSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = UserTimezoneModel
#         fields = '__all__'
#         read_only_fields = ['user']
#
#
# class UserLanguageSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = UserLanguageModel
#         fields = '__all__'
#         read_only_fields = ['user']
#
#
# class UserCurrencySerializer(serializers.ModelSerializer):
#     class Meta:
#         model = UserCurrencyModel
#         fields = '__all__'
#         read_only_fields = ['user']
