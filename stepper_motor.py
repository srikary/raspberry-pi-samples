import RPi.GPIO as GPIO
import time
 
GPIO.setmode(GPIO.BCM)
 
direction_pin = 6
step_pin = 5

GPIO.setup(direction_pin, GPIO.OUT)
GPIO.setup(step_pin, GPIO.OUT)
 
 
def move_shaft(direction, delay, steps):
  GPIO.output(direction_pin, direction)
  for i in range(0, steps):
    GPIO.output(step_pin, GPIO.HIGH)
    time.sleep(delay)
    GPIO.output(step_pin, GPIO.LOW)

def forward(delay, steps):
  move_shaft(GPIO.HIGH, delay, steps)
  
def backward(delay, steps):
  move_shaft(GPIO.LOW, delay, steps)
 
while True:
  forward(0.002, 200)
  backward(0.003, 200)
