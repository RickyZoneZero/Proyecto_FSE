#Módulo utilizado para mostrar el estado de la puerta con display 7 segmentos y leds de colores.



#Librerías utilizadas

#De la librería gpiozero importar los elementos de display 7 segmentos y led.

#De la librería time importar la interrupción de tiempo sleep.

from gpiozero import LEDCharDisplay, LED

from time import sleep



#Declaración de pines y variables para el display siete segmentos y los leds.

display = LEDCharDisplay(0,5,6,13,19,26,20,active_high = False)

red = LED(14)

green =  LED(15)



#Función encargada de mostrar cada letra en el display.

def display_name(name):

	for char in name:

		display.value = char 

		sleep(1)

	display.off()



#Función encargada de generar y mostrar el mensaje "OPEN".

def mostrar_mensaje_abierto():

        print("Abriendo")

        display_name("OPEN")

        red.off()

        green.on()

	

#Función encargada de generar y mostrar el mensaje "CLOSE"

def mostrar_mensaje_cerrado():

        print("Cerrando")

        display_name("CLOSE")

        red.on()

        green.off()

