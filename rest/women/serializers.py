from django.utils import timezone
from rest_framework import serializers
from .models import *


class WomenSerializer(serializers.ModelSerializer):
    # user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    name = serializers.CharField(max_length=100, required=False)
    lastname = serializers.CharField(max_length=100, required=False)
    age = serializers.IntegerField(required=False)
    # women_like = serializers.PrimaryKeyRelatedField(many=True, queryset=WomenRelation.objects.filter(like=True))
    like_true = serializers.SerializerMethodField()

    class Meta:
        model = Women
        fields = ('id', 'name', 'lastname', 'age', 'del_obj', 'display', 'like_true')

    def get_like_true(self, instance):
        return WomenRelation.objects.filter(women=instance, like=True).values_list('user_id', flat=True)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = WomenUser
        fields = "__all__"

class WomenRelationSerializer(serializers.ModelSerializer):
    # women_like = WomenSerializer(many=True, read_only=True)
    class Meta:
        model = WomenRelation
        fields = "__all__"


class BlackListJWTSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlackListJWT
        fields = "__all__"


# class RefreshJWTSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = RefreshJWT
#         fields = "__all__"
