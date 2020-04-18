#!/usr/bin/env python3
########################################################################
# Filename    : Relay.py
# Description : Control Rele y Motor con Pulsador 
# Author      : Antonio2709
# modification: 19/04/2020
########################################################################
import RPi.GPIO as GPIO
import time

relayPin = 11     # define el relayPin
buttonPin = 12    # define el buttonPin
debounceTime = 50

def setup():    
    GPIO.setmode(GPIO.BOARD)       
    GPIO.setup(relayPin, GPIO.OUT)   # poner relayPin en OUTPUT modo
    GPIO.setup(buttonPin, GPIO.IN)   # poner buttonPin en INTPUT modo

def loop():
    relayState = False
    lastChangeTime = round(time.time()*1000)
    buttonState = GPIO.HIGH
    lastButtonState = GPIO.HIGH
    reading = GPIO.HIGH
    while True:
        reading = GPIO.input(buttonPin)     
        if reading != lastButtonState :
            lastChangeTime = round(time.time()*1000)
        if ((round(time.time()*1000) - lastChangeTime) > debounceTime):
            if reading != buttonState :
                buttonState = reading;
                if buttonState == GPIO.LOW:
                    print("Pulsador presionado!")
                    relayState = not relayState
                    if relayState:
                        print("Encender rele ...")
                        
                    else :
                        print("Apagar rele ... ")
                else :
                    print("Pulsador liberado!")
                    print('')
        GPIO.output(relayPin,relayState)
        lastButtonState = reading # lastButtonState almacenar el estado mas reciente
    
def destroy():
    GPIO.cleanup()                      

if __name__ == '__main__':     # Arrancar programa
    print ('Programa esta arrancado...')
    print ('Presionar contrl+C para finalizar el programa')
    setup()
    try:
        loop()
    except KeyboardInterrupt:   # Presionar contrl+C para finalizar el programa
        destroy()

