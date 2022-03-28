import blynklib
import RPi.GPIO as GPIO
from time import sleep
import time

BLYNK_AUTH = 'GQNVXrn_3gXzL1F1Ca-efx9Dr_Alklmo'

# initialize Blynk
blynk = blynklib.Blynk(BLYNK_AUTH)

#relay
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

#blynk
#WRITE_EVENT_PRINT_MSG = "[WRITE_VIRTUAL_PIN_EVENT] Pin: V{} Value: '{}'"
#WRITE_EVENT_PRINT_MSG = "Pin: V{} Value: '{}'"

@blynk.handle_event('write V4')
def write_virtual_pin_handler(pin, value):
    GPIO.output(RELAIS_2_GPIO, GPIO.HIGH) # out
    GPIO.output(RELAIS_3_GPIO, GPIO.HIGH)
    #print(WRITE_EVENT_PRINT_MSG.format(pin, value))
    print("Pin: V{} Value: '{}'".format(pin, value))

while True:
    button_stateG = GPIO.input(inG)
    button_stateR = GPIO.input(inR)
    #print(button_stateG)
    #print(button_stateR)
    if button_stateG == 0 and button_stateR == 1:
      print("open")
      GPIO.output(RELAIS_2_GPIO, GPIO.HIGH) # out
      GPIO.output(RELAIS_3_GPIO, GPIO.HIGH)
      GPIO.output(RELAIS_4_GPIO, GPIO.HIGH)
    elif button_stateR == 0 and button_stateG == 1:
      print("close")
      GPIO.output(RELAIS_2_GPIO, GPIO.LOW) # out
      GPIO.output(RELAIS_3_GPIO, GPIO.LOW)
      GPIO.output(RELAIS_4_GPIO, GPIO.LOW)
    blynk.run()
