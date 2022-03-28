import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BCM)

pushpin = 25 # set input push button pin
pushpin1 = 8

GPIO.setup(pushpin, GPIO.IN, pull_up_down=GPIO.PUD_UP) # with pull up resistor
GPIO.setup(pushpin1, GPIO.IN, pull_up_down=GPIO.PUD_UP)

while True:
    print(GPIO.input(pushpin)," ",GPIO.input(pushpin1))
    sleep(0.2)
