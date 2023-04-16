import RPi.GPIO as GPIO
from time import sleep

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
LED = 13
GPIO.setup(LED, GPIO.OUT)

# LED blinks on and off every second
try:
    while True:
        GPIO.output(LED, GPIO.HIGH)
        sleep(1)
        GPIO.output(LED, GPIO.LOW)
        sleep(1)
    
except KeyboardInterrupt:
    GPIO.cleanup()