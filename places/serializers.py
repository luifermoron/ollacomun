
from rest_framework import serializers

from places.models import Place


class PlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Place
        fields = (
            'id', 'name', 'description', 'longitude', 'latitude', )