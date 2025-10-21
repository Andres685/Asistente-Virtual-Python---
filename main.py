from pruba import bienvenida_Usuario
from infoUsuario import leer_usuario, reconocer_idioma
from functions.llamadoFunciones import COMMANDS, ACTIONS
from pruba import speak

# ejecutar la acción correspondiente
idioma = reconocer_idioma()
bienvenida_Usuario(idioma)
while True:
    query = leer_usuario(idioma)
    q = query.lower().strip()
    for key, phrases in COMMANDS.items():
        if (any(p in q for p in phrases)):
            ACTIONS[key](idioma)