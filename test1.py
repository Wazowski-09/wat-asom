import RPi.GPIO as GPIO
import BlynkLib
import time

RELAIS_1_GPIO = 2
RELAIS_2_GPIO = 3
RELAIS_3_GPIO = 4

GPIO.setwarnings(False)

GPIO.setmode(GPIO.BCM)

GPIO.setup(RELAIS_1_GPIO, GPIO.OUT)
GPIO.setup(RELAIS_2_GPIO, GPIO.OUT)
GPIO.setup(RELAIS_3_GPIO, GPIO.OUT)

GPIO.output(RELAIS_1_GPIO, GPIO.LOW)
GPIO.output(RELAIS_2_GPIO, GPIO.LOW)
GPIO.output(RELAIS_3_GPIO, GPIO.LOW)

BLYNK_AUTH = 'vx2PmALZocpxYT76UWYegqcfLnqDnFCH'

# Initialize Blynk
blynk = BlynkLib.Blynk(BLYNK_AUTH)

# Register Virtual Pins
@blynk.VIRTUAL_WRITE(1)
def my_write_handler(value):
  print('Current V1 value: {}'.format(value[0]))
  if int(format(value[0])) == 1:
    GPIO.output(RELAIS_2_GPIO, GPIO.HIGH)
    blynk.virtual_write(16, 0)
    blynk.virtual_write(15, 255)
    print("relay1-work")
  else:
    GPIO.output(RELAIS_2_GPIO, GPIO.LOW)
    blynk.virtual_write(15, 0)
    blynk.virtual_write(16, 255)
    print("relay1-not-work")

try:
    while True:
        blynk.run()

except KeyboardInterrupt:
    sys.exit(0)
    GPIO.cleanup()
