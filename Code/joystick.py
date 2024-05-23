
# SPDX-FileCopyrightText: 2018 Kattni Rembor for Adafruit Industries
#
# SPDX-License-Identifier: MIT

"""CircuitPython Essentials HID Mouse example"""
import time
import analogio
import board
import digitalio
import usb_hid
from time import sleep
from digitalio import DigitalInOut, Direction, Pull
from pwmio import PWMOut
from adafruit_motor import motor as Motor

# inputting all needed files

DEBUG = True  # mode of operation; False = normal, True = debug
drv8833_ain1 = PWMOut(board.GP17, frequency=50)
drv8833_ain2 = PWMOut(board.GP16, frequency=50)
drv8833_bin1 = PWMOut(board.GP18, frequency=50)
drv8833_bin2 = PWMOut(board.GP19, frequency=50)
drv8833_sleep = DigitalInOut(board.GP20)
motor_a = Motor.DCMotor(drv8833_ain1, drv8833_ain2)
motor_b = Motor.DCMotor(drv8833_bin1, drv8833_bin2)
drv8833_sleep.direction = Direction.OUTPUT
drv8833_sleep.value = True  # enable (turn on) the motor driver

# establishing all pins for the motors, as well as for the H bridge / also establishing the motor's driver capabilities


x_axis = analogio.AnalogIn(board.GP27)
y_axis = analogio.AnalogIn(board.GP26)
select = digitalio.DigitalInOut(board.A2)
select.direction = digitalio.Direction.INPUT
select.pull = digitalio.Pull.UP

# establishing the pins for the joystick as well as its capabilites of direction

pot_min = 0.00
pot_max = 3.29
step = (pot_max - pot_min) / 20.0

# establishing the range of inputs for the joystick

def get_voltage(pin):
    return (pin.value * 3.3) / 65536

# establishing voltage/pin values for joystick inputs

def steps(axis):
    """ Maps the potentiometer voltage range to 0-20 """
    return round((axis - pot_min) / step)

# defining steps for the motor

# def print_motor_status(motor):
#     if motor == motor_a:
#         motor_name = "A"
#     elif motor == motor_b:
#         motor_name = "B"
#     else:
#         motor_name = "Unknown"
#     print(f"Motor {motor_name} throttle is set to {motor.throttle}.")
def basic_operations():
    # Drive forward at full throttle
    motor_a.throttle = 1.0
    motor_b.throttle = 1.0

# defining basic movement of the motors to throttle at full capabilities

while True:
    x = get_voltage(x_axis)
    y = get_voltage(y_axis)

    if select.value is False:
        time.sleep(0.2)  # Debounce delay

    if steps(y) > 19.0:
         #print(f" Y: {steps(y)}") 
         print("Forward")
         motor_a.throttle = 1.0
         motor_b.throttle = 1.0

# if the joystick is pushed all the way up, both motors throttle forward
    
    elif steps(y) < 1.0:
         #print(f" Y: {steps(y)}")
         print("Backward")
         motor_a.throttle = -1.0
         motor_b.throttle = -1.0

# if the joystick is pushed all the way down, both motors throttle backward
    
    elif steps(x) > 19.0:
         #print(f" X: {steps(x)}")
         print("Turn left")
         motor_a.throttle = 1.0
         motor_b.throttle = -1.0

# if the joystick is pushed all the way to the right, one motor moves forward and the other backward, allowing it to turn
    
    elif steps(x) < 1.0:
         #print(f" X: {steps(x)}")
         print("Turn right")
         motor_a.throttle = -1.0
         motor_b.throttle = 1.0

# if the joystick is pushed all the way to the left, the other motor moves forward and the other backward, allowing it to turn the other way

    else:
         motor_a.throttle = 0.0
         motor_b.throttle = 0.0
