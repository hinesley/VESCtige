import json

from rest_framework import generics

from rides.models import Ride
from rides.serializers import RideSerializer


class RideListCreateAPIView(generics.ListCreateAPIView):
    queryset = Ride.objects.all()
    serializer_class = RideSerializer
