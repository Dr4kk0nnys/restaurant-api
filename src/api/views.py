from django.shortcuts import render
from django.http import HttpResponse

from rest_framework import viewsets
from rest_framework.response import Response

from api.serializers import RestaurantRegisterSerializer


class IndexViewset(viewsets.ViewSet):
    def list(self, request, format=None, pk=None):
        return Response({'Sup brother': 'sup'})


class RestaurantRegisterViewset(viewsets.ViewSet):
    def create(self, request, format=None, pk=None):
        serializer = RestaurantRegisterSerializer(data=request.data)

        if not serializer.is_valid():
            return Response({'Created': 'false'})

        return Response({'Created': 'true'})
