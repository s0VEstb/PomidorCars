from rest_framework import serializers
from . import models

class ABitInfoAboutUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ABitInfoAboutUs
        fields = ['id', 'title', 'text']


class SlogansNumbersSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.SlogansNumbers
        fields = ['id', 'our_slogan', 'number', 'text']


class SlogansTextSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.SlogansText
        fields = ['id', 'our_slogan', 'title', 'description']


class OurSloganSerializer(serializers.ModelSerializer):
    slogans_numbers = SlogansNumbersSerializer(many=True, read_only=True)
    slogans_text = SlogansTextSerializer(many=True, read_only=True)

    class Meta:
        model = models.OurSlogan
        fields = ['id', 'title', 'slogans_numbers', 'slogans_text']


class ProudRewardsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ProudRewards
        fields = ['id', 'image', 'description', 'our_proud']


class OurProudSerializer(serializers.ModelSerializer):
    proud_rewards = ProudRewardsSerializer(many=True, read_only=True)

    class Meta:
        model = models.OurProud
        fields = ['id', 'title', 'proud_rewards']


class CompanyAuthorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CompanyAuthors
        fields = ['id', 'name', 'company_authors_info', 'url_1', 'url_2']


class CompanyAuthorsInfoSerializer(serializers.ModelSerializer):
    company_authors = CompanyAuthorsSerializer(many=True, read_only=True)

    class Meta:
        model = models.CompanyAuthorsInfo
        fields = ['id', 'image', 'description', 'company_authors']


