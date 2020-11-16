from rest_framework import serializers

from api.models import RestaurantRegister


class RestaurantRegisterSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = RestaurantRegister
        fields = '__all__'
