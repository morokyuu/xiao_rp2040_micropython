from machine import ADC, Pin
import time

#xiao rp2040
adc = ADC(Pin(27))

while True:
    ad = adc.read_u16()
    print(ad)
    time.sleep_ms(10)