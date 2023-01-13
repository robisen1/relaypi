import RPi.GPIO as GPIO
import time


in1 = 18
in2 = 23
in3 = 24
in4 = 25
in5 = 18
in6 = 12
in7 = 16


GPIO.setmode(GPIO.BOARD)
GPIO.setup(in1, GPIO.OUT)
GPIO.setup(in2, GPIO.OUT)
GPIO.setup(in3, GPIO.OUT)
GPIO.setup(in4, GPIO.OUT)
GPIO.setup(in5, GPIO.OUT)
GPIO.setup(in6, GPIO.OUT)
GPIO.setup(in7, GPIO.OUT)


GPIO.output(in1, False)
GPIO.output(in2, False)
GPIO.output(in3, False)
GPIO.output(in4, False)
GPIO.output(in5, False)
GPIO.output(in6, False)
GPIO.output(in7, False)



try:
    while True:
      for x in range(5):
            GPIO.output(in1, True)
            GPIO.output(in2, True)
            GPIO.output(in5, True)
            time.sleep(0.1)
            GPIO.output(in1, False)
            GPIO.output(in2, True)
            GPIO.output(in5, True)
            time.sleep(0.1)
            GPIO.output(in2, False)
      
      GPIO.output(in1,True)
      GPIO.output(in2,True)
      GPIO.output(in4,True)
      GPIO.output(in5,True)

      for x in range(4):
            GPIO.output(in1, True)
            GPIO.output(in2, True)
            GPIO.output(in5, True)
            time.sleep(0.05)
            GPIO.output(in1, False)
            GPIO.output(in2, False)
            GPIO.output(in5, False)

            time.sleep(0.05)
      GPIO.output(in1,True)

      for x in range(4):
            GPIO.output(in4, True)
            time.sleep(0.05)
            GPIO.output(in4, False)
            time.sleep(0.05)
      GPIO.output(in2,True)



except KeyboardInterrupt:
    GPIO.cleanup()
