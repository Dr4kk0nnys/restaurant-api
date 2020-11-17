from django.core.exceptions import ObjectDoesNotExist
from django.core.validators import MinValueValidator

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
    The RestaurantViewSet may list, create, update and delete info.

    list: Return the account information being guided by the token id.

    create: Creates a brand new account.

    update: Update all the info of a certain account being guided by the token id.

    delete: Delete a certain account being guided by the token id.
    """
    # TODO: Custom validation to the serializer fields ( such as, is the address correctly sended ? )
    # TODO: Create a function to validate the info received in the request

    def get_serializer_and_is_valid(self, data):
        serializer = RestaurantSerializer(data=data)

        if not serializer.is_valid():
            return (serializer, False)
        return (serializer, True)

    # TODO: Implement the validation to the values received
    def validate_info(self, values):
        pass

    def list(self, request):
        (serializer, is_valid) = self.get_serializer_and_is_valid(request.data)
        if not is_valid:
            return Response({'Serializer not valid': 'true'})

        return Response(Restaurant.objects.filter(token_id=serializer.data['token_id']).values())

    def create(self, request):
        (serializer, is_valid) = self.get_serializer_and_is_valid(request.data)
        if not is_valid:
            return Response({'Serializer not valid': 'true'})

        # TODO: While registering the restaurant the user won't have a token id yet, so this field can be None ( explain in the documentation )
        [restaurant_name, owner_name, address, phone_number, token_id] = serializer.data.values()

        # The restaurant name already exists.
        if Restaurant.objects.filter(restaurant_name=restaurant_name):
            return Response({'Already Created': 'True'})
        
        # TODO: Create the generate_token_id() function
        Restaurant.objects.get_or_create(
            restaurant_name=restaurant_name,
            owner_name=owner_name,
            address=address,
            phone_number=phone_number,
            token_id='fhdsakjfhsakjfhaksjdfhasdkfjhasjdfhasjkfdhasjhfsdkjfhasjfhasdjkfhag3yughfsdjkfhasjdhfaklsjdfhajksfdh'
        )

        return Response({'Created': 'true'})

    def put(self, request):
        (serializer, is_valid) = self.get_serializer_and_is_valid(request.data)
        if not is_valid:
            return Response({'Serializer not valid': 'true'})

        [restaurant_name, owner_name, address, phone_number, token_id] = serializer.data.values()

        # TODO: Validate the info ( it will check if the token id exists, etc ... )
        
        Restaurant.objects.select_for_update().filter(token_id=token_id).update(
            restaurant_name=restaurant_name,
            owner_name=owner_name,
            address=address,
            phone_number=phone_number
        )
        return Response({'Created': 'true'})

    def delete(self, request):
        (serializer, is_valid) = self.get_serializer_and_is_valid(request.data)
        if not is_valid:
            return Response({'Serializer not valid': 'true'})
        
        [restaurant_name, owner_name, address, phone_number, token_id] = serializer.data.values()

        try:
            Restaurant.objects.get(token_id=token_id).delete()
        except Restaurant.DoesNotExist:
            return Response({'Deleted': 'false'})

        return Response({'Deleted': 'true'})
