#Write your code here to run the stepper motor without using any loop
from machine import Pin
import time
coila=Pin(18,Pin.OUT)
coilb=Pin(19,Pin.OUT)
coilc=Pin(22,Pin.OUT)
coild=Pin(23,Pin.OUT)

while True:
     coila.value(1)
     coilb.value(0)
     coilc.value(0)
     coild.value(0)
     time.sleep(1)

     coila.value(0)
     coilb.value(1)
     coilc.value(0)
     coild.value(0)
     time.sleep(1)

     coila.value(0)
     coilb.value(0)
     coilc.value(1)
     coild.value(0)
     time.sleep(1)

     coila.value(0)
     coilb.value(0)
     coilc.value(0)
     coild.value(1)
     time.sleep(1)
time.sleep(0.5)
