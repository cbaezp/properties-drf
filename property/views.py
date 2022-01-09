from django.shortcuts import render
from rest_framework import generics

from .models import Category, Property
from .serializers import PropertySerializer


class PropertyListView(generics.ListAPIView):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer


class PropertyView(generics.RetrieveAPIView):
    lookup_field = "slug"
    queryset = Property.objects.all()
    serializer_class = PropertySerializer
