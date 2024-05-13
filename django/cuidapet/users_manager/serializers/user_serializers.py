from rest_framework import serializers
from users_manager.models import BaseUser


class ListUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = BaseUser
        fields = [
            "id",
            "email",
            "name",
            "surnames",
            "phone_number",
            "role",
        ]


class ProfileUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = BaseUser
        fields = [
            "id",
            "name",
            "surnames",
            "phone_number",
            "email",
            "address",
            "town",
            "role",
        ]
