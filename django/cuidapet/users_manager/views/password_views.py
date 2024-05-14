import logging

from django.contrib.auth import authenticate, login
from rest_framework import permissions, status, viewsets
from rest_framework.authentication import SessionAuthentication
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication
from users_manager.models import BaseUser

from .utils import check_user


class ChangePasswordViewSet(viewsets.ViewSet):
    authentication_classes = [SessionAuthentication, JWTAuthentication]
    permissions_classes = [permissions.IsAuthenticated]

    def update(self, request, pk=None):
        print("222")
        result = check_user(request.user)
        if result:
            return result

        print(request)

        user = BaseUser.objects.filter(pk=request.user.pk).first()
        if "old_password" not in request.data and not user.check_password(
            "old_password"
        ):
            logging.error("Contraseña incorrecta.")
            return Response(
                {"detail": "Contraseña incorrecta."},
                status=status.HTTP_400_BAD_REQUEST,
            )
        user = BaseUser.objects.get(pk=request.user.pk)
        user.set_password(request.data["new_password"])
        user.save()
        user = authenticate(
            emai=request.user.email, password=request.data["new_password"]
        )
        login(request, user)
        return Response(
            {"detail": "Contraseña cambiada."}, status=status.HTTP_200_OK
        )
