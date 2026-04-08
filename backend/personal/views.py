from django.shortcuts import render
from rest_framework import viewsets

from personal.models import ProjectItemModel
from personal.serializers import ProjectItemSerializer


# Create your views here.
class ProjectItemViewSet(viewsets.ModelViewSet):
    class Meta:
        model = ProjectItemModel
        serializer_class = ProjectItemSerializer
