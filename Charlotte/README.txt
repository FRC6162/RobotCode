This directory contains source code shared at the 2017 SWATPosium Presentation entitled "Cheesecake"
We are actively updating this software with clarifying comments.
Any feedback would be most welcome.

Instructions:

Installation:
(1) The file with the highest number is the most recent
(2) The software is written in Python 3 using the Anaconda / Spyder IDE
(3) The softare requires a working tkinter installation to work properly. Please see online tutorials to properly install tkinter on your system

Operation:
(4) There are several functions on the software.  It is based on a compeitition we had at a summer STEM camp. Students needed to create the best robot climbing 
module design based on a sset of available gears: 0, 1 or 2 planetary gear stages (5:1, 10:1, neither or both) and five available individual gears (72, 54, 40, 24, 18) of which 0, 2 or 4 were to be selected.
The resulting mechanism was to be optimized to allow a robot to climb a rope as quickly as possible. 
(5) Users of the program may calculate one of the following:
(a) The force required to lift an obejct vertically based on its mass
(b) The torque required to roll a rope to which is attached a mass, given the radius of the roller and  the mass of the object
(c) The torque required to lift the object on a rope given several intermediate gear stages.
(d) When entering gear stages, the individual gears are listed in order from the gear attached to the motor to the intermediate gears (if any) to the gear attached to the rolling axle.
(e) For each planetary gear stage used, enter the gear ratio as 5 for 5:1 and 10 for 10:1, etc.
(6) A calculation of the estimated time for a robot to climb the rope given the mass of the robot, the radius of the axle and the gear stages. As of November 6, 2017, only one motor is used in this source code: 775Pro.  Perhaps code for additional motors will be incorporated in the future.
(7) A robot race simulator for three robots.  At the moment valid data for three robot modules must be entered, one for each "Team" If wnay of the specificied gear ratios is not valid, an error will be produced and the robots will not climb.
 

