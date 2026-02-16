#with two lists
from machine import Pin
import time

coila=Pin(18,Pin.OUT)
coilb=Pin(19,Pin.OUT)
coilc=Pin(22,Pin.OUT)
coild=Pin(23,Pin.OUT)

bleh = [[1,1,0,0],[0,1,0,0],[0,1,1,0],[0,0,1,0],[0,0,1,1],[0,0,0,1],[1,0,0,1],[1,0,0,0]]
bleh_reverse = [[1,0,0,0],[1,0,0,1],[0,0,0,1],[0,0,1,1],[0,0,1,0],[0,1,1,0],[0,1,0,0],[1,1,0,0]]
while True:
    for x in range(500):
        for i in bleh:
            coila.value(i[0])
            coilb.value(i[1])
            coilc.value(i[2])
            coild.value(i[3])
            time.sleep_ms(3)
            
    for x in range(500):
        for i in bleh_reverse:
            coila.value(i[0])
            coilb.value(i[1])
            coilc.value(i[2])
            coild.value(i[3])
            time.sleep_ms(3)
