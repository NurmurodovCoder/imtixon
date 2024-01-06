from rest_framework import serializers
from .models import City, Street, Shop
from datetime import datetime

current_time = datetime.now().time()


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ('name',)


class StreetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Street
        fields = ('name', 'city',)


class ShopSerializer(serializers.ModelSerializer):
    city = CitySerializer()
    street = StreetSerializer()

    class Meta:
        model = Shop
        fields = '__all__'

    def get_opening(self, obj):
        current_time = datetime.now().time()

        return obj.opening_time < current_time < obj.closing_time

