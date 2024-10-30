from django.shortcuts import render
from .models import CarModel, MarkModel
from .serializers import CarSerializer
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter



class CarListAPIView(generics.ListCreateAPIView):
    serializer_class = CarSerializer
    queryset = CarModel.objects.all()
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['name', 'price', 'mark']
    search_fields = ['name', 'price', 'mark__name']
    ordering_fields = ['name', 'price', 'mark__name']



class CarDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CarSerializer
    queryset = CarModel.objects.all()
    lookup_field = 'id'