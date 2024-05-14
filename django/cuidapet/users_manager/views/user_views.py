import logging

from rest_framework import permissions, status, viewsets
from rest_framework.authentication import SessionAuthentication
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication
from users_manager.models import BaseUser
from users_manager.serializers import ListUserSerializer, ProfileUserSerializer

from .utils import check_user


class UserViewSet(viewsets.ViewSet):
    authentication_classes = [SessionAuthentication, JWTAuthentication]
    permissions_classes = [permissions.IsAuthenticated]

    def list(
        self,
        request,
    ):
        result = check_user(request.user)
        if result:
            return result
        if request.user.role == "ADMI":
            queryset = BaseUser.objects.all()
        elif request.user.role == "CLIN":
            queryset = BaseUser.objects.exclude(role="ADMI").exclude(
                role="CLIN"
            )
        else:
            return Response(
                {"detail": "Acceso denegado."},
                status=status.HTTP_401_UNAUTHORIZED,
            )
        return Response(
            ListUserSerializer(queryset, many=True).data,
            status=status.HTTP_200_OK,
        )

    def retrieve(selt, request, pk=None):
        result = check_user(request.user)
        if result:
            return result
        return Response(
            ProfileUserSerializer(
                BaseUser.objects.filter(pk=request.user.pk).first()
            ).data,
            status=status.HTTP_200_OK,
        )

    def create(self, request):
        result = check_user(request.user)
        if result:
            return result
        if request.user.role != "ADMI" and request.user.role != "CLIN":
            return Response(
                {"detail": "Acceso denegado."},
                status=status.HTTP_401_UNAUTHORIZED,
            )
        if (
            "email" in request.data
            and request.data["email"] != ""
            and request.data["email"] is not None
        ):
            if BaseUser.objects.filter(email=request.data["email"]).first():
                logging.error("Error: Ya existe usuario.")
                return Response(
                    {"detail": "Ya existe usuario."},
                    status=status.HTTP_400_BAD_REQUEST,
                )
        if "email" not in request.data or "phone_number" not in request.data:
            logging.error(
                "Error: Correo electrónico o número de teléfono incompletos."
            )
            return Response(
                {
                    "detail": "Correo electrónico o número de teléfono"
                    " incompletos."
                },
                status=status.HTTP_400_BAD_REQUEST,
            )
        BaseUser.objects.create(
            email=request.data["email"],
            name=request.data["name"],
            surnames=request.data["surnames"],
            phone_number=request.data["phone_number"],
            address=request.data["address"]
            if "address" in request.data
            else "",
            town=request.data["town"] if "town" in request.data else "13",
            role=request.data["role"]
            if request.user.role == "ADMI"
            else "PROP",
        ).save()
        return Response(
            {"detail": "Usuario creado correctamente"},
            status=status.HTTP_200_OK,
        )

    def update(self, request, pk=None):
        result = check_user(request.user)
        if result:
            return result
        if (
            "email" in request.data
            and request.data["email"] != ""
            and request.data["email"] is not None
        ):
            if BaseUser.objects.filter(email=request.data["email"]).exclude(
                pk=pk
            ):
                logging.error("Error: Ya existe usuario.")
                return Response(
                    {"detail": "Ya existe usuario."},
                    status=status.HTTP_400_BAD_REQUEST,
                )

        user = BaseUser.objects.filter(pk=pk).first()
        user.email = (
            request.data["email"] if "email" in request.data else user.email
        )
        user.name = (
            request.data["name"] if "name" in request.data else user.name
        )
        user.surnames = (
            request.data["surnames"]
            if "surnames" in request.data
            else user.surnames
        )
        user.phone_number = (
            request.data["phone_number"]
            if "phone_number" in request.data
            else user.phone_number
        )
        user.address = (
            request.data["address"]
            if "address" in request.data
            else user.address
        )
        user.town = (
            request.data["town"] if "town" in request.data else user.town
        )
        user.save()
        return Response(
            {"detail": "Datos de usuario actualizados."},
            status=status.HTTP_200_OK,
        )

    def delete(self, requets, pk=None):
        result = check_user(requets.user)
        if result:
            return result
        BaseUser.objects.filter(pk=pk).first().delete()
        return Response(
            {"detail": "Ususario eliminado correctamente."},
            status=status.HTTP_200_OK,
        )
