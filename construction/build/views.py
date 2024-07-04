from django.shortcuts import render

from .models import Institution,Building,Zone
from .serializers import ZoneSerializer,InstitutionSerializer,BuildingSerializer
from .permissions import CustomPermission

from rest_framework.viewsets import ModelViewSet

class ZoneApiView(ModelViewSet):
    queryset = Zone.objects.all()
    serializer_class = ZoneSerializer
    permission_classes = [CustomPermission]


class InstitutionApiView(ModelViewSet):
    queryset = Institution.objects.all()
    serializer_class = InstitutionSerializer
    permission_classes = [CustomPermission]


class BuildingApiView(ModelViewSet):
    queryset = Building.objects.all()
    serializer_class = BuildingSerializer
    permission_classes = [CustomPermission]

