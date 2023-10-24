import dht 

from machine import Pin 

 

d = dht.DHT11(Pin(22)) 

d.measure() 

a = d.temperature() # np. 23 (°C) 

b = d.humidity()    # np. 41 (% RH) 

print(a) 

print(b) 