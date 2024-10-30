from rest_framework import serializers
from .models import CarModel, MarkModel


class MarkSerializer(serializers.ModelSerializer):
    class Meta:
        model = MarkModel
        fields = ('name',)


class CarSerializer(serializers.ModelSerializer):
    mark = MarkSerializer()

    class Meta:
        model = CarModel
        fields = ('id', 'name', 'price', 'mark')
