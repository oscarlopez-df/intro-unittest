"""
Módulo que contiene funciones para realizar llamadas a servicios web externos.

Contiene las siguientes funciones:
    - get_response: Obtiene datos de un servicio web.

"""

import requests
from datetime import datetime
from mathfuncs.sum import sum


def get_response():
    """
    Obtiene datos de un servicio web.

    Returns:
        dict: Datos obtenidos del servicio web.

    """

    response = requests.get("https://example.com/api/data")
    if response.status_code == 200:
        return response.json()
    else:
        return None


def sum_and_post(a, b):
    """
    Takes two numbers, sums them and posts the result to a web service.

    Args:
        a (float): First number.
        b (float): Second number.

    Returns:
        dict: Response from the web service.

    """
    result = sum(a, b)
    response = requests.post("https://example.com/api/data", json={"result": result})
    return response.json()


def post_current_datetime():
    """
    Posts the current datetime to a web service.

    Returns:
        dict: Response from the web service.

    """
    now_ts = datetime.now().timestamp()
    response = requests.post("https://example.com/api/data", json={"datetime": now_ts})
    response_json = response.json()
    response_json["datetime"] = now_ts
    return response_json