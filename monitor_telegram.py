import requests
import time
import urllib3

# Deshabilitar advertencias de SSL
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Configuración del bot de Telegram
TELEGRAM_TOKEN = "7570090378:AAH7GRgm6G7FAoIEyyQtwtku3qcrsmyWrBA"  # Tu token de Telegram
TELEGRAM_CHAT_ID = "7504800067"  # Tu chat_id
TELEGRAM_API_URL = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"

# URL de la página de tu universidad
URL_UNIVERSIDAD = "https://siu.uni.edu.ni/notasuni/Login.aspx"

# Función para enviar un mensaje a Telegram
def enviar_mensaje_telegram(mensaje):
    params = {
        "chat_id": TELEGRAM_CHAT_ID,
        "text": mensaje,
    }
    response = requests.post(TELEGRAM_API_URL, params=params)
    if response.status_code == 200:
        print("Mensaje enviado a Telegram.")
    else:
        print("Error al enviar el mensaje a Telegram.")

# Función para verificar el estado de la página
def verificar_pagina():
    try:
        response = requests.get(URL_UNIVERSIDAD, verify=False)  # Deshabilitar verificación SSL
        if response.status_code == 200:
            enviar_mensaje_telegram("¡La página está activa! Ve a matricularte.")
            return True
        else:
            print(f"Página no disponible. Código de estado: {response.status_code}")
            return False
    except requests.exceptions.RequestException as e:
        print(f"Error al conectar: {e}")
        return False

# Bucle para verificar cada 15 minutos
while True:
    if verificar_pagina():
        # Si la página está activa, espera 15 minutos antes de volver a verificar
        time.sleep(900)  # 900 segundos = 15 minutos
    else:
        # Si la página no está activa, espera 5 minutos antes de volver a verificar
        time.sleep(300)  # 300 segundos = 5 minutos
