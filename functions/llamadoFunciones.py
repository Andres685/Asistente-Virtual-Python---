from functions.os_ops import cerrar_programa, abrir_comandos, abrir_google, abrir_spotify, abrir_visual, abrir_ip, abrir_git, abrir_tareas
from functions.online_ops import encontrar_ip, consejo_aleatorio, play_on_yotube

OPEN_VISUAL = ("abrir visual", "open visual", "visual studio", "vscode", "abrir vscode", "abre visual")
OPEN_SPOTIFY = ("abrir spotify", "open spotify", "spotify", "abre spotify")
OPEN_CMD = ("abrir cmd", "abrir comandos", "abre comandos", "comandos")
OPEN_CHROME = ("abrir chrome", "abrir google", "google", "abre google", "abre chrome")
OPEN_GITHUB = ("abrir git", "git", "abre git", "open git")
OPEN_TASK = ("abrir tareas", "tareas", "abre tareas", "open task", "open task manager", "abre administrador")
CONSULTAR_IP = ("ip", "mi ip", "cual es mi ip", "dame mi ip", "Give me my ip, show me my ip")
CONSEJO = ("dame un consejo", "consejo", "give me a ", "necesito un consejo")
YOUTUBE = ("reproduce en youtube", "youtube", "video en youtube")
CERRAR = ("cerrar", "close")

COMMANDS = {
    "visual": OPEN_VISUAL,
    "spotify": OPEN_SPOTIFY,
    "comandos": OPEN_CMD,
    "google": OPEN_CHROME,
    "git" : OPEN_GITHUB,
    "tareas": OPEN_TASK,
    "ip": CONSULTAR_IP,
    "consejo" : CONSEJO,
    "youtube": YOUTUBE,
    "cerrar":CERRAR
}

ACTIONS = {
    "visual": abrir_visual,
    "spotify": abrir_spotify,
    "comandos": abrir_comandos,
    "google": abrir_google,
    "git": abrir_git,
    "tareas": abrir_tareas,
    "ip": encontrar_ip,
    "consejo": consejo_aleatorio,
    "youtube" : play_on_yotube,
    "cerrar" : cerrar_programa
}