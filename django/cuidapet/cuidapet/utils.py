import requests
import logging

api_switch={
    'nationalities': 'https://restcountries.com/v3.1/all',
    'dogs':'https://api.thedogapi.com/v1/breeds',
    'cats':'https://api.thecatapi.com/v1/breeds',
}

def get_constants(const):
    result=requests.get(api_switch.get(const))
    if result.status_code==200:
        return result.json()
    else:
        logging.error("Error en la conexión con la API de "+str(const))
        return None
    
