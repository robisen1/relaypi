import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

# init list with pin numbers

pinList = [18,23]

# loop through pins and set mode and state to 'low'

for i in pinList:
    GPIO.setup(i, GPIO.OUT)
    GPIO.output(i, GPIO.HIGH)

# time to sleep between operations in the main loop

SleepTimeL = 0.2

# main loop

try:
  while True:

    for i in pinList:
        GPIO.output(i, GPIO.HIGH)
        time.sleep(SleepTimeL);
        GPIO.output(i, GPIO.LOW)

    pinList.reverse()

    for i in pinList:
        GPIO.output(i, GPIO.HIGH)
        time.sleep(SleepTimeL);
        GPIO.output(i, GPIO.LOW)

    pinList.reverse()

# End program cleanly with keyboard

    GPIO.cleanup()
    print ("Good bye!")
  
  
except KeyboardInterrupt:
  print ("  Quit")

  # Reset GPIO settings
  GPIO.cleanup()
