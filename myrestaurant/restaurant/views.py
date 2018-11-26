from restaurant.models import *
from restaurant.serializers import *
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse
from rest_framework import generics
from django_filters import rest_framework as filters
import json

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'restaurant': reverse('restaurant-list', request=request, format=format),
        'cuisine_type': reverse('cuisine_type-list', request=request, format=format),
        'outlet_type': reverse('outlet_type-list', request=request, format=format),
        'affordability': reverse('affordability-list', request=request, format=format),
    })

# class RestaurantList(APIView):
#     def post(self, request, format=None):
#         kwargs = request.data
#         data = Restaurant.objects.filter(**kwargs)
#         serializer = RestaurantSerializer(data, many=True)
#         return Response(serializer.data)

class RestaurantFilter(filters.FilterSet):
    cuisine_type = filters.AllValuesMultipleFilter()
    outlet_type = filters.AllValuesMultipleFilter()
    affordability = filters.AllValuesMultipleFilter()

    class Meta:
        model = Restaurant
        fields = ['cuisine_type', 'outlet_type', 'affordability','halal']

class RestaurantList(generics.ListAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
    filterset_class = RestaurantFilter

class RestaurantDetail(APIView):
    def get_object(self, pk):
        try:
            return Restaurant.objects.get(pk=pk)
        except Restaurant.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        restaurant = self.get_object(pk)
        serializer = RestaurantSerializer(restaurant)
        return Response(serializer.data)

class CuisineTypeList(APIView):
    def get(self, request, format=None):
        cuisine_type = CuisineType.objects.all()
        serializer = CuisineTypeSerializer(cuisine_type, many=True)
        return Response(serializer.data)

class OutletTypeList(APIView):
    def get(self, request, format=None):
        outlet_type = OutletType.objects.all()
        serializer = OutletTypeSerializer(outlet_type, many=True)
        return Response(serializer.data)

class AffordabilityList(APIView):
    def get(self, request, format=None):
        affordability = Affordability.objects.all()
        serializer = AffordabilitySerializer(affordability, many=True)
        return Response(serializer.data)
