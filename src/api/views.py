from django.core.exceptions import ObjectDoesNotExist
from django.core.validators import MinValueValidator
from django.db.models import Q

from rest_framework import viewsets
from rest_framework.response import Response

from api.models import Restaurant, Client
from api.serializers import RestaurantSerializer, ClientSerializer

from api.utils.credentials import generate_token, generate_hash


# TODO: Standardize the return of the Responses
# TODO: Create some more organized files on the root directory


class IndexViewset(viewsets.ViewSet):
    # TODO: Make the index return the possible links of the api
    def list(self, request, format=None, pk=None):
        return Response({'Sup brother': 'sup'})


class RestaurantViewset(viewsets.ViewSet):
    """
    The RestaurantViewSet may list, create, update and delete info.

    list: Return the account information being guided by the token id.

    create: Creates a brand new account requiring all the information.

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
            data.values() looks like this:
                [0]: email
                [1]: password
                [2]: restaurant name
                [3]: owner name
                [4]: address
                [5]: phone number
                [6]: token id
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
        try:
            token_id = request.data['token_id']
        except KeyError:
            return Response({'Error trying to get the token_id': 'true'})
        
        return Response(Restaurant.objects.filter(token_id=token_id).values())

    def create(self, request):
        (serializer, is_valid) = self.get_serializer_and_is_valid(request.data)
        if not is_valid:
            return Response({'Serializer not valid': 'true'})

        # get_serialized_data() returns None if an error occurs while trying to unpack the data.
        data = self.get_serialized_data(serializer.data)
        if not data:
            return Response({'Error occurred trying to get data': 'true'})

        # The restaurant name already exists or the email is already being used.
        if Restaurant.objects.filter(Q(restaurant_name=data[2]) | Q(email=data[0])):
            return Response({'Already Created': 'True'})

        Restaurant.objects.get_or_create(
            email=data[0],
            password=generate_hash(data[1]),
            restaurant_name=data[2],
            owner_name=data[3],
            address=data[4],
            phone_number=data[5],
            token_id=generate_token(data[0], data[1])
        )

        return Response({'success': 'true', 'data': data, 'error': {}})

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

        try:
            Restaurant.objects.get(token_id=token_id).delete()
        except Restaurant.DoesNotExist:
            return Response({'Deleted': 'false'})

        return Response({'Deleted': 'true'})


class ClientViewset(viewsets.ViewSet):
    """
    The client viewset may list, create, update or delete a client.

    list: List the client information being guided by the token id.

    create: Creates a new client with all the info.

    update: Updates the client info being guide by the token id.

    delete: Delete a client being guided by the token id.
    """
    def list(self, request):
        try:
            client = Client.objects.get(token_id=request.data['token_id']).values()
        except KeyError:
            return Response({'Error trying to get the token id': 'true'})
        
        return Response({'success': 'true', 'data': client, 'error': {}})

    def create(self, request):
        serializer = ClientSerializer(data=request.data)

        if not serializer.is_valid():
            return Response({'The serializer is not valid': 'true'})

        Client.objects.get_or_create(
            email=serializer.data['email'],
            password=generate_hash(serializer.data['password']),
            name=serializer.data['name'],
            address=serializer.data['address'],
            token_id=generate_token(serializer.data['email'], serializer.data['password'])
        )

        return Response(serializer.data)

    def update(self, request):
        serializer = ClientSerializer(data=request.data)

        if not serializer.is_valid():
            return Response({'The serializer is not valid': 'true'})
        
        Client.objects.select_for_update().filter(token_id=serializer.data['token_id']).update(
            email=serializer.data['email'],
            password=generate_hash(serializer.data['password']),
            name=serializer.data['name'],
            address=serializer.data['address'],
            token_id=generate_token(serializer.data['email'], serializer.data['password'])
        )

        return Response(serializer.data)
    
    def delete(self, request):
        try:
            Client.objects.get(token_id=request.dta['token_id']).delete()
        except Client.DoesNotExist:
            return Response({'Deleted:': 'false'})
        
        return Response({'Deleted': 'true'})
