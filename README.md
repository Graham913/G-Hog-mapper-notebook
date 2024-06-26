# G-Hog-mapper-notebook

## Issue at hand

Groundhogs have become a massive problem in the outdoor community of CHS. They dig holes in multiple places around the CHS garden which people could step in and hurt themselves. They also eat the vegetation. These matters cause the CHS Garden and Urban Farming classes to be unsafe environments. 

We wish to alleviate these issues and gather more information about the groundhogs by creating a robot to inspect the groundhog tunnels. By doing so, we may learn more about the groundhog activities such as the time that they are active, which could prove useful for attempting to capture and "relocate" the pests in the future.

# September/October

## Planning

Our initial idea is to create a remote-controlled robot that can direct live video feedback to the controller. We want to drive this robot through the groundhog tunnels at CHS and explore the intricate designs within. We plan to achieve this by controlling motors using a joystick, and some form of screen/camera to see video.  

Our end goal is to get video inside of the tunnels, but really just create a robot that we can control and will give us a live video feed. Our success will be measured by whether or not we can accomplish this goal.

## Initial brainstorming 

https://learn.adafruit.com/ttl-serial-camera/overview

https://learn.adafruit.com/adafruit-2-8-and-3-2-color-tft-touchscreen-breakout-v2

Sample drawings of our chassis featuring a central body and tank treads.

<img src="images/ChasisDrawing.PNG" width="300">

## Materials for the chassis

<img src="images/MetalSheet.jpg" width="200"> <img src="images/WoodSheet.jpg" width="200">

The metal may be more durable but harder to cut and manipulate. And vice versa for the wood. 

# November

### Diagram is drawn by Miller for utilizing the high torque motors / H-bridge (DRV8833)
This diagram shows us how to wire the 2 potential motors we may utilize and it assists us in coding the motors. Motor "A" will connect its power into AOUT1 and ground into AOUT2. Motor "B" will connect its power into BOUT1 and ground into BOUT2. A 9-volt battery will be used to connect to the power/ground slots on the H bridge. AIN1/AIN2 connect the H bridge to GP pins on the pico for Motor A, and BIN1/BIN2 will do the same for Motor B.

<img src="images/MotorDiagram.jpg" width="300">

### Figured out code to move high-torque motors back and forth. 
Currently working on a method to move the motors independently of each other and the computer (Joystick, switch, etc.) We had to workshop the example code we found online using other code in order to be able to use the motors to move back and forth / left and right. We used inspiration from Malachi's old robot arm project with Mariam, where potentiometers were used for stepper motors. 

The robot moves forward when the joystick is at a "Y" value of >19 (the joystick is pushed all the way up) which directs both motors to have values of +1. It moves backward when the joystick has a "Y" value of <1 which directs both motors to have values of -1. The rotation of the robot is created by one motor have a +1 value and the other having a -1 value. 

The joystick at rest is essentially at a graph point of (10,10). Moving it "up" all the way increases the point value to (10,20) / If you move it all the way down it creates a point value of (10,0) and the same for X values. Using this information we coded the joystick/motors to move utilizing said values. 

Here we have the motors moving with example paper wheels.

<img src="images/ezgif.com-crop.gif" width="200">

[Joystick Code](Code/joystick.py)

### Wiring diagram for the joystick 

The wires shown on the diagram are an accurate estimation of how many we will truly need. However, we are not 100% sure of how many wires the LCD screen will require.

<img src="images/updatedwiringdiagramjoystick.png" width="300">


# December

### We have found a camera in the lab and have ordered this LCD screen to hopefully pair the two (99% sure this is the right one)

<img src="images/lcdscreen.png" width="400">


We have decided to use a LoRa board with an extra pico to be able to control the motors wirelessly. We also would like to connect the camera/screen wirelessly with the boards. We have no LoRa experience and may be difficult to pursue our purpose. The LoRa boards connect to one another wirelessly with a radio signal. If we can accomplish this goal, it would require one Pico on the robot with a LoRa module, and another Pico on the remote controller with another LoRa module. 

We have begun to write code for the LoRa boards and tried to make them talk to one another. 

We researched the LoRa boards and brainstormed with our mentors in person on how to move forward in our project. We sat down with them and watched several informative videos regarding Bluetooth, hard wiring, and radio connection. After close research, we have realized that we cannot transmit video from one LoRa board to another. However, we will still try to see if the LoRa modules are feasible to transmit the signal for the joystick/motors. This would minimize the amount of wires needed in regards to connecting the robot to the controller.


# January 

We made a lot of progress in terms of CAD, creating most of what we needed for the final robot. Graham has been working hard and focused on the CAD while I was focused on researching ahead for tasks such as tackling the camera and LCD screen. 

The "Initial Chassis Base" is simply the design for the base of the robot's payload. It has holes extruded to allow for screws to hold other parts in that we print. The "Initial Rough Tread Design" is a rough draft of our ideas for the tank treads. The "Singular Tread" is one of the many identical treads we will print and assemble together using pieces of wire as axles in order to act as proper treads. The "Tread Wheel" is one of the 4 identical wheels we will print to surround the motors. The treads will then surround those wheels to move on uneven terrain. The "Bracket" and "Motor Brackets" are used to hold the motors and the fake motors. Each side of the robot will have one real motor and one fake one which essentially acts as an axle. The "Tread Assembly" shows what the result of assembling all of the singular treads will be. The "Rough Assembly" shows what our base will look like with the wheels on either side.

### Initial Chassis Base - - - - - - - - - - - - - - - - - -Initial Rough Tread Design
<img src="images/chasis.png" width="400">                                  <img src="images/initial design treads.png" width="400">


### Singular Tread - - - - - - - - - - - - - - - - - - - -Tread Wheel 
<img src="images/singletread.png" width="400"> <img src="images/treadwheels.png" width="330">




### Bracket - - - - - - - - - - - - - - - - - - - - - -Motor Bracket
<img src="images/bracket.png" width="360"> <img src="images/motorholder.png" width="400">




### Tread Assembly - - - - - - - - - - - - - - - - -Rough Assembly
<img src="images/treadassembly.png" width="370"> <img src="images/roughassembly.png" width="450">

# February 

We have started printing treads for the robot and researching the camera/LCD screen. Graham printed the little individual tank treads and assembled them using pieces of wire which he cut to act as axles. 

### This week the French people were here in Charlottesville. We got minimal work done during this time.

<img src="images/IMG_5414.JPG" width="400">

Our mentors came and we got feedback from several other UVA students as well. One student proposed the idea of Bluetooth, which we took into consideration, but we still did not believe it would be sufficient for our task at hand. We finalized our idea to fully wire the robot. We also got started on wiring and coding the LCD screen and were directed to focus on that before the camera. 

### 50-foot wire bundle cable 
We ordered 50 feet of wire in a cable that splits off into 8 different wires in order to allow us to use the robot at large distances. We hope to split up these wires for the joystick and whatever other needs we may have in the future. In the event we connect something else to this long strand of wire, we can combine power/ground for each part into one wire apiece. 

<img src="images/50ftwire.png" width="400">

# March


### Graham has started to create the circuit board for the robot 
We are still trying to figure out how many wires we will need exactly for the final design, but for now, we will leave extra space on the circuit board just in case. During this time Malachi is doing research and testing the LCD screen that we purchased online. It is seemingly overcomplicated when it comes to wiring. 

<img src="images/IMG_5102.jpg" width="300">

### Circuit board with battery and one of the motors attached to the laser-cut chassis
The motor is screwed into the laser-cut chassis with printed handles. The next step is to finish assembling the chassis, including incorporating the other motor on the other side, as well as wiring them to the pico.

<img src="images/IMG_5103.jpg" width="300">


# April

Currently testing a different LCD screen that we found in the lab which acts as a shield on a metro express board, struggling to figure out the code. We got the LCD screen to turn on with basic code and continued to print treads and wheels for the robot. By default, LCD screens are a blank white image. 

### We have decided to forget about the LCD screen / Camera and complete the project as just a remote-controlled robot. 

The treads are fully printed and work with both motors to move the chassis in either direction and can rotate. The robot is fully functional now, minus the camera. A video of our robot doing such is below

<img src="images/ezgif.com-optimize.gif" width="400">

# May

### Graham's mom luckily found a cheap endoscope in the Amazon return bins
After this discovery, we are 100% able to have a live video feed on the controller, which allows us to use the robot when the pilot cannot see it. This device turns on to allow us to view an image shown from a 6-foot-long cable. It also features a flashlight which is beneficial for use in dark spaces (such as groundhog tunnels!). 

<img src="images/IMG_5914-ezgif.com-crop.gif" width="400">

After a close inspection of the endoscope, we determined that we could use a few of the remaining wires in the 50-foot cable, and splice some of the endoscope camera wires in order to extend its range. To our surprise, this was a success and the long distance of wire had little effect on video interference. Unfortunately, however, there was one wire too few to connect the camera's flashlight. We will fix this issue by attaching a simple desk-type "lamp" onto the robot which is small enough to make little impact on the weight. 



### Last week of the year

### Updated wiring diagrams

Each lime green star denotes wire that is spliced to be connected to the 50-foot cable of wire. 

<img src="images/copynewupdatedwiringdiagramjoystick.png" width="370"> <img src="images/endoscopewiring.png" width="370">


After presenting, our robot stopped working. After working with Mr. Miller and the voltmeters, we discovered that the H-bridge for the motors was fried. We determined this by testing the voltage of each part of our project and noticing that the A-out / B-out pins on the H-bridge were not receiving power. We replaced the H-bridge and it now works, independent of the computer. 

### Videos of the robot moving back and forth / rotating left/right 
The video appears grainy due to the frame rate and low quality of the gifs

<img src="images/IMG_6020-ezgif.com-optimize.gif" width="400"> <img src="images/IMG6021ezgif.com-optimize.gif" width="370">


### Final images of our robot put together

<img src="images/0417A749-42C0-4F32-86AB-DDC2BC87EEFB.JPG" width="400"> <img src="images/6B119889-926A-4EE0-B02F-B5A751682F0C.jpg" width="400">
<img src="images/784E048F-CDF8-4A06-A291-AE7E9AC5C36A.JPG" width="400"> 
<img src="images/CC8FB4FE-1D89-40C9-B79D-4D55B785BB4D.jpg" width="200"> <img src="images/41C56C78-BC86-44BF-80E6-890C4DBED0A3.JPG" width="400"> 

### Testing our robot inside at a distance

<img src="images/ezgif.com-optimizefinalinsidetest.gif" width="400">

### Official testing

We took the robot outside in search of groundhog holes. One of the first ones we found seemed to be big enough to fit the payload, and this footage shows the video feed from us maneuvering the robot inside the tunnel. The first video shows the initial movement, and the second one shows a slug we discovered. Obstacles inside the tunnels such as large rocks made it difficult to move throughout the tunnel, but we managed. 

<img src="images/videofofintunnel-ezgif.com-optimize.gif" width="400"> <img src="images/slugvideo-ezgif.com-optimize.gif" width="300">

We also decided to do tests of the robot's distance capabilities. We believe it could go much further, however, it is just slow to move with so much wire sent out. The first video shows the robot going out around 20-25 feet. The second video shows the live video feed at said distance. 

<img src="images/distancetest-ezgif.com-optimize.gif" width="300"> <img src="images/cameratest-ezgif.com-optimize.gif" width="400">


# Final reflection

Our project features a controller consisting of a bundle of wires, a joystick controller, and a screen to see a live video feed. The robot which is wired to the controller has a chassis with all of the components attached such as motors with treads to move the robot and the parts needed to control them. There is a flashlight on the robot which is paired with the snake camera from the endoscope. To turn on the camera, hold down the power button on the endoscope. Then you may use the joystick to move in whichever direction desired. The light is turned on by the button on the back of it. After a long year, we concluded our project with the ability to maneuver our robot within the groundhog tunnels with live video feed. Originally our goal was to accomplish just that, which we have. However, we did have some shortcomings. Our time management throughout the year was our biggest issue. We had spurs of efficient time use which were typically when a deadline was approaching. During those times such as the very end of the year, we were very efficient and got a lot of work done. In the last 2 weeks of the year, we made huge strides to finish our project. Another small issue was simplicity. If we had thought ahead to just purchase an endoscope it could have subtracted a month or 2 worth of work. We could have also collaborated more with our mentors, but we did still make good progress with them. It is easy to say we should have done this and that, but we used the knowledge we had and tried to make the smartest decisions for each part of our project. Overall we learned a lot, such as Code/CAD skills, working with a budget, and most importantly, proper time management. 


### Bill of lab materials

-Laser-cut chassis

-3d printed brackets for motors

-2 motors (one on each side of the chassis)

-Laser cut wheels

-3d printed treads/wires used as axles to keep together

-4-40 screws/washers/nuts

-Circuit board

-Raspberry Pi Pico

-Many wires

-Standoffs

-9v battery and holder

-3v lone battery

-H bridge

-Desk lamp

-Endoscope

-Joystick

-50 ft wire bundle

-Duct tape! Astronauts saved their lives on Apollo 13 using duct tape. Who's to say that engineers are above using it? <img src="images/ducttapeapollo.png" width="200">
