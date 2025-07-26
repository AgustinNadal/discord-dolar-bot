import requests
import os

API_BASE = os.getenv("API_URL", "https://dolarapi.com/v1/dolares")

def informacion_comandos():
    return """
    **Comandos disponibles:**
    - `/dolarB`: Obtiene el valor del dólar blue.
    - `/dolar`: Obtiene el valor del dólar oficial.
    - `/valores`: Obtiene todos los valores de los tipos de dólar disponibles.
    """

def obtener_dolar_blue():
    try:
        res = requests.get(f"{API_BASE}/blue")
        data = res.json()
        return f"💸 Dólar Blue: Compra ${data['compra']} | Venta ${data['venta']}"
    except Exception as e:
        return f"⚠️ Error al obtener el dólar blue: {e}"

def obtener_dolar_oficial():
    try:
        res = requests.get(f"{API_BASE}/oficial")
        data = res.json()
        return f"💵 Dólar Oficial: Compra ${data['compra']} | Venta ${data['venta']}"
    except Exception as e:
        return f"⚠️ Error al obtener el dólar oficial: {e}"

def obtener_todos_los_valores():
    try:
        tipos = ["oficial", "blue", "tarjeta", "mep", "ccb", "cripto"]
        valores = []

        for tipo in tipos:
            url = f"{API_BASE}/{tipo}"
            res = requests.get(url)
            
            if res.status_code != 200:
                continue  # salteamos este tipo si la respuesta es mala

            try:
                data = res.json()
            except Exception:
                continue  # si no es JSON válido, salteamos

            nombre = data.get("nombre", tipo.capitalize())
            compra = data.get("compra", "-")
            venta = data.get("venta", "-")
            valores.append(f"💱 **{nombre}** → Compra: ${compra} | Venta: ${venta}")

        if not valores:
            return "⚠️ No se pudo obtener ningún valor de la API."

        return "\n".join(valores)

    except Exception as e:
        return f"⚠️ Error general: {e}"

