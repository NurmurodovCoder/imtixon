from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from .models import City, Street, Shop
from datetime import datetime


class ShopAPITests(APITestCase):
    def setUp(self):
        # Create sample City
        self.city = City.objects.create(name='Tashkent')

        # Create sample Street
        self.street = Street.objects.create(name='Broadway', city=self.city)

        # Create sample Shop
        self.shop = Shop.objects.create(
            name='Sample Shop',
            city=self.city,
            street=self.street,
            house='123',
            opening_time=datetime.now().time(),
            closing_time=datetime.now().time()
        )

    def test_get_city_list(self):
        url = reverse('city-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_street_list(self):
        url = reverse('street-list', kwargs={'city_id': self.city.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_shop_list(self):
        url = reverse('shop-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_filter_shop_list_by_city(self):
        url = reverse('shop-list')
        response = self.client.get(url, {'city': 'Tashkent'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_filter_shop_list_by_street(self):
        url = reverse('shop-list')
        response = self.client.get(url, {'street': 'Broadway'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_filter_shop_list_by_open_status(self):
        url = reverse('shop-list')
        response = self.client.get(url, {'open': '0'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

        response = self.client.get(url, {'open': '1'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 0)  # Assuming no shop is currently open

# from django.urls import reverse
# from rest_framework.test import APITestCase
#
# from .models import City, Street, Shop
#
#
# class CityListTests(APITestCase):
#     def test_list_cities(self):
#         City.objects.create(name="New York")
#         City.objects.create(name="London")
#
#         url = reverse('city-list')
#         response = self.client.get(url)
#
#         self.assertEqual(response.status_code, 200)
#         self.assertEqual(len(response.data), 2)
#         self.assertEqual(response.data[0]['name'], 'New York')
#         self.assertEqual(response.data[1]['name'], 'London')
#
#
# class StreetListTests(APITestCase):
#     def test_list_streets_for_city(self):
#         city = City.objects.create(name="Paris")
#         Street.objects.create(name="Champs-Élysées", city=city)
#         Street.objects.create(name="Rue de Rivoli", city=city)
#
#         url = reverse('street-list', kwargs={'city_id': city.id})
#         response = self.client.get(url)
#
#         self.assertEqual(response.status_code, 200)
#         self.assertEqual(len(response.data), 2)
#         self.assertEqual(response.data[0]['name'], 'Champs-Élysées')
#         self.assertEqual(response.data[1]['name'], 'Rue de Rivoli')
#
#
# class ShopListTests(APITestCase):
#     def setUp(self):
#         self.city = City.objects.create(name="Berlin")
#         self.street = Street.objects.create(name="Friedrichstraße", city=self.city)
#         self.shop1 = Shop.objects.create(name="Shop 1", city=self.city, street=self.street, opening_time="09:00", closing_time="18:00")
#         self.shop2 = Shop.objects.create(name="Shop 2", city=self.city, street=self.street, opening_time="10:00", closing_time="20:00")
#
#     def test_list_shops_filtered_by_city(self):
#         url = reverse('shop-list') + '?city=Berlin'
#         response = self.client.get(url)
#
#         self.assertEqual(response.status_code, 200)
#         self.assertEqual(len(response.data), 2)
#
#     def test_list_shops_filtered_by_street(self):
#         url = reverse('shop-list') + '?street=Friedrichstraße'
#         response = self.client.get(url)
#
#         self.assertEqual(response.status_code, 200)
#         self.assertEqual(len(response.data), 2)
#
#     def test_list_shops_filtered_by_open_status(self):
#         # Assuming current time is within opening hours of Shop 1
#         url = reverse('shop-list') + '?open=1'
#         response = self.client.get(url)
#
#         self.assertEqual(response.status_code, 200)
#         self.assertEqual(len(response.data), 1)
#         self.assertEqual(response.data[0]['name'], 'Shop 1')
