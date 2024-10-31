from rest_framework.test import APITestCase
from django.urls import reverse
from cars.models import CarModel, MarkModel
from cars.serializers import CarSerializer


class BooksAPITestCase(APITestCase):
    def setUp(self):
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


    
