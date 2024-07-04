from django.urls import path, include

from .views import ZoneApiView, InstitutionApiView, BuildingApiView

urlpatterns = [
    path('api/v1/zones/', ZoneApiView.as_view({'get': 'list', 'post': 'create'})),
    path('api/v1/zone/<int:pk>/', ZoneApiView.as_view({'get': 'retrieve', 'delete': 'destroy'})),
    path('api/v1/institutions/', InstitutionApiView.as_view({'get': 'list', 'post': 'create'})),
    path('api/v1/institution/<int:pk>/', InstitutionApiView.as_view({'get': 'retrieve', 'delete': 'destroy'})),
    path('api/v1/buildings/', BuildingApiView.as_view({'get': 'list', 'post': 'create'})),
    path('api/v1/building/<int:pk>/', BuildingApiView.as_view({'get': 'retrieve', 'delete': 'destroy'})),

    path('api-auth/', include('rest_framework.urls'))
]
