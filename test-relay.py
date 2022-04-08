import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM) # GPIO Numbers instead of board numbers

RELAIS_1_GPIO = 23
RELAIS_2_GPIO = 16
RELAIS_3_GPIO = 12
RELAIS_4_GPIO = 7

GPIO.setwarnings(False)
GPIO.setup(RELAIS_1_GPIO, GPIO.OUT)
GPIO.setup(RELAIS_2_GPIO, GPIO.OUT) # GPIO Assign mode
GPIO.setup(RELAIS_3_GPIO, GPIO.OUT)
GPIO.setup(RELAIS_4_GPIO, GPIO.OUT)

while True:
#    GPIO.output(RELAIS_1_GPIO, GPIO.LOW)
#    GPIO.output(RELAIS_2_GPIO, GPIO.LOW) # out
#    GPIO.output(RELAIS_3_GPIO, GPIO.LOW)
#    GPIO.output(RELAIS_4_GPIO, GPIO.LOW)
#    time.sleep(1)
    GPIO.output(RELAIS_1_GPIO, GPIO.HIGH)
#    GPIO.output(RELAIS_2_GPIO, GPIO.HIGH)
#    GPIO.output(RELAIS_3_GPIO, GPIO.HIGH)
#    GPIO.output(RELAIS_4_GPIO, GPIO.HIGH)
#    time.sleep(1)


#import RPi.GPIO as GPIO
#import time

#GPIO.setmode(GPIO.BCM) # Broadcom pin-numbering scheme

#RELAIS_1_GPIO = 16

#GPIO.setwarnings(False)
#GPIO.setup(RELAIS_1_GPIO, GPIO.OUT) # GPIO Assign mode

# Initial state for LEDs:
#print("Testing RF out, Press CTRL+C to exit")
#while True:
#    try:
#         print("set GIOP high")
#         GPIO.output(RELAIS_1_GPIO, GPIO.LOW) # out
#         time.sleep(1)
#         GPIO.output(RELAIS_1_GPIO, GPIO.HIGH)
#         time.sleep(1)             
#    except KeyboardInterrupt: # If CTRL+C is pressed, exit cleanly:
#       print("Keyboard interrupt")
#
#    except:
#       print("some error") 
#
#    finally:
#       print("clean up") 
#       GPIO.cleanup() # cleanup all GPIO 
