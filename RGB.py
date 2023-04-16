import RPi.GPIO as GPIO
from time import sleep

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
r = 11
g = 13
b = 15
GPIO.setup(r, GPIO.OUT)
GPIO.setup(g, GPIO.OUT)
GPIO.setup(b, GPIO.OUT)

# displays red for first second then green finally blue
try:
    while True:
        GPIO.output(r, GPIO.HIGH)
        GPIO.output(g, GPIO.LOW)
        GPIO.output(b, GPIO.LOW)
        sleep(1)
        GPIO.output(r, GPIO.LOW)
        GPIO.output(g, GPIO.HIGH)
        GPIO.output(b, GPIO.LOW)
        sleep(1)
        GPIO.output(r, GPIO.LOW)
        GPIO.output(g, GPIO.LOW)
        GPIO.output(b, GPIO.HIGH)
        sleep(1)
    
except KeyboardInterrupt:
    GPIO.cleanup()