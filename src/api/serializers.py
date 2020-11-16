from rest_framework import serializers

from api.models import Restaurant


class RestaurantSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Restaurant
        fields = '__all__'
