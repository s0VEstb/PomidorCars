from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('cars/', views.CarListAPIView.as_view(), name='car_list'),
    path('cars/<int:id>/', views.CarDetailAPIView.as_view(), name='car_detail'),
]