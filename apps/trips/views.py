from django.shortcuts import render
from rest_framework import viewsets, permissions

from apps.trips.models import Trip
from apps.trips.serializers import TripSerializer


class TripView(viewsets.ReadOnlyModelViewSet):
    lookup_field = 'id'
    lookup_url_kwarg = 'trip_id'
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Trip.objects.all()
    serializer_class = TripSerializer
