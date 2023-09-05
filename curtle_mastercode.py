# This program demonstrates the use of the PCA9685 PWM driver
# This is useful to effectively control multiple servos or motors
# In this example, there is a standard servo on channel 0 and 
# a motor or continuous rotation servo(on channel 2). You can
# also test this code with only one of the two channels in use
# (just don't connect anything to the other channel)

# Libraries
import time
from adafruit_servokit import ServoKit

# Initialize ServoKit for the PWA board.
kit = ServoKit(channels=16)

# Specify the channels you are using on the PWM driver
channel_servo = 8
channel_motor1 = 0
channel_motor2 = 4

# To set the servo range to 180 degrees
# You can adjust the values if needed
kit.servo[channel_servo].set_pulse_width_range(400,2300)
kit.continuous_servo[channel_motor1].set_pulse_width_range(1200,1800)
kit.continuous_servo[channel_motor2].set_pulse_width_range(1200,1800)

#pen states

def penup():
    kit.servo[channel_servo].angle = 30
    time.sleep(1)

def pendown():
    kit.servo[channel_servo].angle = 51
    time.sleep(1.5)

def pencap():
    kit.servo[channel_servo].angle = 5
    time.sleep(1)
    
# motion

def forward(l):
    speed = 1
    kit.continuous_servo[0].throttle = speed
    kit.continuous_servo[4].throttle = -0.98*speed
    t = (3/21.5)*l
    time.sleep(t)
    kit.continuous_servo[0].throttle = 0
    kit.continuous_servo[4].throttle = 0

def backward(l):
    speed = 1
    kit.continuous_servo[0].throttle = -speed
    kit.continuous_servo[4].throttle = 0.99*speed
    t = (3/21.3)*l
    time.sleep(t)
    kit.continuous_servo[0].throttle = 0
    kit.continuous_servo[4].throttle = 0

def left(a):
    speed = -1
    kit.continuous_servo[0].throttle = speed
    kit.continuous_servo[4].throttle = 0.98*speed
    t = (1/54.5)*a
    time.sleep(t)
    kit.continuous_servo[0].throttle = 0
    kit.continuous_servo[4].throttle = 0

def right(a):
    speed = 1
    kit.continuous_servo[0].throttle = 0.96*speed
    kit.continuous_servo[4].throttle = speed
    t = (1/57.6)*a
    time.sleep(t)
    kit.continuous_servo[0].throttle = 0
    kit.continuous_servo[4].throttle = 0

# name letters

def drawC():
    forward(4)
    left(90)
    forward(6)
    left(90)
    pendown()
    forward(4)
    left(90)
    forward(6)
    left(90)
    forward(4)
    penup()
    forward(1)

def drawU():
    right(90)
    backward(6)
    pendown()
    forward(6)
    left(90)
    forward(4)
    left(90)
    forward(6)
    penup()
    backward(6)
    right(90)
    forward(1)

def drawT():
    left(90)
    forward(6)
    right(90)
    pendown()
    forward(4)
    penup()
    backward(2)
    right(90)
    pendown()
    forward(6)
    penup()
    left(90)
    forward(3)

def drawL():
    right(90)
    backward(6)
    pendown()
    forward(6)
    left(90)
    forward(4)
    penup()
    forward(1)

def drawE():
    pendown()
    forward(4)
    penup()
    backward(4)
    left(90)
    pendown()
    forward(3)
    right(90)
    forward(4)
    penup()
    backward(4)
    left(90)
    pendown()
    forward(3)
    right(90)
    forward(4)
    penup()
    right(90)
    forward(6)
    left(90)
    forward(1)

# SPIS 2023

# Main program 
try:
    penup()
    pendown()
    penup()
    
    forward(4)
    left(90)
    forward(6)
    left(90)
    pendown()
    forward(4)
    left(90)
    forward(6)
    left(90)
    forward(4)
    penup()
    forward(1)
    
    pendown()
    penup()
        
# Quit the program when the user presses CTRL + C
except KeyboardInterrupt:
        kit.continuous_servo[channel_motor1].throttle = 0
        kit.continuous_servo[channel_motor2].throttle = 0
        