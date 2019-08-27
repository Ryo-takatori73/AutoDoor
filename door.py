#!/usr/bin/env python
#-*- coding: utf-8 -*-

import time
import RPi.GPIO as GPIO



INTAVAL = 3
SLEEPTIME = 1
SENSOR_PIN = 33

GPIO.cleanup()




GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(33,GPIO.IN)
GPIO.setup(8,  GPIO.OUT)
GPIO.setup(10, GPIO.OUT)
GPIO.setup(12, GPIO.OUT)
GPIO.setup(38,  GPIO.OUT)
GPIO.setup(40, GPIO.OUT)
GPIO.setup(32, GPIO.OUT)

pwmR = GPIO.PWM(12, 50)
pwmR.start(0)
pwmL = GPIO.PWM(32, 50)
pwmL.start(0)
print("Ready:")
def openA():
    print ('==>OPEN')
    pwmR.ChangeDutyCycle(0)
    GPIO.output(8,  1)
    GPIO.output(10, 0)
    pwmL.ChangeDutyCycle(0)
    GPIO.output(38,  1)
    GPIO.output(40, 0)
    print ('====>OPENING')
    pwmR.ChangeDutyCycle(100)
    pwmL.ChangeDutyCycle(100)
    

def stopA():
    print ('==>stopA')
    GPIO.output(8, 1)
    GPIO.output(10, 1)
    GPIO.output(38, 1)
    GPIO.output(40, 1)
    print("====>Stopped")
def closeA():
    print("==>Close")
    GPIO.output(8, 0)
    GPIO.output(10, 1)
    GPIO.output(38, 0)
    GPIO.output(40, 1)
    print("====>Closing")


def stopB():
    print("==>stopB")
    GPIO.output(8, 0)
    GPIO.output(10, 0)
    GPIO.output(38, 0)
    GPIO.output(40, 0)
    print("====>stopped")
    
def endA():
    print("==>Ending")
    GPIO.cleanup()
    print(":end")


st = time.time()-INTAVAL
last=0
def openD(last):
    if(last<1):
        openA()
        time.sleep(5)
        stopA()
        stopB()
def closeD(last):
    if(last==-3):
        closeA()
        time.sleep(5)
        stopA()
        stopB()
        
try:
  while True:
  
    print ("==>Detect: "+str(GPIO.input(SENSOR_PIN)))
    if(GPIO.input(SENSOR_PIN)==0):
      last = last-1
      closeD(last)
    if(GPIO.input(SENSOR_PIN)) and (st + INTAVAL < time.time()):
      st = time.time()
      print("==>人を感知しました")
      openD(last)
      last = 1
 

    time.sleep(SLEEPTIME)
except KeyboardInterrupt:
  pass
print("==>cleaning")
GPIO.cleanup()
print("====>Cleaned")
print("==>close")
print(":end")

