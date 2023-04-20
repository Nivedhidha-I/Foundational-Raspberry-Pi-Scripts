import RPi.GPIO as GPIO
import time
import sqlite3

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
LDR = 13
GPIO.setup(LDR, GPIO.IN)
con = sqlite3.connect('ldr.db')
c = con.cursor()

# get data from LDR and store it in sqlite3 database
try:
    while True:
        ldr = GPIO.output(LDR)
        Time = time.strftime("%H:%M:%S")
        Date = time.strftime("%Y-%m-%d")
        c.execute("INSERT INTO LDR(ldr, time, date) VALUES(?, ?, ?)", (ldr, Time, Date))
        con.commit()
        time.sleep(60)

except KeyboardInterrupt:
    GPIO.cleanup()