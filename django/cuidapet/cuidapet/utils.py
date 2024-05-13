import logging

import requests
from rest_framework import status
from rest_framework.response import Response

api_switch = {
    "nationalities": "https://restcountries.com/v3.1/all",
    "dogs": "https://api.thedogapi.com/v1/breeds",
    "cats": "https://api.thecatapi.com/v1/breeds",
    "towns": (
        "https://public.opendatasoft.com/api/explore/v2.1/catalog/datasets/georef-spain-provincia/records?order_by=acom_code&limit=52"
    ),
}


def get_constants(const):
    result = requests.get(api_switch.get(const))
    if result.status_code == 200:
        return result.json()
    else:
        logging.error("Error en la conexión con la API de " + str(const))
        return None


def check_user(user):
    if not user:
        logging.error("Ususario no encontrado")
        return Response(
            {"detail": "Ususario no encontrado"},
            status=status.HTTP_400_BAD_REQUEST,
        )
    if not BaseUser.objects.filter(email=user.email).first():
        logging.error("Ususario no encontrado")
        return Response(
            {"detail": "Ususario no encontrado"},
            status=status.HTTP_400_BAD_REQUEST,
        )
    return None
