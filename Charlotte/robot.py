#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 17 16:31:49 2017

@author: chenquancheng
"""

#!/usr/bin/env python3
"""
    This is a good foundation to build your robot code on
"""

import wpilib

class MyRobot(wpilib.IterativeRobot):

    def robotInit(self):
        """
        This function is called upon program startup and
        should be used for any initialization code.
        """
        self.robot_drive = wpilib.RobotDrive(0,1,2,3)
        self.stick = wpilib.Joystick(1)
        self.Motor1 = wpilib.VictorSP(4)
        self.Motor2 = wpilib.VictorSP(5)
        self.Switch1 = wpilib.DigitalInput(0)
        self.Switch2 = wpilib.DigitalInput(1)
        self.Servo1 = wpilib.Servo(6)
        self.Servo2 = wpilib.Servo(7)
        self.robot_drive = wpilib.RobotDrive(0,True)

    def autonomousInit(self):
        """This function is run once each time the robot enters autonomous mode."""
        self.auto_loop_counter = 0

    def autonomousPeriodic(self):
        """This function is called periodically during autonomous."""

        # Check if we've completed 100 loops (approximately 2 seconds)
        if self.auto_loop_counter < 100:
            self.robot_drive.drive(-0.5, 0) # Drive forwards at half speed
            self.auto_loop_counter += 1
        else:
            self.robot_drive.drive(0, 0)    #Stop robot

    def teleopPeriodic(self):
        """This function is called periodically during operator control."""
        self.robot_drive.arcadeDrive(self.stick)
        if self.stick.getRawButton()==True:
            self.Motor1.set(self.stick.getRawAxis(1))   #This number ranges from -1 to 1-fully reverse to fully forward
            self.Servo1.set(self.stick.getRawAxis(2)) #This number ranges from 0 to 1-fully left to fullt right
        else:
            self.Motor1.set(self.stick.getRawAxis(3))
            self.Servo1.set(self.stick.getRawAxis(4))
        if self.Switch2.get()==True:
            self.Motor2.set(self.stick.getRawAxis(5))
            self.Servo2.set(self.stick.getRawAxis(6))
        else:
            self.Motor2.set(0)
            self.Servo2.set(0)

    def testPeriodic(self):
        """This function is called periodically during test mode."""
        wpilib.LiveWindow.run()

if __name__ == "__main__":
    wpilib.run(MyRobot)