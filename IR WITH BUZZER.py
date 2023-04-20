import RPi.GPIO as GPIO
from time import sleep

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
IR = 11
BUZZER = 13
GPIO.setup(IR, GPIO.IN)
GPIO.setup(BUZZER, GPIO.OUT)

# getting input from IR sensor if sensed any object then buzzer is played till object is out of vicinity.
try:
    while True:
        if GPIO.input(IR):
            GPIO.output(BUZZER, GPIO.HIGH)
            while GPIO.input(IR):
                sleep(1)
        else:
            GPIO.output(BUZZER, GPIO.LOW)

except KeyboardInterrupt:
    GPIO.cleanup()