from restaurant.models import *
from restaurant.serializers import *
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'restaurant': reverse('restaurant-list', request=request, format=format),
        'cuisine_type': reverse('cuisine_type-list', request=request, format=format),
        'outlet_type': reverse('outlet_type-list', request=request, format=format),
        'affordability': reverse('affordability-list', request=request, format=format),
    })

class RestaurantList(APIView):
    def get(self, request, format=None):
        restaurants = Restaurant.objects.all()
        serializer = RestaurantSerializer(restaurants, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = RestaurantSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

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
