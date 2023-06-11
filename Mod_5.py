from gpiozero import Motor
from time import sleep

motor = Motor(forward=4,backward=14)

def cerrar_puerta():
	motor.forward()

def abrir_puerta():
	motor.backward()
