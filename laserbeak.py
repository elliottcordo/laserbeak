#!/usr/bin/python

from bootstrap import *
import dweepy
import time
from datetime import datetime


mad = (255.0, 0.0, 0.0)
happy = (0.0, 255.0, 0.0)
sorta_mad = (255.0, 255.0, 102)

while True: 

    led.fillOff()
    led.all_off()
    
    if datetime.now().hour < 10:
        print "sleepy time"
        sleep(60)
        continue

    mood = dweepy.get_latest_dweet_for('yourthing')[0]['content']['status']
    print  mood

    step = 0.01
    if mood == 'failure':
        c = mad
    elif mood == 'warning':
        c = sorta_mad
    else:
        c = happy
    r, g, b = c

    if mood in ('success', 'warning'):
        print 'color range'
	level = 0.01
	dir = step
	while level >= 0.0:
		led.fill(Color(r, g, b, level))
		led.update()
		if(level >= 0.99):
			dir = -step
		level += dir
		#sleep(0.005)

    else: #failure
        print 'sin wave animations'
        anim = Wave(led, Color(r, g, b), 4)
        for i in range(led.lastIndex):
            anim.step()
            led.update()
            #sleep(0.15)

