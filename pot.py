from machine import Pin, ADC	 
from time import sleep 

pot = ADC(Pin(4)) 
pot.atten(ADC.ATTN_11DB)       #Full range: 3.3v 

while True: 
      print(pot.read()/4095*3.3) 
      sleep(0.1) 