#Módulo utilizado para encender las luces exteriores cinco minutos después de detectar oscuridad.

#Librerías utilizadas
#De la librería gpiozero importar los elementos de sensor de luz y led.
#De la librería signal importar pause para eventos desincronizados.
#De la librería time importar los módulos para obtener métricas de tiempo.
from gpiozero import LightSensor, LED
from signal import pause
from time import sleep, localtime, strftime

#Declaración de pines y variables para el sensor de luz y el led.
sensor = LightSensor(18)
led = LED(17)

#Función para calcular la hora en que se prenden y se apagan las luces exteriores.
def calcular_hora():
	hora_luces = strftime("%I:%M:%S %p", localtime())
	return hora_luces

#Función para encender las luces exteriores después de cinco minutos.
def encender():
	sleep(5)
	print("Las luces exteriores se han encendido a las ", calcular_hora())
	led.on()

#Función para apagar las luces inmediatamente después de detectar luz.
def apagar():
	print("Las luces exteriores se han apagado a las ", calcular_hora())
	led.off()

#Funciones que va a realizar el sensor de luz dependiendo del estado.
sensor.when_dark = encender
sensor.when_light = apagar

pause()
