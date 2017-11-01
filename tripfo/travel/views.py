from rest_framework import viewsets

from travel.models import Travel
from travel.serializers import TravelSerializer


class TravelViewSet(viewsets.ModelViewSet):
    queryset = Travel.objects.all()
    serializer_class = TravelSerializer
