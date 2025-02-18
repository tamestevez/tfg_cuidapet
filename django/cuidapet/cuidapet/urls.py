"""
URL configuration for cuidapet project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)
from users_manager import views as user_views
from pet_manager import views as pet_views

api_urls = {
    "user": (user_views.UserViewSet, "UserProfile"),
    "user/change-password": (
        user_views.ChangePasswordViewSet,
        "ChangePasswordProfile",
    ),

}

router = routers.DefaultRouter()

for url, (viewset, model) in api_urls.items():
    router.register(url, viewset, model)

urlpatterns = [
    path("api/", include(router.urls)),
    path("admin/", admin.site.urls),
    path(
        "api/two-factor-generate/", user_views.GenerateTwoFactorView.as_view()
    ),
    path("api/login/", user_views.LoginView.as_view()),
    path("api/logout/", user_views.LogoutView.as_view()),
    path(
        "api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"
    ),
    path(
        "api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"
    ),
    path("api/token/verify/", TokenVerifyView.as_view(), name="token_verify"),
    path("api/forgot-password/", user_views.ForgotPasswordView.as_view()),
    path("api/reset-password/", user_views.ResetPasswordView.as_view()),
]
