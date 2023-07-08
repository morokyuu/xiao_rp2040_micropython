from machine import Pin, PWM
import time

#xiao rp2040
#color led
BLUE = 25
GREEN = 16
RED  = 17

pwm0 = PWM(Pin(BLUE), freq=50, duty_u16=32768)
green = Pin(GREEN, Pin.OUT)
red = Pin(RED, Pin.OUT)
green.on() # ON/OFF is reverted on xiao board. ON=led_off
red.off()  #

while True:
    for d in range(0,60000,3000):
        pwm0.duty_u16(d)
        time.sleep_ms(100)
        print(d)
    red.toggle()
    
    