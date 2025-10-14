from functions.os_ops import abrir_camara, abrir_comandos, abrir_google, abrir_spotify, abrir_visual, abrir_ip
from pruba import bienvenida_Usuario
from infoUsuario import leer_usuario, reconocer_idioma

OPEN_VISUAL = ("abrir visual", "open visual", "visual studio", "vscode", "abrir vscode", "abre visual")
OPEN_SPOTIFY = ("abrir spotify", "open spotify", "spotify", "abre spotify")
OPEN_CMD = ("abrir cmd", "abrir comandos", "abre comandos", "comandos")
OPEN_CHROME = ("abrir chrome", "abrir google", "google", "abre google", "abre chrome")

COMMANDS = {
    "visual": OPEN_VISUAL,
    "spotify": OPEN_SPOTIFY,
    "comandos": OPEN_CMD,
    "google": OPEN_CHROME
}

ACTIONS = {
    "visual": abrir_visual,
    "spotify": abrir_spotify,
    "comandos": abrir_comandos,
    "google": abrir_google
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
