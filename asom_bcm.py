import RPi.GPIO as GPIO
import time

import BlynkLib

# Initialize Blynk
blynk = BlynkLib.Blynk('eYCqFwdwVKD81qKjL_8Lr0pM3vHQsMdc')

# Register Virtual Pins
# @blynk.VIRTUAL_WRITE(1)
# def my_write_handler(value):
#     print('Current V1 value: {}'.format(value))

# @blynk.VIRTUAL_READ(2)
# def my_read_handler():
#     # this widget will show some time in seconds..
#     blynk.virtual_write(2, int(time.time()))

GPIO.setmode(GPIO.BCM) # GPIO Numbers instead of board numbers
GPIO.setwarnings(False)

RELAIS_1_GPIO = 2
RELAIS_2_GPIO = 3
RELAIS_3_GPIO = 4

GPIO.setup(RELAIS_1_GPIO, GPIO.OUT, initial = GPIO.LOW) # GPIO Assign mode
GPIO.setup(RELAIS_2_GPIO, GPIO.OUT, initial = GPIO.LOW) # GPIO Assign mode
GPIO.setup(RELAIS_3_GPIO, GPIO.OUT, initial = GPIO.LOW) # GPIO Assign mode

# GPIO.setup(RELAIS_1_GPIO, GPIO.OUT, initial = GPIO.HIGH) # GPIO Assign mode
# GPIO.setup(RELAIS_2_GPIO, GPIO.OUT, initial = GPIO.HIGH) # GPIO Assign mode
# GPIO.setup(RELAIS_3_GPIO, GPIO.OUT, initial = GPIO.HIGH) # GPIO Assign mode

# @blynk.on("connected")
# def blynk_connected():
#     print("Updating values from the server...")
#     blynk.sync_virtual(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12,
#                        13, 14, 15, 16, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36)
#     print("status OK")

@blynk.VIRTUAL_WRITE(1)
def my_write_handler(value):
    print('Current V1 value: {}'.format(value[0]))
    x1 = format(value)
    if x1 == "1":
        GPIO.output(RELAIS_1_GPIO, GPIO.HIGH)
        print("relay1-work")
    else:
        GPIO.output(RELAIS_1_GPIO, GPIO.LOW)
        print("relay1-not-work")

@blynk.VIRTUAL_WRITE(2)
def my_write_handler(value):
    print('Current V2 value: {}'.format(value))
    x2 = format(value)
    if x2 == "1":
        GPIO.output(RELAIS_2_GPIO, GPIO.HIGH)
        print("relay1-work")
    else:
        GPIO.output(RELAIS_2_GPIO, GPIO.LOW)
        print("relay1-not-work")

@blynk.VIRTUAL_WRITE(3)
def my_write_handler(value):
    print('Current V3 value: {}'.format(value))
    x3 = format(value)
    if x3 == "1":
        GPIO.output(RELAIS_3_GPIO, GPIO.HIGH)
        print("relay1-work")
    else:
        GPIO.output(RELAIS_3_GPIO, GPIO.LOW)
        print("relay1-not-work")

while True:
    blynk.run() 
