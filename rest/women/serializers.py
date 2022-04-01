from django.utils import timezone
from rest_framework import serializers
from .models import *


class WomenSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Women
        fields = "__all__"

