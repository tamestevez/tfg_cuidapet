from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from users_manager.models import BaseUser


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def get_token(cls, user: BaseUser):
        token = super().get_token(user)
        token["email"] = user.email
        token["name"] = user.name
        token["surnames"] = user.surnames
        token["role"] = user.role
        return token
