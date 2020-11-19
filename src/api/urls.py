from django.urls import path, include

from rest_framework.routers import DefaultRouter

from api import views


router = DefaultRouter()
router.register(r'', views.IndexViewset, basename='index')
router.register(r'restaurant', views.RestaurantViewset, basename='restaurant')
router.register(r'client', views.ClientViewset, basename='client')


urlpatterns = [
    path('', include(router.urls))
]
