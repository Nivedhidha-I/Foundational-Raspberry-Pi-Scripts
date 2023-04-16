import RPi.GPIO as GPIO
from time import sleep

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
buzzer = 13
GPIO.setup(LED, GPIO.OUT)

# buzzer makes sound on and off every second
try:
    while True:
        GPIO.output(buzzer, GPIO.HIGH)
        sleep(1)
        GPIO.output(buzzer, GPIO.LOW)
        sleep(1)
    
except KeyboardInterrupt:
    GPIO.cleanup()