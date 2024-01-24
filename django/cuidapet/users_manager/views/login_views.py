import logging

import pyotp
from cuidapet.constants import OTP_ERROR, USER_ERROR
from django.contrib.auth import authenticate, login, logout
from rest_framework import permissions, status, views
from rest_framework.response import Response
from users_manager.models import BaseUser
from users_manager.serializers import CustomTokenObtainPairSerializer


class GenerateTwoFactorView(views.APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request):
        if (
            not request.data
            or "email" not in request.data
            or "password" not in request.data
        ):
            return Response(status=status.HTTP_400_BAD_REQUEST)
        user = authenticate(
            email=request.data.get("email"),
            password=request.data.get("password"),
        )
        if not user:
            logging.error("Generate Two Factor View Error: " + USER_ERROR)
            return Response(
                {"detail": USER_ERROR}, status=status.HTTP_401_UNAUTHORIZED
            )
        if not user.otp_generator_code:
            user.otp_generator_code = pyotp.random_base32()
            user.save()
            logging.info("Generate Two Factor View Info: OK")
            return Response(
                {
                    "otpauth_url": pyotp.totp.TOTP(
                        user.otp_generator_code
                    ).provisioning_uri(issuer_name="Cuidapet"),
                    "user_email": request.data.get("email"),
                },
                status=status.HTTP_200_OK,
            )
        logging.info("Generate Two Factor View Info: OK")
        return Response(
            {"user_email": request.data.get("email")},
            status=status.HTTP_200_OK,
        )


class LoginView(views.APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request):
        if (
            not request.data
            or "email" not in request.data
            or "otp_code" not in request.data
        ):
            return Response(status=status.HTTP_400_BAD_REQUEST)
        user = BaseUser.objects.filter(email=request.data["email"]).first()
        if not user:
            logging.error("Login View Error: " + USER_ERROR)
            return Response(
                {"detail": USER_ERROR}, status=status.HTTP_404_NOT_FOUND
            )
        if not pyotp.TOTP(user.otp_generator_code).verify(
            request.data["otp_code"]
        ):
            logging.error("Login View Error: " + OTP_ERROR)
            return Response(
                {"detail": OTP_ERROR}, status=status.HTTP_401_UNAUTHORIZED
            )
        if user.is_authenticated:
            login(request, user)
            token = CustomTokenObtainPairSerializer.get_token(user)
            logging.info("Usuario accediendo a la plataforma.")
            return Response(
                {
                    "refresh_token": str(token),
                    "access_token": str(token.access_token),
                },
                status=status.HTTP_200_OK,
            )
        logging.error(
            "Login View Error:" " Problema en el acceso a la plataforma."
        )
        return Response(status=status.HTTP_403_FORBIDDEN)


class LogoutView(views.APIView):
    permission_classes = (permissions.IsAuthenticated,)
    def post(self, request):
        logging.info("Usuario saliendo de la plataforma.")
        logout(request)
        return Response(
            {"detail": "El usuario ha cerrado sesión de forma correcta."},
            status=status.HTTP_200_OK,
        )
