from rest_framework import serializers

from personal.models import ProjectItemModel, ContactMessageModel


class ProjectItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectItemModel
        fields = '__all__'


class ContactMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactMessageModel
        fields = '__all__'