import os
import subprocess as sp
from pruba import speak
from infoUsuario import leer_usuario
rutas = {
    'google': r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    'visual': r"C:\Users\guzma\AppData\Local\Programs\Microsoft VS Code\Code.exe",
    'git': r"C:\Users\guzma\AppData\Local\GitHubDesktop\app-3.5.3\GitHubDesktop.exe"
}
def abrir_camara(idioma):
    os.startfile("microsoft.windows.camara:")
    speak("Camara")
def abrir_google(idioma):
    os.startfile(rutas['google'])
    speak("Google")
def abrir_spotify(idioma):
    os.startfile("spotify:")
    speak("Spotify")
def abrir_visual(idioma):
    os.startfile(rutas['visual'])
    speak("Visual Code")
def abrir_comandos(idioma):
    os.system('start cmd')
    speak("CMD")
def abrir_ip(idioma):
    sp.run("ipconfig", shell=True)
def abrir_git(idioma):
    os.startfile(rutas['git'])
    speak("Git Hub")
def abrir_tareas(idioma):
    os.system('taskmgr')
    speak("Administrador de Tareas")
def cerrar_programa(idioma):
    speak("Que Programa Desea Cerrar?")
    nombre = leer_usuario(idioma).lower()
    try:
        sp.run(f"taskkill /F /IM {nombre}.exe", shell=True)
        speak(f"{nombre} cerrado")
    except Exception as e:
        speak("No pude cerrar el programa")
        print("Error:", e)
