import RPi.GPIO as GPIO
from time import sleep
import time
GPIO.setmode(GPIO.BCM)

RELAIS_2_GPIO = 16
RELAIS_3_GPIO = 12
RELAIS_4_GPIO = 7

inG = 8
inR = 25

GPIO.setwarnings(False)
GPIO.setup(RELAIS_2_GPIO, GPIO.OUT) # GPIO Assign mode
GPIO.setup(RELAIS_3_GPIO, GPIO.OUT)
GPIO.setup(RELAIS_4_GPIO, GPIO.OUT)

 # set input push button pin
GPIO.setup(inG, GPIO.IN, pull_up_down=GPIO.PUD_UP) # with pull up resistor
GPIO.setup(inR, GPIO.IN, pull_up_down=GPIO.PUD_UP)

while True:
    button_stateG = GPIO.input(inG)
    button_stateR = GPIO.input(inR)
    #print(button_stateG)
    #print(button_stateR)
    if button_stateG == 1:
      print("open")
      GPIO.output(RELAIS_2_GPIO, GPIO.LOW) # out
      GPIO.output(RELAIS_3_GPIO, GPIO.LOW)
      GPIO.output(RELAIS_4_GPIO, GPIO.LOW)
    elif button_stateR == 0:
      print("close")
      GPIO.output(RELAIS_2_GPIO, GPIO.HIGH) # out
      GPIO.output(RELAIS_3_GPIO, GPIO.HIGH)
      GPIO.output(RELAIS_4_GPIO, GPIO.HIGH)
