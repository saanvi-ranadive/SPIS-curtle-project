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


def penup():
    lasttime = time.time()
    while True:
        currenttime = time.time()
        kit.servo[channel_servo].angle = 90
        if (currenttime - lasttime) > 1:
            break

def pendown():
    lasttime = time.time()
    while True:
        currenttime = time.time()
        kit.servo[channel_servo].angle = 0
        if (currenttime - lasttime) > 1:
            break

def forward():
    speed = 1
    kit.continuous_servo[0].throttle = speed
    kit.continuous_servo[4].throttle = -speed

def backward():
    speed = 1
    kit.continuous_servo[0].throttle = -speed
    kit.continuous_servo[4].throttle = speed

def turn1(): # change to left or right turn once hardware implemented
    speed = 1
    kit.continuous_servo[0].throttle = speed
    kit.continuous_servo[4].throttle = speed

def turn2(): # change to left or right turn once hardware implemented
    speed = -1
    kit.continuous_servo[0].throttle = speed
    kit.continuous_servo[4].throttle = speed


# Main program 
try:

    noError = True
    while noError:
        forward()
        time.sleep(5)
        backward()
        time.sleep(5)
        
# Quit the program when the user presses CTRL + C
except KeyboardInterrupt:
        kit.continuous_servo[channel_motor1].throttle = 0
        kit.continuous_servo[channel_motor2].throttle = 0
        