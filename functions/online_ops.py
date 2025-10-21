import requests
from decouple import config
from pruba import speak
from infoUsuario import leer_usuario
import pywhatkit as kit
from deep_translator import GoogleTranslator

def encontrar_ip(idioma):
    ip_result = requests.get('https://api64.ipify.org?format=json').json()
    ip = ip_result['ip']
    speak(f"Tu Ip es: {ip}") if idioma=='es' else speak(f"Your Ip is: {ip}")
    return ip_result["ip"]

def consejo_aleatorio(idioma):
    consejo_request = requests.get("https://api.adviceslip.com/advice").json()
    consejo = consejo_request['slip']['advice']
    if idioma == 'es':
        consejo = GoogleTranslator(source='en', target='es').translate(consejo)
        speak(f"Mi consejo es: {consejo}")
    else:
        speak(f"My advice is: {consejo}")
def play_on_yotube(idioma):
    if (idioma == 'es'):
        speak("Que Desea Ver en Yotube?")
    else:
        speak("What do you want to see on Yotube?")
    video = leer_usuario(idioma).lower()
    kit.playonyt(video)