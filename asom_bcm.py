import RPi.GPIO as GPIO
import time
import socket
from gpiozero import CPUTemperature
import BlynkLib

time.sleep(60)

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
    x1 = format(value[0])
    if x1 == '1':
        GPIO.output(RELAIS_1_GPIO, GPIO.HIGH)
        blynk.virtual_write(16, 0)
        blynk.virtual_write(15, 255)
        print("relay1-work")
    else:
        GPIO.output(RELAIS_1_GPIO, GPIO.LOW)
        blynk.virtual_write(15, 0)
        blynk.virtual_write(16, 255)
        print("relay1-not-work")

@blynk.VIRTUAL_WRITE(2)
def my_write_handler(value):
    print('Current V2 value: {}'.format(value[0]))
    x2 = format(value[0])
    if str(x2) == "1":
        GPIO.output(RELAIS_2_GPIO, GPIO.HIGH)
        blynk.virtual_write(12, 0)
        blynk.virtual_write(11, 255)
        print("relay1-work")
    else:
        GPIO.output(RELAIS_2_GPIO, GPIO.LOW)
        blynk.virtual_write(11, 0)
        blynk.virtual_write(12, 255)
        print("relay1-not-work")

@blynk.VIRTUAL_WRITE(3)
def my_write_handler(value):
    print('Current V3 value: {}'.format(value[0]))
    x3 = format(value[0])
    if x3 is "1":
        GPIO.output(RELAIS_3_GPIO, GPIO.HIGH)
        blynk.virtual_write(14, 0)
        blynk.virtual_write(13, 255)
        print("relay1-work")
    else:
        GPIO.output(RELAIS_3_GPIO, GPIO.LOW)
        blynk.virtual_write(13, 0)
        blynk.virtual_write(14, 255)
        print("relay1-not-work")
        
tmr_start_time = time.time()
while True:
    blynk.run()
    
    t = time.time()
    if t - tmr_start_time > 5:
        testIP = "8.8.8.8"
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect((testIP, 0))
        ipaddr = s.getsockname()[0]
        host = socket.gethostname()
        cpu = CPUTemperature()
        blynk.virtual_write(5, str(ipaddr))
        blynk.virtual_write(6, str(host))
        blynk.virtual_write(7, "Temp CPU : " + str(cpu.temperature) + " C")
        blynk.virtual_write(8, cpu.temperature)
        print(cpu.temperature)
        print ("IP:", ipaddr, " Host:", host)
        tmr_start_time += 5
