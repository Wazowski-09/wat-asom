import blynklib
import time

BLYNK_AUTH = 'GQNVXrn_3gXzL1F1Ca-efx9Dr_Alklmo'

# initialize Blynk
blynk = blynklib.Blynk(BLYNK_AUTH)

WRITE_EVENT_PRINT_MSG = "[WRITE_VIRTUAL_PIN_EVENT] Pin: V{} Value: '{}'"

t = 0

def timer():
    global timer_a
    timer_a = time.time()
    global t
    t = 1

def close_pump():
    blynk.virtual_write(10, 0)

def open_pump():
    blynk.virtual_write(10, 1)
    
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
      global t  
      t = 0
    elif x == "1":
      #print(WRITE_EVENT_PRINT_MSG.format(pin, value))
      timer()

while True:
    blynk.run()
    if(t == 1):
      if time.time() - timer_a > 10:
        timer_a = time.time()
        close_pump()
        t = 0
        print("close")
