from rest_framework import serializers
from .models import City, Street, Shop


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ('name',)


class StreetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Street
        fields = ('name', 'city',)


class ShopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shop
        fields = '__all__'

