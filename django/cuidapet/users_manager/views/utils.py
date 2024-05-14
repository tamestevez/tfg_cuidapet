import logging

from rest_framework import status
from rest_framework.response import Response
from users_manager.models import BaseUser


def check_user(user):
    if not user:
        logging.error("Ususario no encontrado")
        return Response(
            {"detail": "Ususario no encontrado"},
            status=status.HTTP_404_NOT_FOUND,
        )
    if not BaseUser.objects.filter(email=user.email).first():
        logging.error("Ususario no encontrado")
        return Response(
            {"detail": "Ususario no encontrado"},
            status=status.HTTP_404_NOT_FOUND,
        )
    return None
