#!/usr/bin/python

from bootstrap import *

#setup colors to loop through for fade

n = 0
while n < 10:
    anim = LarsonRainbow(led, 2, 0.5)
    for i in range(led.lastIndex*4):
	anim.step()
	led.update()
	sleep(0.03)
        n += 1




