import RPi.GPIO as GPIO
import time
import sqlite3

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
FIRE = 11
BUZZER = 13
GPIO.setup(FIRE, GPIO.IN)
GPIO.setup(BUZZER, GPIO.OUT)
con = sqlite3.connect('homeautomation.db')
c = con.cursor()

# When fire is detected buzzer makes sound until the fire is not detected anymore. (D0 mode)
# Also this data of when the fire started and when it ends is stored in the database; whenever a fire is detected.
try:
    while True:
        fire = GPIO.input(FIRE)
        if fire:
            GPIO.output(BUZZER, GPIO.HIGH)
            date = time.strftime('%Y-%m-%d')
            Time = time.strftime('%H:%M:%S')
            c.execute("INSERT INTO FIRE(DATE, TIME, FIRE) VALUES(?,?,?)", (date, Time, fire))
            con.commit()
            while GPIO.input(FIRE):
                time.sleep(1)
            date = time.strftime('%Y-%m-%d')
            Time = time.strftime('%H:%M:%S')
            fire = GPIO.input(FIRE)
            c.execute("INSERT INTO FIRE(DATE, TIME, FIRE) VALUES(?,?,?)", (date, Time, fire))
            con.commit()
        else:
            GPIO.output(BUZZER, GPIO.LOW)

except KeyboardInterrupt:
    GPIO.cleanup()