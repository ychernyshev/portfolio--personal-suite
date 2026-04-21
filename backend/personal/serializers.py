from rest_framework import serializers

from personal.models import ProjectItemModel
class ProjectItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectItemModel
        fields = '__all__'