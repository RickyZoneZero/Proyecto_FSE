#!/usr/bin/env python3
import whisper
import time
from gpiozero import LED
import sounddevice as sd
from scipy.io.wavfile import write
import wavio as wv
 
         
def main ():
    inicio = time.time()
    record_audio ()
 
    model = whisper.load_model("tiny")
    result = model.transcribe("audio1.wav")
    words = result["text"].split()
 
    for word in words:
        word = word.replace(',', '').replace('.', '').lower()
        if word == 'enciende' or 'encender':
            encender()
            break
        if word == 'parpadea' or 'parpadear':
            parpadear()
            break     
    fin = time.time()
    print(fin-inicio)
 
def encender ():
    LED(17).on()
 
def parpadear ():
    light = LED(17)
    while True:
        light.on()
        sleep(1)
        light.off()
        sleep(1)
 
def record_audio ():
    # Sampling frequency
    freq = 44100
    # Recording duration
    duration = 5
    # Start recorder with the given values
    # of duration and sample frequency
    recording = sd.rec(int(duration * freq),
                    samplerate=freq, channels=2)
    # Record audio for the given number of seconds
    sd.wait()
    # This will convert the NumPy array to an audio
    # file with the given sampling frequency
    write("audio0.wav", freq, recording)
    # Convert the NumPy array to audio file
    wv.write("audio1.wav", recording, freq, sampwidth=2)
         
main ()
 
 
#dar permisos para usar la GPIO
#sudo apt install python3-gpiozero
#sudo usermode -aG gpio <username>
 
#Instalar whisper
#pip install git+https://github.com/openai/whisper.git
#sudo apt update &amp;&amp; sudo apt install ffmpeg
