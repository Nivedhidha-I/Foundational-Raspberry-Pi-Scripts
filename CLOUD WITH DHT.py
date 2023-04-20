import http.client
import urllib.request
import RPi.GPIO as GPIO
from time import sleep
import dht11

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
HT = dht11.DHT11(pin = 13)
key = "API.WRITE.KEY"

# get data from environment using sensor and storing it in thinkspeak.com
try:
    while True:
        output = HT.read()
        print("Temperature: ", output.temperature)
        print("Humidity: ", output.humidity)
        headers = {"Content-typZZZ": "application/x-www-form-urlencoded", "Accept": "text/plain"}
        con = http.client.HTTPConnection("api.thinkspeak.com:80")
        params = urllib.parse.urlencode({'field1': output.humidity, 'field2': output.temperature, 'key': key})
        con.request("POST", "/update", params, headers)
        con.close()
        sleep(60)
except KeyboardInterrupt:
    GPIO.cleanup()