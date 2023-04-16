import RPi.GPIO as GPIO
from time import sleep
import dht11

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
dht = 13
HT = dht11.DHT11(pin = dht)

# get input from DHT sensor and print the temperature and humidity every minute
try:
    while True:
        output = HT.read()
        if output.is_valid():
            print("Temperature: " + output.temperature)
            print("Humidity: " + output.humidity)
        else:
            print("Unable to read.")
        sleep(60)

except KeyboardInterrupt:
    GPIO.cleanup()