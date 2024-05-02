# G-Hog-mapper-notebook



# Planning

Our initial idea is to create a remote-controlled robot that can direct live-video feed back to the controller. We want to drive this robot through the groundhog tunnels at CHS and explore the intriquite designs within. We plan to achieve this by controlling motors using a joystick, and some form of screen/camera to see video.  

## Initial brainstorming 

https://learn.adafruit.com/ttl-serial-camera/overview

https://learn.adafruit.com/adafruit-2-8-and-3-2-color-tft-touchscreen-breakout-v2

<img src="images/ChasisDrawing.PNG" width="300">

## Materials

<img src="images/MetalSheet.jpg" width="200">

<img src="images/WoodSheet.jpg" width="200">


# November

<img src="images/MotorDiagram.jpg" width="300">

Diagram drawn by Miller for utilizing the high torque motors / H-bridge (DRV8833)

Figured out code to move high-torque motors back and forth. Currently working on a method to move the motors independently of each other and the computer (Joystick, switch, etc.)

<img src="images/ezgif.com-crop.gif" width="200">

Had to workshop the code using other code in order to be able to use the motors to move back and forth / left and right.

[Joystick Code](Code/joystick.py)

Wiring diagram for the joystick (Motor 1 is connected to AOUT 1 (power) and AOUT 2 (ground) / Motor 2 is connected to BOUT 1 (power) and BOUT 2 (ground)

<img src="images/wiringdiagramjoystick.png" width="200">

# December

We have decided to use a LoRa board with an extra pico to be able to control the motors wirelessly. We have no LoRa experience and may be difficult to pursue for our purpose

We researched the LoRa boards and brainstormed with our mentors in-person on how to move forward in our project. We have realized that we cannot transmit video from one LoRa board to another, but we will still try to see if they are feasable to transmit the signal for the joystick/motors. 


# January 

# February 

# March

# April

# May



# 12/15/23 Review

### What did you work on?
We began to wire the LoRa boards and began writing code to make the boards talk to each other.

### What decisions were made?
We decided we will use treads to move the vehicle and have finalized the decision to wire the boards together.

### What new resources did you find?
Circuit python forums depicting code for the LoRa boards.

### What new issues were discovered?
The LoRa board is complicated and requires more time than expected to understand the intricacies. 

### What went well?
We established a clear path for completing the LoRa section of our project.

### What was difficult?
It was difficult attempting to connect the LoRa boards via code.

### What is your plan for next week?
Get the boards to talk to each other.

# 2/9/24

We started printing treads for the robot and researching the camera/LCD screen.

# 2/16/24

This week the French people were here in Charlottesville. We got minimal work done during this time.

# 2/23/24

Mentors came this week. We got feedback from several UVA students and finalized our idea to fully wire the robot. We also got started on wiring and coding the LCD screen and were directed to focus on that before the camera.

# 2/29/24

We got the LCD screen to turn on with basic code and continued to print treads and wheels for the robot.

### What we have worked on

We have created the tank treads in onshape, as well as focused on wiring/coding the camera. 

<img src="images/projectlayout.png" width="900">

Decided to scrap LoRa and just fully wire it. Wires shown on the diagram are an accurate estimation of how many we will truly need. However we are not 100% sure of how many the LCD screen will require.


# April

Currently testing the LCD screen as a shield on a metro express board, struggling to figure out the code


Updated wiring diagram concerning the joystick control

<img src="images/wiringdiagramjoystick.png" width="900">



