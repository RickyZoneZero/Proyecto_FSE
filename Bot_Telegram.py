#Módulo utilizado para la gestión y comunicación con el bot de Telegram.

#Librerías utilzadas
#Importar la librería telebot para utilizar el bot de Telegram.
#Importar la librería os para poder ejecutar órdenes en el sistema operativo.
#De la librería time importar la interrupción de tiempo sleep.
#De la librería gpiozero importar los elementos de sensor ultrasónico y led.
import telebot
import os
from time import sleep
from gpiozero import LED, DistanceSensor



#Declaración de pines y variables para el sensor ultrasónico y el led.
#Declaración de variables para el token del bot y creación del bot.
#Declaración de variable chat_id correspondiente al ID del grupo de Telegram. 
#Declaración de variable con el mensaje que se mandará a los usuarios del grupo.
led = LED(26)
sensor = DistanceSensor(echo=18, trigger=17, max_distance=4, threshold_distance=0.2)
API_TOKEN = '6228306806:AAHc7u7cwyvBLWW35KZ-1RBabSVOAa7XYoY'
bot = telebot.TeleBot(API_TOKEN)
chat_id = -1001518392897
mensaje = "Llamen al 911 ¡Alguien ha entrado a la casa!"
alarm_sound = "alarma.wav"


#Función encargada de dar la bienvenida y mostrar las opciones disponibles.
@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.reply_to(message, """\
Hola, soy el Bot de Telegram. Intenta utilizar los siguientes comandos:
/start
/help
/enciende_alarma
/apaga_alarma
/activar_camara
/desactivar_camara\
""")

#Función encargada de activar la alarma.
@bot.message_handler(commands=['enciende_alarma'])
def alarma_on(message):
    bot.reply_to(message, """\
alarma encendida\
""")
    global on
    on = True
    while on:
        print(sensor.distance)
        if sensor.distance < 0.2:
            led.blink()
            bot.send_message(chat_id = chat_id, text = mensaje)
            bot.reply_to(message, """\
¡peligro! alguien acaba de entrar a tu propiedad.\
""")
            os.system("aplay "+ alarm_sound)
            
#Función encargada de desactivar la alarma.
@bot.message_handler(commands=['apaga_alarma'])
def alarma_off(message):
    bot.reply_to(message, """\
alarma apagada\
""")
    global on
    on = False
    led.off()

#Función encargada de mandar URL del servidor web de la cámara.
@bot.message_handler(commands=['activar_camara'])
def activate_camera(message):
    bot.reply_to(message, """\
Cámara activada. Puedes monitorear en el siguiente enlace:
http://192.168.137.78:8081 \
""")
    os.system("sudo systemctl restart motion")
    
#Función encargada de cerrar URL del servidor web de la cámara.
@bot.message_handler(commands=['desactivar_camara'])
def activate_camera(message):
    bot.reply_to(message, """\
Cámara desactivada.\
""")
    os.system("sudo systemctl stop motion")
    
bot.infinity_polling()


