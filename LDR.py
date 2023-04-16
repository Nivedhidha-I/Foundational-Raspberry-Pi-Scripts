import RPi.GPIO as GPIO
from time import sleep

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
ldr = 13
GPIO.setup(ldr, GPIO.IN)

# get input from LDR and print if dark or bright
try:
    while True:
        if GPIO.output(ldr):
            print("The surrounding is bright.")
        else:
            print("The surrounding is dark.")
        sleep(60)

except KeyboardInterrupt:
    GPIO.cleanup()