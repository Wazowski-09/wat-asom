import blynklib
from datetime import datetime

BLYNK_AUTH = 'GQNVXrn_3gXzL1F1Ca-efx9Dr_Alklmo'
blynk = blynklib.Blynk(BLYNK_AUTH)


@blynk.handle_event("connect")
def connect_handler():
    blynk.internal("rtc", "sync")
    print("RTC sync request was sent")


@blynk.handle_event('internal_rtc')
def rtc_handler(rtc_data_list):
    hr_rtc_value = datetime.utcfromtimestamp(int(rtc_data_list[0])).strftime('%Y-%m-%d %H:%M:%S')
    rtctime.var = rtc_data_list[0]
    humantime.var = hr_rtc_value
    print('Raw RTC value from server: {}'.format(rtc_data_list[0]))
    print('Human readable RTC value: {}'.format(hr_rtc_value))

###########################################################
# infinite loop that waits for event
###########################################################
while True:
    blynk.run()
    rtime = rtctime.var
    htime = humantime.var
    if rtctime.var - rtime > 20:
        rtime = rtctime.var
        print('20 seconds')
