from rest_framework import serializers

from calculator.models import DataEntryLineModel, CurrentTariffModel, WeatherConditionModel, WeatherDataModel

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