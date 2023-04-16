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
red = GPIO.PWM(r, 100)
green = GPIO.PWM(g, 100)
blue = GPIO.PWM(b, 100)

# displays a color based on values written
try:
    while True:
        R = input("Enter the value for red: ")
        G = input("Enter the value for green: ")
        B = input("Enter the value for blue: ")
        red.ChangeDutyCycle(R)
        green.ChangeDutyCycle(G)
        blue.ChangeDutyCycle(B)
        sleep(5)
    
except KeyboardInterrupt:
    GPIO.cleanup()