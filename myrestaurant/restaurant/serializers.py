from rest_framework import serializers
from restaurant.models import * 
from address.models import Address

class OutletTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = OutletType
        fields = '__all__'

class CuisineTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CuisineType
        fields = '__all__'

class AffordabilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Affordability
        fields = '__all__'

class OpeningTimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = OpeningTime
        fields = '__all__'

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'

class RestaurantSerializer(serializers.ModelSerializer):
    outlet_type = OutletTypeSerializer(read_only=True)
    cuisine_type = CuisineTypeSerializer(read_only=True)
    affordability = AffordabilitySerializer(read_only=True)
    opening_times = OpeningTimeSerializer(many=True, read_only=True)
    address = AddressSerializer(read_only=True)

    class Meta:
        model = Restaurant
        fields = '__all__'
