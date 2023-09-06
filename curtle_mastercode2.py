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
    time.sleep(1)

def pencap():
    kit.servo[channel_servo].angle = 15
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
    t = (1/57.7)*a
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

def drawH():
    left(91.5)
    pendown()
    forward(5)
    penup()
    backward(2.5)
    right(91.5)
    pendown()
    forward(3)
    penup()
    right(88)
    backward(2.3)
    pendown()
    forward(5)
    penup()
    left(94)
    forward(1)

def drawI():
    left(90)
    pendown()
    forward(5)
    penup()
    backward(5)
    right(87)
    forward(1)
    
def drawM():
    left(95)
    pendown()
    forward(5)
    right(135)
    forward(2)
    left(90)
    forward(2)
    right(130)
    forward(5.5)
    penup()
    left(92)
    forward(1)
    
def drawC():
    forward(3)
    left(90)
    forward(5)
    left(90)
    pendown()
    forward(3)
    left(89)
    forward(5)
    left(90)
    forward(3.7)
    penup()
    forward(1)
    
def drawU():
    right(87)
    backward(5.25)
    pendown()
    forward(5)
    left(91)
    forward(3)
    left(90)
    forward(5.5)
    penup()
    backward(5.5)
    right(90)
    forward(1)

def drawR():
    left(93)
    pendown()
    forward(5)
    right(89)
    forward(3)
    right(88)
    forward(2.5)
    right(88)
    forward(3)
    left(144)
    forward(4.8)
    penup()
    left(47)
    forward(1)

def drawT():
    left(91)
    forward(5.5)
    right(90)
    pendown()
    forward(4)
    penup()
    backward(2.2)
    right(90)
    pendown()
    forward(5.5)
    penup()
    left(94)
    forward(3)
    
def drawL():
    right(88.5)
    backward(5.4)
    pendown()
    forward(5.1)
    left(90.5)
    forward(4)
    penup()
    forward(1)

def drawE():
    pendown()
    forward(4)
    penup()
    backward(4)
    left(92)
    pendown()
    forward(2.5)
    right(88.5)
    forward(4)
    penup()
    backward(4)
    left(92)
    pendown()
    forward(2.5)
    right(88)
    forward(4)
    penup()
    right(89)
    forward(5)
    left(94)
    forward(1)

def drawsquare():
    penup()
    pendown()
    for x in range(4):
        forward(4)
        left(90)
    penup()
    
# Main program 
try:
    penup()
    drawH()
    drawI()
    forward(4)
    drawI()
    drawM()
#     left(25)
#     backward(20)
#     right(22)
#     drawC()
#     drawU()
#     drawR()
#     drawT()
#     drawL()
#     drawE()
        
# Quit the program when the user presses CTRL + C
except KeyboardInterrupt:
        kit.continuous_servo[channel_motor1].throttle = 0
        kit.continuous_servo[channel_motor2].throttle = 0
        