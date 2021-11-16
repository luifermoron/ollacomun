
from rest_framework import serializers

from places.models import Place


class PlaceSerializer(serializers.ModelSerializer):
    images = serializers.StringRelatedField(many=True)
    class Meta:
        model = Place
        fields = (
            'id', 'name', 'description', 'longitude', 'latitude', 'images', )