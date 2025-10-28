"""URLs do app Famlias."""
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import FamiliaViewSet


router = DefaultRouter()
router.register(r'', FamiliaViewSet, basename='familia')

app_name = 'familias'

urlpatterns = [
    path('', include(router.urls)),
]
