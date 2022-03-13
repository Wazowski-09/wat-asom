import BlynkLib
import time

# Initialize Blynk
blynk = BlynkLib.Blynk('GQNVXrn_3gXzL1F1Ca-efx9Dr_Alklmo')

# Register Virtual Pins
@blynk.VIRTUAL_WRITE(1)
def my_write_handler(value):
    print('Current V1 value: {}'.format(value))
    blynk.virtual_write(2, format(value[0]))

#@blynk.VIRTUAL_READ(2)
#def my_read_handler():
#    # this widget will show some time in seconds..
#    blynk.virtual_write(2, x)
    
@blynk.VIRTUAL_WRITE(3)
def my_write_handler(value):
    print('Current V3 value: {}'.format(value))

while True:
    blynk.run()
