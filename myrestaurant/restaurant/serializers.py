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
    WEEKDAYS = (
       (1, 'Monday'),
       (2, 'Tuesday'),
       (3, 'Wednesday'),
       (4, 'Thursday'),
       (5, 'Friday'),
       (6, 'Saturday'),
       (7, 'Sunday'),
    )
    weekday_display = serializers.CharField(source='get_weekday_display')

    from_hour = serializers.TimeField(format=('%I:%M %p'))
    to_hour =  serializers.TimeField(format=('%I:%M %p'))

    # def get_weekday_name(self, obj):
    #     return obj.get_weekday_display()
    #
    # weekday_name = serializers.SerializerMethodField(read_only=True, source='get_weekday_name')

    class Meta:
        model = OpeningTime
        fields = ('id', 'weekday', 'weekday_display', 'from_hour', 'to_hour')

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
