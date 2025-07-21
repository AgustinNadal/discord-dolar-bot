import requests
import os

API_BASE = os.getenv("API_URL")

def obtener_dolar_blue():
    try:
        res = requests.get(f"{API_BASE}/blue")
        data = res.json()
        return f"💵 Dólar Blue: Compra ${data['compra']} | Venta ${data['venta']}"
    except Exception as e:
        return f"Error al obtener el dólar blue: {e}"
    

def obtener_dolar_oficial():
    try:
        res = requests.get(f"{API_BASE}/oficial")
        data = res.json()
        return f"💵 Dólar Oficial: Compra ${data['compra']} | Venta ${data['venta']}"
    except Exception as e:
        return f"Error al obtener el dólar oficial: {e}"