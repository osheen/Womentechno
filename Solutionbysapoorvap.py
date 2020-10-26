#1)Full Clockwise Stepper Motor :-

import Adafruit_BBIO.GPIO as GPIO
import time

GPIO.setup("P9_11",GPIO.OUT)
GPIO.setup("P9_12",GPIO.OUT)
GPIO.setup("P9_13",GPIO.OUT)
GPIO.setup("P9_14",GPIO.OUT)

while True:

    GPIO.output("P9_11",GPIO.HIGH)
    GPIO.output("P9_12",GPIO.HIGH)
    GPIO.output("P9_13",GPIO.LOW)
    GPIO.output("P9_14",GPIO.LOW)
    time.sleep(10)
    GPIO.output("P9_11",GPIO.LOW)
    GPIO.output("P9_12",GPIO.HIGH)
    GPIO.output("P9_13",GPIO.HIGH)
    GPIO.output("P9_14",GPIO.LOW)
    time.sleep(10)
    GPIO.output("P9_11",GPIO.LOW)
    GPIO.output("P9_12",GPIO.LOW)
    GPIO.output("P9_13",GPIO.HIGH)
    GPIO.output("P9_14",GPIO.HIGH)
    time.sleep(10)
    GPIO.output("P9_11",GPIO.HIGH)
    GPIO.output("P9_12",GPIO.LOW)
    GPIO.output("P9_13",GPIO.LOW)
    GPIO.output("P9_14",GPIO.HIGH)
    time.sleep(10)


	                  


#2) full anti-clockwise stepper motor:-
import Adafruit_BBIO.GPIO as GPIO
import time

GPIO.setup("P9_11",GPIO.OUT)
GPIO.setup("P9_12",GPIO.OUT)
GPIO.setup("P9_13",GPIO.OUT)
GPIO.setup("P9_14",GPIO.OUT)

while True:

    GPIO.output("P9_11",GPIO.LOW)
    GPIO.output("P9_12",GPIO.LOW)
    GPIO.output("P9_13",GPIO.HIGH)
    GPIO.output("P9_14",GPIO.HIGH)
    time.sleep(5)
    GPIO.output("P9_11",GPIO.HIGH)
    GPIO.output("P9_12",GPIO.LOW)
    GPIO.output("P9_13",GPIO.LOW)
    GPIO.output("P9_14",GPIO.HIGH)
    time.sleep(5)
    GPIO.output("P9_11",GPIO.HIGH)
    GPIO.output("P9_12",GPIO.HIGH)
    GPIO.output("P9_13",GPIO.LOW)
    GPIO.output("P9_14",GPIO.LOW)
    time.sleep(5)
    GPIO.output("P9_11",GPIO.LOW)
    GPIO.output("P9_12",GPIO.HIGH)
    GPIO.output("P9_13",GPIO.HIGH)
    GPIO.output("P9_14",GPIO.LOW)
    time.sleep(5)


	                  
# 3) Half clockwise stepper motor:-

import Adafruit_BBIO.GPIO as GPIO
import time

GPIO.setup("P9_11",GPIO.OUT)
GPIO.setup("P9_12",GPIO.OUT)
GPIO.setup("P9_13",GPIO.OUT)
GPIO.setup("P9_14",GPIO.OUT)

while True:

    GPIO.output("P9_11",GPIO.HIGH)
    GPIO.output("P9_12",GPIO.LOW)
    GPIO.output("P9_13",GPIO.LOW)
    GPIO.output("P9_14",GPIO.LOW)
    time.sleep(5)
    GPIO.output("P9_11",GPIO.HIGH)
    GPIO.output("P9_12",GPIO.HIGH)
    GPIO.output("P9_13",GPIO.LOW)
    GPIO.output("P9_14",GPIO.LOW)
    time.sleep(5)
    GPIO.output("P9_11",GPIO.LOW)
    GPIO.output("P9_12",GPIO.HIGH)
    GPIO.output("P9_13",GPIO.LOW)
    GPIO.output("P9_14",GPIO.LOW)
    time.sleep(5)
    GPIO.output("P9_11",GPIO.LOW)
    GPIO.output("P9_12",GPIO.HIGH)
    GPIO.output("P9_13",GPIO.HIGH)
    GPIO.output("P9_14",GPIO.LOW)
    time.sleep(5)
    GPIO.output("P9_11",GPIO.LOW)
    GPIO.output("P9_12",GPIO.LOW)
    GPIO.output("P9_13",GPIO.HIGH)
    GPIO.output("P9_14",GPIO.LOW)
    time.sleep(5)
    GPIO.output("P9_11",GPIO.LOW)
    GPIO.output("P9_12",GPIO.LOW)
    GPIO.output("P9_13",GPIO.HIGH)
    GPIO.output("P9_14",GPIO.HIGH)
    time.sleep(5)
    GPIO.output("P9_11",GPIO.LOW)
    GPIO.output("P9_12",GPIO.LOW)
    GPIO.output("P9_13",GPIO.LOW)
    GPIO.output("P9_14",GPIO.HIGH)
    time.sleep(5)
    GPIO.output("P9_11",GPIO.HIGH)
    GPIO.output("P9_12",GPIO.LOW)
    GPIO.output("P9_13",GPIO.LOW)
    GPIO.output("P9_14",GPIO.HIGH)
    time.sleep(10)

	                  
# 4) Half anti-clockwise stepper motor:-
import Adafruit_BBIO.GPIO as GPIO
import time

GPIO.setup("P9_11",GPIO.OUT)
GPIO.setup("P9_12",GPIO.OUT)
GPIO.setup("P9_13",GPIO.OUT)
GPIO.setup("P9_14",GPIO.OUT)

while True:

    GPIO.output("P9_11",GPIO.LOW)
    GPIO.output("P9_12",GPIO.HIGH)
    GPIO.output("P9_13",GPIO.HIGH)
    GPIO.output("P9_14",GPIO.HIGH)
    time.sleep(5)
    GPIO.output("P9_11",GPIO.LOW)
    GPIO.output("P9_12",GPIO.LOW)
    GPIO.output("P9_13",GPIO.HIGH)
    GPIO.output("P9_14",GPIO.HIGH)
    time.sleep(5)
    GPIO.output("P9_11",GPIO.HIGH)
    GPIO.output("P9_12",GPIO.LOW)
    GPIO.output("P9_13",GPIO.HIGH)
    GPIO.output("P9_14",GPIO.HIGH)
    time.sleep(5)
    GPIO.output("P9_11",GPIO.HIGH)
    GPIO.output("P9_12",GPIO.LOW)
    GPIO.output("P9_13",GPIO.LOW)
    GPIO.output("P9_14",GPIO.HIGH)
    time.sleep(5)
    GPIO.output("P9_11",GPIO.HIGH)
    GPIO.output("P9_12",GPIO.HIGH)
    GPIO.output("P9_13",GPIO.LOW)
    GPIO.output("P9_14",GPIO.HIGH)
    time.sleep(5)
    GPIO.output("P9_11",GPIO.HIGH)
    GPIO.output("P9_12",GPIO.HIGH)
    GPIO.output("P9_13",GPIO.LOW)
    GPIO.output("P9_14",GPIO.LOW)
    time.sleep(5)
    GPIO.output("P9_11",GPIO.HIGH)
    GPIO.output("P9_12",GPIO.HIGH)
    GPIO.output("P9_13",GPIO.HIGH)
    GPIO.output("P9_14",GPIO.LOW)
    time.sleep(5)
    GPIO.output("P9_11",GPIO.LOW)
    GPIO.output("P9_12",GPIO.HIGH)
    GPIO.output("P9_13",GPIO.HIGH)
    GPIO.output("P9_14",GPIO.LOW)
    time.sleep(10)

	                  
					  
