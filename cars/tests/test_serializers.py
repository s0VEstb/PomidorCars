from rest_framework.test import APITestCase
from django.urls import reverse
from cars.serializers import CarSerializer
from cars.models import CarModel


class CarSerializerTestCase(APITestCase):
    def test_ok(self):
        car_1 = CarModel.objects.create(name='car_1', price=1000)
        car_2 = CarModel.objects.create(name='car_2', price=2000)
        data = CarSerializer([car_1, car_2], many=True).data
        expected_data = [
            {
                'id': car_1.id,
                'name': 'car_1',
                'price': 1000,
                'mark': None
            },
            {
                'id': car_2.id,
                'name': 'car_2',
                'price': 2000,
                'mark': None
            }
        ]
        self.assertEqual(expected_data, data)

