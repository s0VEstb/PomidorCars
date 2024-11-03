from rest_framework.test import APITestCase
from django.urls import reverse
from cars.models import CarModel, MarkModel
from cars.serializers import CarSerializer
from django.contrib.auth.models import User
import json


class CarsAPITestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create(username='test_user')
        self.mark1 = MarkModel.objects.create(name='KIA')
        self.mark2 = MarkModel.objects.create(name='TOYOTA')

        self.car_1 = CarModel.objects.create(name='KIA K5', price=1000, mark=self.mark1)
        self.car_2 = CarModel.objects.create(name='TOYOTA', price=2000, mark=self.mark2)
        self.car_3 = CarModel.objects.create(name='OPTIMA', price=1000, mark=self.mark1)

    def test_get(self):
        url = reverse('car_list')
        response = self.client.get(url)
        serializer_data = CarSerializer([self.car_1, self.car_2, self.car_3], many=True).data
        self.assertEquals(serializer_data, response.data)
        self.assertEquals(response.status_code, 200)

    def test_filter(self):
        url = reverse('car_list')
        response = self.client.get(url, data={'price': 1000})
        serializer_data = CarSerializer([self.car_1, self.car_3], many=True).data
        self.assertEquals(serializer_data, response.data)
        self.assertEquals(response.status_code, 200)

    def test_search(self):
        url = reverse('car_list')
        response = self.client.get(url, data={'search': 'KIA'})
        serializer_data = CarSerializer([self.car_1, self.car_3], many=True).data
        self.assertEquals(serializer_data, response.data)
        self.assertEquals(response.status_code, 200)

    def test_ordering(self):
        url = reverse('car_list')
        response = self.client.get(url, data={'ordering': 'mark__name'})
        serializer_data = CarSerializer([self.car_1, self.car_3, self.car_2], many=True).data
        self.assertEquals(serializer_data, response.data)
        self.assertEquals(response.status_code, 200)

    def test_create(self):
        self.assertEquals(3, CarModel.objects.all().count())
        url = reverse('car_list')
        data = {
            "name": "KIA K3",
            "price": 1000,
            "mark": self.mark1.id
        }
        self.client.force_login(self.user)
        response = self.client.post(url, data=data, format='json')
        self.assertEquals(response.status_code, 201)
        self.assertEquals(4, CarModel.objects.all().count())

    def test_put(self):
        url = reverse('car_detail', args=(self.car_1.id,))
        data = {
            "name": "KIA K5",
            "price": 9000,
            "mark": self.mark1.id
        }
        self.client.force_login(self.user)
        response = self.client.put(url, data=data, format='json')
        self.assertEquals(response.status_code, 200)
        self.car_1.refresh_from_db()
        self.assertEquals(9000, self.car_1.price)

    def test_delete(self):
        url = reverse('car_detail', args=(self.car_1.id,))
        self.client.force_login(self.user)
        response = self.client.delete(url)
        self.assertEquals(response.status_code, 204)
        self.assertEquals(CarModel.objects.all().count(), 2)
    
    def test_detail(self):
        url = reverse('car_detail', args=(self.car_1.id,))
        response = self.client.get(url)
        serializer_data = CarSerializer(self.car_1).data
        self.assertEquals(serializer_data, response.data)
        self.assertEquals(response.status_code, 200)