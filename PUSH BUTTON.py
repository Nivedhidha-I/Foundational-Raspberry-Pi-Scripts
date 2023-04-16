import RPi.GPIO as GPIO
from time import sleep

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
push_button = 13
GPIO.setup(push_button, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)

# when button is pressed it outputs the same and since it is pull down switch mode True when pressed and False when removed 
try:
    while True:
        if GPIO.input(push_button) == True:
            print("Button pressed")
        else:
            print("Button not pressed")
        sleep(1)

except KeyboardInterrupt:
    GPIO.cleanup()