import RPi.GPIO as GPIO
import BlynkLib
import time

BLYNK_AUTH = 'eYCqFwdwVKD81qKjL_8Lr0pM3vHQsMdc'
blynk = BlynkLib.Blynk(BLYNK_AUTH)

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

@blynk.on("connected")
def blynk_connected():
    print("Updating values from the server...")
    blynk.sync_virtual(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12,
                       13, 14, 15, 16, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36)
    print("status OK")

@blynk.on("V1")
def v1_write_handler(value):
    #print('Current slider value: {}'.format(value[0]))
    x1 = format(value[0])
    if x1 == "1":
        GPIO.output(RELAIS_1_GPIO, GPIO.HIGH)
        print("relay1-work")
    else:
        GPIO.output(RELAIS_1_GPIO, GPIO.LOW)
        print("relay1-not-work")


@blynk.on("V2")
def v2_write_handler(value):
    #print('Current slider value: {}'.format(value[0]))
    x2 = format(value[0])
    if x2 == "1":
        GPIO.output(RELAIS_2_GPIO, GPIO.HIGH)
        blynk.virtual_write(34, 255)
        blynk.virtual_write(35, 0)
        print("relay2-work")
    else:
        GPIO.output(RELAIS_2_GPIO, GPIO.LOW)
        blynk.virtual_write(34, 0)
        blynk.virtual_write(35, 255)
        print("relay2-not-work")


@blynk.on("V3")
def v3_write_handler(value):
    #print('Current slider value: {}'.format(value[0]))
    x3 = format(value[0])
    if x3 == "1":
        GPIO.output(RELAIS_3_GPIO, GPIO.HIGH)
        blynk.virtual_write(24, 255)
        blynk.virtual_write(25, 0)
        print("relay1-work")
    else:
        GPIO.output(RELAIS_3_GPIO, GPIO.LOW)
        blynk.virtual_write(24, 0)
        blynk.virtual_write(25, 255)
        print("relay3-not-work")

while True:
    blynk.run() 
