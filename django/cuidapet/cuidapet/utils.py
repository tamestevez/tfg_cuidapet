import logging

import requests

api_switch = {
    "nationalities": "https://restcountries.com/v3.1/all",
    "dogs": "https://api.thedogapi.com/v1/breeds",
    "cats": "https://api.thecatapi.com/v1/breeds",
    "towns": (
        "https://public.opendatasoft.com/api/explore/v2.1/catalog/datasets/georef-spain-provincia/records?order_by=acom_code&limit=52"
    ),
}


def get_constants(const):
    try:
        result = requests.get(api_switch.get(const))
        if result.status_code == 200:
            return result.json()
        else:
            logging.error("Error en la conexión con la API de " + str(const))
            return None
    except Exception as e:
        logging.error("Error: " + str(e))
        return None
