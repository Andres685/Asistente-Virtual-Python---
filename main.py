from functions.os_ops import abrir_camara, abrir_comandos, abrir_google, abrir_spotify, abrir_visual, abrir_ip, abrir_git, abrir_tareas
from pruba import bienvenida_Usuario
from infoUsuario import leer_usuario, reconocer_idioma

OPEN_VISUAL = ("abrir visual", "open visual", "visual studio", "vscode", "abrir vscode", "abre visual")
OPEN_SPOTIFY = ("abrir spotify", "open spotify", "spotify", "abre spotify")
OPEN_CMD = ("abrir cmd", "abrir comandos", "abre comandos", "comandos")
OPEN_CHROME = ("abrir chrome", "abrir google", "google", "abre google", "abre chrome")
OPEN_GITHUB = ("abrir git", "git", "abre git", "open git")
OPEN_TASK = ("abrir tareas", "tareas", "abre tareas", "open task", "open task manager", "abre administrador")

COMMANDS = {
    "visual": OPEN_VISUAL,
    "spotify": OPEN_SPOTIFY,
    "comandos": OPEN_CMD,
    "google": OPEN_CHROME,
    "git" : OPEN_GITHUB,
    "tareas": OPEN_TASK
}

ACTIONS = {
    "visual": abrir_visual,
    "spotify": abrir_spotify,
    "comandos": abrir_comandos,
    "google": abrir_google,
    "git": abrir_git,
    "tareas": abrir_tareas
}
# ejecutar la acción correspondiente
idioma = reconocer_idioma()
bienvenida_Usuario(idioma)
while True:
    query = leer_usuario(idioma)
    q = query.lower().strip()
    for key, phrases in COMMANDS.items():
        if (any(p in q for p in phrases)):
            ACTIONS[key]()
