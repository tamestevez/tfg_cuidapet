from rest_framework_simplejwt.views import TokenRefreshView
from users_manager.serializers import CustomTokenObtainPairSerializer


class CustomTokenObtainPairView(TokenRefreshView):
    serializer_class = CustomTokenObtainPairSerializer
