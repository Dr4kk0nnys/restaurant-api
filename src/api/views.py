from django.core.exceptions import ObjectDoesNotExist
from django.core.validators import MinValueValidator

from rest_framework import viewsets
from rest_framework.response import Response

from api.utils.credentials import generate_token, generate_hash

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

    def get_serialized_data(self, data):
        try:
            info = []

            """
            data.values() should look like this:
                [0]: email
                [1]: password
                [2]: restaurant name
                [3]: owner name
                [4]: address
                [5]: phone number
            """
            for value in data.values():
                info.append(value)
            return info
        except:
            return None

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

        # get_serialized_data() returns None if an error occurs while trying to unpack the data.
        data = self.get_serialized_data(serializer.data)
        if not data:
            return Response({'Error occurred trying to get data': 'true'})

        # The restaurant name already exists.
        if Restaurant.objects.filter(restaurant_name=data[0]):
            return Response({'Already Created': 'True'})

        test = Restaurant.objects.get_or_create(
            email=data[0],
            password=generate_hash(data[1]),
            restaurant_name=data[2],
            owner_name=data[3],
            address=data[4],
            phone_number=data[5],
            token_id=generate_token(data[0], data[1])
        )

        return Response(data)

    def put(self, request):
        (serializer, is_valid) = self.get_serializer_and_is_valid(request.data)
        if not is_valid:
            return Response({'Serializer not valid': 'true'})

        # get_serialized_data() returns None if an error occurs while trying to unpack the data.
        data = self.get_serialized_data(serializer.data)
        if not data:
            return Response({'Error occurred trying to get data': 'true'})

        # TODO: Validate the info ( it will check if the token id exists, etc ... )
        Restaurant.objects.select_for_update().filter(token_id=serializer.data['token_id']).update(
            email=data[0],
            password=generate_hash(data[1]),
            restaurant_name=data[2],
            owner_name=data[3],
            address=data[4],
            phone_number=data[5],
            token_id=generate_token(data[0], data[1])
        )
        return Response({'Updated': 'true'})

    def delete(self, request):
        try:
            token_id = request.data['token_id']
        except KeyError:
            return Response({'Could not find the token id in the request body': 'true'})

        # TODO: Validate the token id.
        try:
            Restaurant.objects.get(token_id=token_id).delete()
        except Restaurant.DoesNotExist:
            return Response({'Deleted': 'false'})

        return Response({'Deleted': 'true'})
