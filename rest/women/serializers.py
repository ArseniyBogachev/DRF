from django.utils import timezone
from rest_framework import serializers
from .models import *


class WomenSerializer(serializers.ModelSerializer):
    # user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    name = serializers.CharField(max_length=100, required=False)
    lastname = serializers.CharField(max_length=100, required=False)
    age = serializers.IntegerField(required=False)

    class Meta:
        model = Women
        fields = "__all__"


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = WomenUser
        fields = "__all__"

