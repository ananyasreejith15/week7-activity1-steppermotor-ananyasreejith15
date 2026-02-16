#Write your code here to run the stepper motor without using any loop
from machine import Pin
import time

led1 = Pin(12, Pin.OUT)
led2 = Pin(14, Pin.OUT)
led3 = Pin(26, Pin.OUT)
led4 = Pin(33, Pin.OUT)

t = 0.1

while True:
    led1.value(1) 
    led2.value(0) 
    led3.value(0) 
    led4.value(0) 
    time.sleep(t)
    
    led1.value(0)
    led2.value(1)
    led3.value(0)
    led4.value(0)
    time.sleep(t)
    
    led1.value(0)
    led2.value(0)
    led3.value(1)
    led4.value(0)
    time.sleep(t)
    
    led1.value(0)
    led2.value(0)
    led3.value(0)
    led4.value(1)
    time.sleep(t)
    
    
