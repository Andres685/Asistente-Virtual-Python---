import pyttsx3
from decouple import config
from datetime import datetime
import time
USERNAME = config('USUARIO')
BOTNAME = config('BOT_NAME')

#Metodo para Hablar
def speak(texto):
    print(f"[HABLANDO]: {texto}")
    motor = pyttsx3.init('sapi5') 
    voices = motor.getProperty('voices')
    motor.setProperty('voice', voices[1].id)
    motor.setProperty('rate', 220)  # Ajusta la velocidad de palabras x minuto
    motor.setProperty('volume', 1.0) #Ajustar el Volumen
    motor.say(texto)
    motor.runAndWait()
    motor.stop()
    del motor  # ← borra la variable
    
#Metodo para Saludar segun tiempo Horario
def bienvenida_Usuario(idioma):
    hora = datetime.now().hour
    if idioma == "es":
        if(6<=hora<12):
            speak(f"Buenos dias {USERNAME}")
        elif(12<=hora<16):
            speak(f"Buenas Tardes {USERNAME}")
        elif(16<=hora<19):
            speak(f"Buenas Noches {USERNAME}")
        time.sleep(0.5)
        speak(f"Soy {BOTNAME} tu Asistente Virtual. Como puedo Ayudarte?")
    else:
        if(6<=hora<12):
            speak(f"Good Morning {USERNAME}")
        elif(12<=hora<16):
            speak(f"Good Afternon {USERNAME}")
        elif(16<=hora<19):
            speak(f"Good Night {USERNAME}")
        time.sleep(0.5)
        speak(f"I am {BOTNAME} your virtual assistant, how can i help you??")
  
if (__name__ == "__main__"):  
    bienvenida_Usuario('es')