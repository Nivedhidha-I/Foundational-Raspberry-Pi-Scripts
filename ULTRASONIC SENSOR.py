import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
TRIG = 11
ECHO = 13
GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)

#  check if any object is placed in the vicinity of the device
try:
    while True:
        GPIO.output(TRIG, GPIO.HIGH)
        time.sleep(0.00001)
        GPIO.output(TRIG, GPIO.LOW)
        while GPIO.input(ECHO) == 0:
            pulse_start = time.time()
        while GPIO.input(ECHO) == 1:
            pulse_end = time.time()
        distance = (pulse_end - pulse_start) * 17150
        distance = round(distance + 1.15, 2)
        if distance >= 5 and distance <= 20:
            print("Object found at ", distance, " cm.")
        else:
            print("No object present.")

except KeyboardInterrupt:
    GPIO.cleanup()