from django.urls import path
from .views import CityList, StreetList, ShopList

urlpatterns = [
    path('city/', CityList.as_view(), name='city-list'),
    path('city/<int:city_id>/street/', StreetList.as_view(), name='street-list'),
    path('shop/', ShopList.as_view(), name='shop-list'),
]
