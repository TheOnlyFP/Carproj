import RPi.GPIO as GPIO
from time import sleep

freq = 15
no = 'n'

GPIO.setmode(GPIO.BCM)

inchan_list = [27,23,22] #Insert Anime joke here
outchan_list = [21,20,26,19,16,13,6,5] #-\\-
GPIO.setup(inchan_list, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) #Sets them up as inputs
GPIO.setup(outchan_list, GPIO.OUT, initial=GPIO.LOW) #Sets them up as outputs


pwmflf = GPIO.PWM(19,freq)
pwmblf = GPIO.PWM(13,freq)
pwmfrf = GPIO.PWM(21,freq)
pwmbrf = GPIO.PWM(6, freq)
pwmflb = GPIO.PWM(26,freq)
pwmblb = GPIO.PWM(16,freq)
pwmfrb = GPIO.PWM(20,freq)
pwmbrb = GPIO.PWM(5, freq)


pwmflf.start(100)
flf = input('frontleft forward: ')
pwmflf.stop()
pwmflb.start(100)
flb = input('frontleft backward: ')
pwmflb.stop()
pwmblf.start(100)
blf = input('backleft forward: ')
pwmblf.stop()
pwmblb.start(100)
blb = input('backleft backward: ')
pwmblb.stop()
pwmfrf.start(100)
frf = input('frontright forward: ')
pwmfrf.stop()
pwmfrb.start(100)
frb = input('frontright backward: ')
pwmfrb.stop()
pwmbrf.start(100)
brf = input('backright forward: ')
pwmbrf.stop()
pwmbrb.start(100)
brb = input('backward backward: ')
pwmbrb.stop()

if (flf == no) or (flb == no):
	print('swap 19 and 26')
	
if (blb == no) or (blf == no):
	print('swap 13 and 16') 
	
if (frf == no) or (frb == no):
	print('swap 21 and 20') 
	
if (brf == no) or (brb == no):
	print('swap 6 and 5') 	

GPIO.cleanup()
