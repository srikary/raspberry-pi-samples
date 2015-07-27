import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(0, GPIO.OUT)
pwm = GPIO.PWM(0, 100)
pwm.start(5)


def update(angle):
  duty = float(angle) / 10.0 + 2.5
  pwm.ChangeDutyCycle(duty)

delay_period = 0.01
 
while True:
	for angle in range(0, 180):
		update(angle)
		time.sleep(delay_period)
	for angle in range(0, 180):
		update(180 - angle)
		time.sleep(delay_period)
