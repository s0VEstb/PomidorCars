from django.shortcuts import render
from . import serializers
from . import models
from rest_framework import generics


class ABitInfoAboutUsViewSet(generics.ListCreateAPIView):
    queryset = models.ABitInfoAboutUs.objects.all()
    serializer_class = serializers.ABitInfoAboutUsSerializer


class OurSlogan(generics.ListCreateAPIView):
    queryset = models.OurSlogan.objects.all()
    serializer_class = serializers.OurSloganSerializer


class OurProud(generics.ListCreateAPIView):
    queryset = models.OurProud.objects.all()
    serializer_class = serializers.OurProudSerializer


class CompanyAuthorsInfo(generics.ListCreateAPIView):
    queryset = models.CompanyAuthorsInfo.objects.all()
    serializer_class = serializers.CompanyAuthorsInfoSerializer



