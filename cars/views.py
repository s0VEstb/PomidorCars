from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from SeniorPomidor import settings
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


class OauthAPIGithubView(APIView):
    def get(self, request):
        github_auth_url = (
            f"https://github.com/login/oauth/authorize?"
            f"client_id={settings.SOCIAL_GITHUB_KEY}&"
            f"redirect_uri={settings.SOCIAL_AUTH_REDIRECT_URI}&"
            f"scope=user"
        )
        return Response({"auth_url": github_auth_url})

