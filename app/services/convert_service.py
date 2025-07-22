import requests
from fastapi import HTTPException

# 1. Función que consulta la API externa
def exchange_rate(from_currency: str, to_currency: str):
    url = f"https://api.exchangerate.host/convert?from={from_currency}&to={to_currency}&amount=1"

    response = requests.get(url)

    if response.status_code != 200:
        raise HTTPException(status_code=500, detail="Error al obtener la tasa de cambio")

    data = response.json()
    if not data.get("success", False):
        raise HTTPException(status_code=500, detail="Respuesta inválida de la API")
    
    return data["info"]["rate"]

# 2. Función para realizar el 
def convert_currency(amount: float,rate: float):
    return round(amount * rate, 4)