from rest_framework import generics
from .models import City, Street, Shop
from .serializers import CitySerializer, StreetSerializer, ShopSerializer

from datetime import datetime

current_time = datetime.now().time()


class CityList(generics.ListAPIView):
    queryset = City.objects.all()
    serializer_class = CitySerializer


class StreetList(generics.ListAPIView):
    serializer_class = StreetSerializer

    def get_queryset(self):
        city_id = self.kwargs['city_id']
        return Street.objects.filter(city_id=city_id)


class ShopList(generics.ListCreateAPIView):
    serializer_class = ShopSerializer

    def get_queryset(self):
        city = self.request.query_params.get('city', None)
        street = self.request.query_params.get('street', None)
        open_status = self.request.query_params.get('open', None)

        queryset = Shop.objects.all()

        if city:
            queryset = queryset.filter(city__name=city)
        if street:
            queryset = queryset.filter(street__name=street)
        if open_status is not None:
            if open_status == '0':
                
                queryset = queryset.filter(closing_time__lt=current_time)
            else:

                queryset = queryset.filter(opening_time__gt=current_time)

        return queryset
