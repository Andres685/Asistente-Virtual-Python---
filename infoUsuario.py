import speech_recognition as sr
from random import choice
from utils import default_text, texto_defecto
from pruba import speak
def reconocer_idioma():
    speak("Selecciona un Idioma para la Conversacion")
    idioma = input("ES - EN: ")
    idioma = idioma.lower()
    if idioma == 'es':
        speak("Te hablare en español")
        return idioma
    elif idioma=='en':
        speak("im going to speak you in english")
        return idioma
    else:
        speak("Seleccione un idioma Valido")
        exit()
def leer_usuario(idioma):
    r = sr.Recognizer()
    with sr.Microphone() as source:
            print("Escuchando..." if idioma =='es' else "Listening...")
            r.pause_threshold = 1
            audio = r.listen(source)
            if idioma == 'es':
                try:
                    print("Reconociendo....")
                    query = r.recognize_google(audio, language = "es-ES")
                    if not 'salir'in query and not 'alto' in query:
                        print(query)
                        speak(choice(texto_defecto))
                    else:
                        speak("Tenga un buendia Señor")
                        exit()
                except Exception:
                    speak("No He Podido Entender, podria Repetirlo?")
                    query = 'None'
                return query
            else:
                try:
                    print("Recognizing....")
                    query = r.recognize_google(audio, language = "en-EN")
                    if not 'exit' in query and not 'stop' in query:
                        print(query)
                        speak(choice(default_text))
                    else:
                        speak("Have a nice day Sr")
                        exit()
                except Exception:
                    speak("i cant understand your peticion, shall you repeat please?")
                    query = 'None'
                return query