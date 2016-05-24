#!/usr/bin/python

from bootstrap import *

while True: 
#setup colors to loop through for fade
    colors = [
	(178.0,255.0,102.0),
	(0.0,128.0,255.0),
	(0.0,255.0,255.0),
	(255.0,255.0,51.0),
    ]
    # colors = [
    #     (255.0,0.0,0.0),
    #     (0.0,255.0,0.0),
    #     (0.0,0.0,255.0),
    #     (255.0,255.0,255.0),
    # ]


    step = 0.01
    for c in range(4):
        print 'color range'
	r, g, b = colors[c]
	level = 0.01
	dir = step
	while level >= 0.0:
		led.fill(Color(r, g, b, level))
		led.update()
		if(level >= 0.99):
			dir = -step
		level += dir
		#sleep(0.005)

    led.fillOff()
#    led.all_off()

#animations - each animation method moves the animation forward one step on each call
#after each step, call update() to push it to the LED strip
    print 'sin wave animations'
    anim = Wave(led, Color(0, 255, 255), 4)
    for i in range(led.lastIndex):
	anim.step()
	led.update()
	#sleep(0.15)

    anim = Wave(led, Color(204, 0, 204), 2)
    for i in range(led.lastIndex):
	anim.step()
	led.update()
	#sleep(0.15)


    print 'rolling rainbow'
    anim = Rainbow(led)
    for i in range(384):
	anim.step()
	led.update()

    led.fillOff()


    print 'evenly distributed rainbow'
    anim = RainbowCycle(led)
    for i in range(384*2):
	anim.step()
	led.update()

    led.fillOff()

    #setup colors for wipe and chase
    colors = [
	Color(255, 0, 0),
	Color(0, 255, 0),
	Color(0, 0, 255),
	Color(255, 255, 255),
    ]

    for c in range(4):
	anim = ColorWipe(led, colors[c])

	for i in range(num):
		anim.step()
		led.update()
		#sleep(0.03)

    led.fillOff()

    for c in range(4):
	anim = ColorChase(led, colors[c])

	for i in range(num):
		anim.step()
		led.update()
		#sleep(0.03)

    led.fillOff()

    print 'scanner: single color and changing color'
    anim = LarsonScanner(led, Color(255, 0, 0))
    for i in range(led.lastIndex*4):
	anim.step()
	led.update()
	#sleep(0.03)

    led.fillOff()
    print 'larson rainbow'
    anim = LarsonRainbow(led, 2, 0.5)
    for i in range(led.lastIndex*4):
        anim.step()
        led.update()
        sleep(0.03)

# led.all_off()
    led.fillOff()
    print "cycle complete"


