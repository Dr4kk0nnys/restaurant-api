from rest_framework import serializers

from api.models import Restaurant


class RestaurantSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Restaurant
        fields = ['id', 'email', 'password', 'restaurant_name', 'owner_name', 'address', 'phone_number', 'token_id']
