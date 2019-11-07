from django.shortcuts import render

from rest_framework import generics, status, serializers, filters

# Create your views here.
from places.models import Place
from places.serializers import PlaceSerializer


class GetPlaces(generics.ListAPIView):
    filter_backends = (filters.OrderingFilter,)
    ordering = ('-id')
    serializer_class = PlaceSerializer

    def get_serializer_context(self, *args, **kwargs):
        return {"request": self.request}

    def get_queryset(self, *args, **kwargs):
        return Place.objects.filter(is_active=True)
