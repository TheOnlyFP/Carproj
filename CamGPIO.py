#!/usr/bin/python

import RPi.GPIO as GPIO
from time import sleep
import numpy as np
import cv2
from Camtest_vbest import camcap

position = 0

#import ends

GPIO.setmode(GPIO.BCM)
inchan_list = [27,23,22] #Insert Anime joke here
outchan_list = [21,20,26,19,16,13,6,5] #-\\-
GPIO.setup(inchan_list, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) #Sets them up as inputs
GPIO.setup(outchan_list, GPIO.OUT, initial=GPIO.LOW) #Sets them up as outputs

freq= 15

#setup end

forward_list = [21,19,13,6] #All channels that make the wheels go forward
forward_stop = [20,26,16,5] #Reverse, but also to turn the other direction off
left_list = [26,16,21,6] #to turn car left / left motors go back
right_list = [19,13,20,5] # -\\- right
all_list = [20,19,13,5,21,26,16,6]
pwmflf = GPIO.PWM(19,freq)
pwmblf = GPIO.PWM(13,freq)
pwmfrf = GPIO.PWM(21,freq)
pwmbrf = GPIO.PWM(6, freq)
pwmflb = GPIO.PWM(26,freq)
pwmblb = GPIO.PWM(16,freq)
pwmfrb = GPIO.PWM(20,freq)
pwmbrb = GPIO.PWM(5, freq)

#motorlist end

#mfl = f(19) b(26)
#mbl = f(13) b(16)
#mfr = f(21) b(20)
#mbr = f(6)  b(5)

Maxcorrectup=100
Mincorrectup=100
Maxcorrectdown=0
Mincorrectdown=0
Setpoint=0
Error=0
Waittime=1000

#Negative vals = turn right
#Positive vals = turn left

#Motorpins end


def main():
    print("main")
    main2()
                     
def main2():
    try:
        while True:
            value = camcap()
            print(value)
            if value[1] < 20000: #forward
                Correction = 100
                allforward(Correction)
            elif value[0] > 20000 and value[2] < 20000: #right
                turnright(int(value[0]/61200)*100)
                print("Value 2: ", value[2])
                print("right")
            elif value[2] > 20000 and value[0] < 20000: #Left
                turnleft(int(value[2]/61200)*100)
                print("Value 0: ", value[0])
                print("left")
            elif value[2] >20000 and value[0] > 20000:
                print("backwards")
            print("end")
    except KeyboardInterrupt:
        GPIO.cleanup()

def allforward(dc):
    print(dc)
    GPIO.output(forward_stop, 0)
    pwmfrf.start(dc)    
    pwmbrf.start(dc)
    pwmflf.start(dc)
    pwmblf.start(dc)

    
def turnleft(dc):
    print(dc)
    if dc > Maxcorrectup:
        dc= Maxcorrectup
    elif dc < Mincorrectup:
        dc= Mincorrectup 
    GPIO.output(left_list, 0)
    pwmfrf.start(dc)
    pwmbrf.start(dc)
    pwmflb.start(dc)
    pwmblb.start(dc)

#left_list = [26,16,21,6] #to turn car left
#right_list = [19,13,20,5] # -\\- right 

def turnright(dc):
    print(dc)
    if dc < Maxcorrectdown:
        dc=Maxcorrectdown
    elif dc > Mincorrectdown:
        dc=Mincorrectdown
    GPIO.output(right_list, 0) 
    pwmflf.start(dc)
    pwmblf.start(dc)
    pwmfrb.start(dc)
    pwmbrb.start(dc)

#function end


#Event end

GPIO.output(right_list, 0)

print("start")

main()

GPIO.cleanup()

#Code end
