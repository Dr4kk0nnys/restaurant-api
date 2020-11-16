from django.urls import path, include

from rest_framework.routers import DefaultRouter

from api import views


router = DefaultRouter()
router.register(r'', views.IndexViewset, basename='index')
router.register(r'restaurant-register', views.RestaurantRegisterViewset, basename='restaurant-register')


urlpatterns = [
    path('', include(router.urls))
]
