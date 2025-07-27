import requests
import os

API_BASE = os.getenv("API_URL", "https://dolarapi.com/v1/dolares")

API_COTIZACIONES = os.getenv("API_COTIZACIONES", "https://dolarapi.com/v1/cotizaciones")

valores_pesos = "TODOS LOS VALORES DE LOS TIPOS DE DÓLARES Y OTRAS MONEDAS ESTAN EXPRESADAS EN PESOS ARGENTINOS (ARS)."


def informacion_comandos():
    return """
    **Comandos disponibles:**
    - `/dolarB`: Obtiene el valor del dólar blue. \n
    - `/dolar`: Obtiene el valor del dólar oficial. \n
    - `/valores`: Obtiene todos los valores de los tipos de dólar disponibles.
    """

def obtener_dolar_oficial():
    try:
        res = requests.get(f"{API_BASE}/oficial")
        data = res.json()
        return f"💵 Dólar Oficial: Compra ${data['compra']} | Venta ${data['venta']}"
    except Exception as e:
        return f"⚠️ Error al obtener el dólar oficial: {e}"

def obtener_dolar_blue():
    try:
        res = requests.get(f"{API_BASE}/blue")
        data = res.json()
        return f"💸 Dólar Blue: Compra ${data['compra']} | Venta ${data['venta']}"
    except Exception as e:
        return f"⚠️ Error al obtener el dólar blue: {e}"

def obtener_dolar_bolsa():
    try:
        res = requests.get(f"{API_BASE}/bolsa")
        data = res.json()
        return f"💳 Dólar Bolsa: Compra ${data['compra']} | Venta ${data['venta']}"
    except Exception as e:
        return f"⚠️ Error al obtener el dólar bolsa: {e}"

def obtener_dolar_CCL():
    try:
        res = requests.get(f"{API_BASE}/contadoconliqui")
        data = res.json()
        return f"💳 Dólar CCL: Compra ${data['compra']} | Venta ${data['venta']}"
    except Exception as e:
        return f"⚠️ Error al obtener el dólar CCL: {e}"

def obtener_dolar_tarjeta():
    try:
        res = requests.get(f"{API_BASE}/tarjeta")
        data = res.json()
        return f"💳 Dólar Tarjeta: Compra ${data['compra']} | Venta ${data['venta']}"
    except Exception as e:
        return f"⚠️ Error al obtener el dólar tarjeta: {e}"

def obtener_dolar_mayorista():
    try:
        res = requests.get(f"{API_BASE}/mayorista")
        data = res.json()
        return f"💵 Dólar Mayorista: Compra ${data['compra']} | Venta ${data['venta']}"
    except Exception as e:
        return f"⚠️ Error al obtener el dólar mayorista: {e}"

def obtener_dolar_cripto():
    try:
        res = requests.get(f"{API_BASE}/cripto")
        data = res.json()
        return f"💱 Dólar Cripto: Compra ${data['compra']} | Venta ${data['venta']}"
    except Exception as e:
        return f"⚠️ Error al obtener el dólar cripto: {e}"

def obtener_todos_los_valores():
    try:
        res = requests.get(API_BASE)

        if res.status_code != 200:
            return "⚠️ Error al obtener los valores de los tipos de dólar."

        data = res.json()
        valores = []

        for tipo_dolar in data:
            nombre = tipo_dolar.get("nombre", "Dólar")
            compra = tipo_dolar.get("compra", "-")
            venta = tipo_dolar.get("venta", "-")
            valores.append(f"💱 **{nombre}** → Compra: ${compra} | Venta: ${venta}")
        
        if not valores:
            return "⚠️ No se encontraron valores disponibles."
        
        return "\n".join(valores) + "\n" + "\n" + valores_pesos
    
    except Exception as e:
        return f"⚠️ Error al obtener los valores: {e}"


def obtener_cotizaciones():
    try:
        res = requests.get(API_COTIZACIONES)

        if res.status_code != 200:
            return "⚠️ Error al obtener las cotizaciones."
        
        datos = res.json()
        valores = []

        for cotizacion in datos:
            nombre = cotizacion.get("nombre", "Moneda")
            compra = cotizacion.get("compra", "-")
            venta = cotizacion.get("venta", "-")
            valores.append(f"💱 **{nombre}** → Compra: ${compra} | Venta: ${venta}")
        
        if not valores:
            return "⚠️ No se encontraron cotizaciones disponibles."
        
        return "\n".join(valores) + "\n" + "\n" + valores_pesos
    
    except Exception as e:
        return f"⚠️ Error al obtener las cotizaciones: {e}"

