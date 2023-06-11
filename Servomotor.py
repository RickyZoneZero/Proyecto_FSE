#Módulo encargado de poner o quitar el seguro de la puerta a través de un servomotor.

#Librerías utilizadas
#De la librería gpiozero importar el elemento de servomotor.
#De la librería time importar la interrupción de tiempo sleep.
from gpiozero import  Servo
from time import sleep

#Declaración de pin y variable para el servomotor.
servo = Servo(12)

try:
    while True:
        print("Setting to min...")
        servo.min()
        sleep(1)

        print("Setting to mid...")
        servo.mid()
        sleep(1)

        print("Setting to max...")
        servo.max()
        sleep(1)
        
except KeyboardInterrupt:
    print("Exiting program")
