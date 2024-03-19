from django.contrib.auth.models import User
from rest_framework import serializers
from api.models import Marketplace


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class MarketplaceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Marketplace
        fields = ['url', 'name', 'description']
