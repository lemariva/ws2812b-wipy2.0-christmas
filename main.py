from ws2812 import WS2812
from leds import LEDs
from utime import sleep_ms
import math as m
import pycom

# actual state				
state = 0 	

# rotate
rotate = 0	
rotate_max = 50
sleep_time_fast = 150 	

# dimmer
fadeout = 1	
dimmer = 1
dimmer_step = 0.05
dimmer_min_level = 0.5
sleep_time = 250

# dimming colors
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
gold = (255,255,0)


chain = WS2812( ledNumber=144,  brightness=100)
leds_color = LEDs(ledNumber=144)

while True:			
	if(state == 0):	
		pycom.rgbled(0x050505)
		
		leds_color.ledsmod1(dimmer)
		chain.show(leds_color.getData())		           
		sleep_ms( sleep_time )
		state = 1		# changing state
		
	elif(state == 1):
		pycom.rgbled(0x080808) 
		
		# all colors dimmer				
		leds_color.ledsmod1(dimmer)
		
		chain.show(leds_color.getData())	
		sleep_ms(sleep_time)			
		
		if (fadeout):
			dimmer -= dimmer_step
		else:
			dimmer += dimmer_step					
		
		if(dimmer < dimmer_min_level):
			fadeout = 0

		if(dimmer > 1):				
			rotate = 0
			dimmer = 1	
			fadeout = 1
			leds_color.ledsmod1(dimmer)									
			state = 2	# changing state
			
	elif(state == 2):
		pycom.rgbled(0x101010) 
		# rotate colors right
		leds_color.movR()
		
		chain.show(leds_color.getData())	
		sleep_ms(sleep_time_fast)					
		
		rotate += 1
		if(rotate == rotate_max):
			rotate = 0
			state = 3
			
	elif(state == 3):
		pycom.rgbled(0x121212) 
		# rotate colors left
		leds_color.movL()
		
		chain.show(leds_color.getData())	
		sleep_ms(sleep_time_fast)
		
		rotate += 1
		if(rotate == rotate_max):
			rotate = 0
			state = 4
			
	elif(state == 4):
		pycom.rgbled(0x141414) 
		# red color dimming 	
		leds_color.ledsmod2(red, dimmer)
		
		chain.show(leds_color.getData())	
		sleep_ms(sleep_time)
		
		if (fadeout):
			dimmer -= dimmer_step
		else:
			dimmer += dimmer_step
			
		if(dimmer < dimmer_min_level):
			fadeout = 0
		if(dimmer > 1):			
			dimmer = 1						
			fadeout = 1
			state = 5	# changing state	
	
	elif(state == 5):
		pycom.rgbled(0x161616) 
		# green color dimming 	
		leds_color.ledsmod2(green, dimmer)
		
		chain.show(leds_color.getData())	
		sleep_ms(sleep_time)
		
		if (fadeout):
			dimmer -= dimmer_step
		else:
			dimmer += dimmer_step
			
		if(dimmer < dimmer_min_level):
			fadeout = 0
			
		if(dimmer > 1):			
			dimmer = 1						
			fadeout = 1
			state = 6	# changing state	
    
	elif(state == 6):
		pycom.rgbled(0x181818) 
		# blue color dimming 
		leds_color.ledsmod2(blue, dimmer)
		
		chain.show(leds_color.getData())	
		sleep_ms(sleep_time)
		
		if (fadeout):
			dimmer -= dimmer_step
		else:
			dimmer += dimmer_step
			
		if(dimmer < dimmer_min_level):
			fadeout = 0
			
		if(dimmer > 1):			
			dimmer = 1
			fadeout = 1
			state = 7	# changing state
			
	elif(state == 7):
		pycom.rgbled(0x202020) 
		# gold color dimming 
		leds_color.ledsmod2(gold, dimmer)
		
		chain.show(leds_color.getData())	
		sleep_ms(sleep_time)		
		
		if (fadeout):
			dimmer -= dimmer_step
		else:
			dimmer += dimmer_step
			
		if(dimmer < dimmer_min_level):
			fadeout = 0
			
		if(dimmer > 1):			
			dimmer = 1						
			fadeout = 1
			state = 0	# changing state				