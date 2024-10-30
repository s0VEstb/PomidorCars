from rest_framework.test import APITestCase
from django.urls import reverse
from cars.models import CarModel
from cars.serializers import CarSerializer


class BooksAPITestCase(APITestCase):
    def test_get(self):
        car_1 = CarModel.objects.create(name='car_1', price=1000)
        car_2 = CarModel.objects.create(name='car_2', price=2000)
        url = reverse('car_list')
        responce = self.client.get(url)
        serializer_data = CarSerializer([car_1, car_2], many=True).data
        self.assertEquals(serializer_data, responce.data)
        self.assertEquals(responce.status_code, 200)
