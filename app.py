import speech_recognition as sr
recognizer = sr.Recognizer()
mic = sr.Microphone()

if (__name__ == "__main__"):
    with mic as source:
        print("Di Algo...")
        audio = recognizer.listen(source)
        
    try:
        text = recognizer.recognize_google(audio, language = "es-ES")
        print(f'Texto Reconocido:{text}')
    except sr.UnknownValueError:
        print ("Error, no se reconoce la voz")
    except sr.RequestError as err:
        print("Error en la Solicitud de reconocimiento: ")
    