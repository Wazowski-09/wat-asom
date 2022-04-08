import RPi.GPIO as GPIO
from time import sleep
import time

#relay
GPIO.setmode(GPIO.BCM)

RELAIS_1_GPIO = 23
RELAIS_2_GPIO = 16
RELAIS_3_GPIO = 12
RELAIS_4_GPIO = 7

inG = 8
inR = 24

t = 0

GPIO.setwarnings(False)
GPIO.setup(RELAIS_1_GPIO, GPIO.OUT)
GPIO.setup(RELAIS_2_GPIO, GPIO.OUT) # GPIO Assign mode
GPIO.setup(RELAIS_3_GPIO, GPIO.OUT)
GPIO.setup(RELAIS_4_GPIO, GPIO.OUT)

 # set input push button pin
GPIO.setup(inG, GPIO.IN, pull_up_down=GPIO.PUD_UP) # with pull up resistor
GPIO.setup(inR, GPIO.IN, pull_up_down=GPIO.PUD_UP)

#blynk
#WRITE_EVENT_PRINT_MSG = "[WRITE_VIRTUAL_PIN_EVENT] Pin: V{} Value: '{}'"
#WRITE_EVENT_PRINT_MSG = "Pin: V{} Value: '{}'"

def timer():
    global timer_a
    timer_a = time.time()
    global t
    t = 1

def close_pump():
    GPIO.output(RELAIS_1_GPIO, GPIO.LOW)
    GPIO.output(RELAIS_2_GPIO, GPIO.LOW) # out
    GPIO.output(RELAIS_3_GPIO, GPIO.LOW)
    GPIO.output(RELAIS_4_GPIO, GPIO.HIGH)

def open_pump():
    GPIO.output(RELAIS_1_GPIO, GPIO.HIGH)
    GPIO.output(RELAIS_2_GPIO, GPIO.HIGH) # out
    GPIO.output(RELAIS_3_GPIO, GPIO.HIGH)
    GPIO.output(RELAIS_4_GPIO, GPIO.LOW)

while True:
    button_stateG = GPIO.input(inG)
    button_stateR = GPIO.input(inR)
    #print(button_stateG)
    #print(button_stateR)
    if button_stateG == 0 and button_stateR == 1:
      print("open")
      GPIO.output(RELAIS_1_GPIO, GPIO.HIGH)
      GPIO.output(RELAIS_2_GPIO, GPIO.HIGH) # out
      GPIO.output(RELAIS_3_GPIO, GPIO.HIGH)
      GPIO.output(RELAIS_4_GPIO, GPIO.LOW)
      timer()
    elif button_stateR == 0 and button_stateG == 1:
      print("close")
      GPIO.output(RELAIS_1_GPIO, GPIO.LOW)
      GPIO.output(RELAIS_2_GPIO, GPIO.LOW) # out
      GPIO.output(RELAIS_3_GPIO, GPIO.LOW)
      GPIO.output(RELAIS_4_GPIO, GPIO.HIGH)
      t = 0
    if(t == 1):
      if time.time() - timer_a > 300:
        timer_a = time.time()
        close_pump()
        t = 0
        print("close")
