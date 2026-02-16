from machine import Pin
import time

coila=Pin(18,Pin.OUT)
coilb=Pin(19,Pin.OUT)
coilc=Pin(22,Pin.OUT)
coild=Pin(23,Pin.OUT)
bleh = [[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]]

while True:
     for i in bleh:
         coila.value(i[0])
         coilb.value(i[1])
         coilc.value(i[2])
         coild.value(i[3])
         time.sleep_ms(5)
