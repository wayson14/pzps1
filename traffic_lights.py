from machine import Pin 
import time 

led_red = Pin(4, Pin.OUT) # GPIO4 układu - odpowiada gniazdu D4 płytki   
led_yellow = Pin(5, Pin.OUT)
led_green = Pin(21, Pin.OUT)

while True:
    led_red.on()
    time.sleep(2)
    led_red.off()

    led_yellow.on()
    time.sleep(2)
    led_yellow.off()

    led_green.on()
    time.sleep(2)
    led_green.off()

