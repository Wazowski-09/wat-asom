import time, os, sys
import json

import BlynkLib
import BlynkEdgent
import RPi.GPIO as GPIO

# -- Configuration --------------------
BLYNK_FIRMWARE_VERSION = "0.1.0"

BLYNK_TEMPLATE_ID = "TMPLaiUHrgaT"
BLYNK_DEVICE_NAME = "Quickstart Template"
BLYNK_AUTH_TOKEN = "p6nnRTzcz6dQPYwZ0nZ1d4ppE6ts4ahC"

blynk = BlynkLib.Blynk(BLYNK_AUTH_TOKEN)

GPIO.setmode(GPIO.BCM) # GPIO Numbers instead of board numbers
GPIO.setwarnings(False)

RELAIS_1_GPIO = 2
RELAIS_2_GPIO = 3
RELAIS_3_GPIO = 4

try:
    with open("config.json") as jsonFile:
        config = json.load(jsonFile)
    needToSave = False
except:
    config = BlynkEdgent.provision(BLYNK_DEVICE_NAME, BLYNK_TEMPLATE_ID, BLYNK_FIRMWARE_VERSION)
    needToSave = True

def reset_config():
    if os.path.exists("config.json"):
        print("Resetting configuration")
        os.remove("config.json")
        # Restart
        os.execv(sys.executable, ['python3'] + sys.argv)
        sys.exit(0)

@blynk.on("connected")
def blynk_connected(ping):
    print('Blynk ready. Ping:', ping, 'ms')
    if needToSave:
        with open('config.json', 'w') as jsonFile:
            json.dump(config, jsonFile)
        print("Configuration is saved")

@blynk.on("disconnected")
def blynk_disconnected():
    print('Blynk disconnected')

GPIO.setup(RELAIS_1_GPIO, GPIO.OUT, initial = GPIO.LOW) # GPIO Assign mode
GPIO.setup(RELAIS_2_GPIO, GPIO.OUT, initial = GPIO.LOW) # GPIO Assign mode
GPIO.setup(RELAIS_3_GPIO, GPIO.OUT, initial = GPIO.LOW) # GPIO Assign mode

# GPIO.setup(RELAIS_1_GPIO, GPIO.OUT, initial = GPIO.HIGH) # GPIO Assign mode
# GPIO.setup(RELAIS_2_GPIO, GPIO.OUT, initial = GPIO.HIGH) # GPIO Assign mode
# GPIO.setup(RELAIS_3_GPIO, GPIO.OUT, initial = GPIO.HIGH) # GPIO Assign mode

def button_callback(channel):
    if GPIO.input(channel) == 1:
        return

    print("Hold button for 10 seconds to reset configuration")
    start_time = time.time()
    # Wait for the button up
    while (GPIO.input(channel) == 0 and
           time.time() - start_time <= 10):
        time.sleep(0.1)
    if time.time() - start_time > 10:
        reset_config()

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
        print("relay2-work")
    else:
        GPIO.output(RELAIS_2_GPIO, GPIO.LOW)
        print("relay2-not-work")


@blynk.on("V3")
def v3_write_handler(value):
    #print('Current slider value: {}'.format(value[0]))
    x3 = format(value[0])
    if x3 == "1":
        GPIO.output(RELAIS_3_GPIO, GPIO.HIGH)
        print("relay1-work")
    else:
        GPIO.output(RELAIS_3_GPIO, GPIO.LOW)
        print("relay3-not-work")

while True:
    blynk.run()
