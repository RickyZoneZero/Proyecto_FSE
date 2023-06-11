import speech_recognition as sr
#import pywhatkit as kt
import os

#create sound
file = "out.wav"
r = sr.Recognizer()
print('Grabando audio.')
os.system("arecord -d 3 --format=S16_LE --rate=16000 --file-type=wav " + file)


# play sound
print('playing sound using native player.')
os.system("aplay " + file)

#

def convert_wav_to_text(wav_file):
    r = sr.Recognizer()
    
    # Cargar el archivo de audio
    with sr.AudioFile(wav_file) as source:
        audio = r.record(source)  # Leer el audio desde el archivo
    
    try:
        text = r.recognize_google(audio, language="es-MX")
        return text
    except sr.UnknownValueError:
        print("No se pudo reconocer el audio")
    except sr.RequestError as e:
        print("Error en la solicitud al servicio de reconocimiento de voz: {0}".format(e))

# Ruta del archivo .wav a convertir
wav_file = "out.wav"

# Convertir el archivo a texto
texto = convert_wav_to_text(wav_file)
print(texto)

try:
    if texto == "información del clima":
        print("Se llegó")
        #kt.search(texto)
        
except:
    print("No te entendí")
