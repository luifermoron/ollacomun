from django.shortcuts import render

from rest_framework import generics, status, serializers, filters

# Create your views here.
from rest_framework.views import APIView

from places.models import Place
from places.serializers import PlaceSerializer

from rest_framework.response import Response
from rest_framework import status


def placefilter(id, uuid):
    if id is None or uuid is None:
        return None
    places = Place.objects.filter(id=id, uuid=uuid)

    if places.exists():
        return places.first()

    return None


class GetPlaces(generics.ListAPIView):
    filter_backends = (filters.OrderingFilter,)
    ordering = ('-id')
    serializer_class = PlaceSerializer

    def get_serializer_context(self, *args, **kwargs):
        return {"request": self.request}

    def get_queryset(self, *args, **kwargs):
        return Place.objects.filter(is_active=True)


class GetPlace(generics.RetrieveAPIView):
    serializer_class = PlaceSerializer
    lookup_field = 'id'

    def get_queryset(self, *args, **kwargs):
        id = self.kwargs.get("id", None)
        uuid = self.kwargs.get("uuid", None)
        place = placefilter(id, uuid)

        if place is None:
            return Place.objects.none()
        return place


class PlaceView(APIView):

    def get(self, request, format=None):
        id = int(request.GET.get('id', None))
        uuid = request.GET.get('uuid', None)
        place = placefilter(id, uuid)

        if place is None:
            return Place.objects.none()
        return place

    def put(self, request, *args, **kwargs):
        id = request.data.get('id')
        uuid = request.data.get('uuid')
        is_active = request.data.get('is_active')

        place = placefilter(id, uuid)
        if place is None or is_active is None:
            return Response(status=status.HTTP_404_NOT_FOUND)

        place.is_active = is_active
        place.save(update_fields=['is_active'])

        return Response(status=status.HTTP_204_NO_CONTENT)
