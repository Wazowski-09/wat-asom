import blynklib
import time

BLYNK_AUTH = 'GQNVXrn_3gXzL1F1Ca-efx9Dr_Alklmo'

# initialize Blynk
blynk = blynklib.Blynk(BLYNK_AUTH)

WRITE_EVENT_PRINT_MSG = "[WRITE_VIRTUAL_PIN_EVENT] Pin: V{} Value: '{}'"


# register handler for virtual pin V4 write event
@blynk.handle_event('write V4')
def write_virtual_pin_handler(pin, value):
    print(WRITE_EVENT_PRINT_MSG.format(pin, value))
    
@blynk.handle_event('write V10')
def write_virtual_pin_handler(pin, value):
    x = format(value[0])
    print("Pin: V{} Value: '{}'".format(pin, value))
    print(format(value[0]))
    if x == "0":
      #print(WRITE_EVENT_PRINT_MSG.format(pin, value))
      print("close")
    elif x == "1":
      #print(WRITE_EVENT_PRINT_MSG.format(pin, value))
      print("open")
      timer_a = time.time()
      print("start")
      if time.time() - timer_a > 10:
        timer_a = time.time()
        blynk.virtual_write(10, 0)
        print("close")
        

while True:
    blynk.run()
