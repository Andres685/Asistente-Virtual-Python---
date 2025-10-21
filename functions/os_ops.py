import os
import subprocess as sp
from pruba import speak
rutas = {
    'google': r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    'visual': r"C:\Users\guzma\AppData\Local\Programs\Microsoft VS Code\Code.exe",
    'git': r"C:\Users\guzma\AppData\Local\GitHubDesktop\app-3.5.3\GitHubDesktop.exe"
}
def abrir_camara():
    os.startfile("microsoft.windows.camara:")
    speak("Camara")
def abrir_google():
    os.startfile(rutas['google'])
    speak("Google")
def abrir_spotify():
    os.startfile("spotify:")
    speak("Spotify")
def abrir_visual():
    os.startfile(rutas['visual'])
    speak("Visual Code")
def abrir_comandos():
    os.system('start cmd')
    speak("CMD")
def abrir_ip():
    sp.run("ipconfig", shell=True)
def abrir_git():
    os.startfile(rutas['git'])
    speak("Git Hub")
def abrir_tareas():
    os.system('taskmgr')
    speak("Administrador de Tareas")