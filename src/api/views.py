from django.core.exceptions import ObjectDoesNotExist

from rest_framework import viewsets
from rest_framework.response import Response

from api.models import Restaurant

from api.serializers import RestaurantSerializer


# TODO: Standardize the return of the Responses


class IndexViewset(viewsets.ViewSet):
    # TODO: Make the index return the possible links of the api
    def list(self, request, format=None, pk=None):
        return Response({'Sup brother': 'sup'})


class RestaurantViewset(viewsets.ViewSet):
    """
    The restaurant view set may update, create or delete a restaurant.

    create: Checks if there is already a restaurant with the name. If it doesn't, it creates a new restaurant.

    update: Checks if there is a restaurant with the info, if it does, updates the info of it.

    delete: Checks if there is a restaurant with the info, if it does, it gets deleted.
    """
    # TODO: Custom validation to the serializer fields ( such as, is the address correctly sended ? )
    # TODO: Create a function to validate the info received in the request
    # TODO: Create a function to get the default values ( restaurant name, owner name, etc ... )

    def create(self, request, format=None, pk=None):
        serializer = RestaurantSerializer(data=request.data)

        if not serializer.is_valid():
            return Response({'Created': 'false'})

        # unpacking data
        [restaurant_name, owner_name, address, phone_number, token_id] = serializer.data.values()

        # The restaurant name already exists.
        if Restaurant.objects.filter(restaurant_name=restaurant_name):
            return Response({'Created': 'false'})
        
        Restaurant.objects.get_or_create(
            restaurant_name=restaurant_name,
            owner_name=owner_name,
            address=address,
            phone_number=phone_number,
            token_id=token_id
        )

        return Response({'Created': 'true'})

    # TODO: You need some credentials to update the info ( token id ) ?
    def put(self, request, format=None, pk=None):
        serializer = RestaurantSerializer(data=request.data)

        if not serializer.is_valid():
            return Response({'Created': 'false'})

        [restaurant_name, owner_name, address, phone_number, token_id] = serializer.data.values()

        try:
            restaurant = Restaurant.objects.select_for_update().get(token_id=token_id)
        except Restaurant.DoesNotExist:
            return Response({'Created': 'false'})
        
        restaurant.restaurant_name = restaurant_name
        restaurant.owner_name = owner_name
        restaurant.address = address
        restaurant.phone_number = phone_number
        
        restaurant.save()

        return Response({'Created': 'true'})
