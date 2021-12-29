import BlynkLib

# Initialize Blynk
blynk = BlynkLib.Blynk('eYCqFwdwVKD81qKjL_8Lr0pM3vHQsMdc')

# Register Virtual Pins
@blynk.VIRTUAL_WRITE(1)
def my_write_handler(value):
    print('Current V1 value: {}'.format(value))

@blynk.VIRTUAL_READ(2)
def my_read_handler():
    # this widget will show some time in seconds..
    blynk.virtual_write(2, int(time.time()))

while True:
    blynk.run()
