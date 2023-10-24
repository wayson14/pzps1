from hcsr04 import HCSR04 
from time import sleep
from machine import Pin, SoftI2C, ADC, PWM
import dht 
import ssd1306 

sensor = HCSR04(trigger_pin=21, echo_pin=19, echo_timeout_us=10000) 
i2c = SoftI2C(scl=Pin(4), sda=Pin(18)) 

oled_width = 128 
oled_height = 64 
oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c) 

d = dht.DHT11(Pin(22)) 
pot = ADC(Pin(32)) 
pot.atten(ADC.ATTN_11DB)       

p12 = Pin(23) 
pwm12 = PWM(p12) 
pwm12.freq(100) 

oled.show() 

while True:
    oled.fill(0)
    sleep(1)
    distance = round(sensor.distance_cm(),2) 
    d.measure() 
    temperature = d.temperature() 
    volt = round(pot.read()/4095*3.3, 2)
    humidity = d.humidity()   

    dst = 'Dist: '+str(distance) + 'cm'
    temp = 'Temperature: '+str(temperature)+'C' 
    hum = 'Humidity: '+str(humidity)+'%'
    v = 'Voltage: '+str(volt)+'V'
    
    pwm12.duty(int(volt/3.3*1023)) 

    oled.text(dst, 0, 0) 
    oled.text(temp, 0, 10)
    oled.text(hum, 0, 20)
    oled.text(v, 0, 30)
    print('Distance:', distance, 'cm')
    oled.show()
    