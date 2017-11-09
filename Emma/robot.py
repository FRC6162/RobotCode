# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 16:13:16 2017

@author: fy
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
        self.robot_drive = wpilib.RobotDrive(0,1)
        self.stick = wpilib.Joystick(1)
        self.switch1 = wpilib.DigitalInput(0)
        self.switch2 = wpilib.DigitalInput(1)
        self.switch3 = wpilib.DigitalInput(2)
        self.switch4 = wpilib.DigitalInput(3)
        self.motor1 = wpilib.VictorSP(4)
        self.motor2 = wpilib.VictorSP(5)
        self.Servo1 = wpilib.Servo(6)
        self.Servo2 = wpilib.Servo(7)
        
            
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
        if self.switch1.get()==True:
            self.motor1.set(self.stick.getRawAxis(1))
            self.Servo1.set(self.stick.getRawAxis(2))
            
        else:
            self.motor1.set(self.stick.getAxis(5))
            self.Servo1.set(self.stick.getAxis(6))
        
        if self.switch2.get()==True:
            self.motor2.set(int(self.stick.getRawButton(1)))
            self.Servo2.set(int(self.stick.getRawButton(2)))
        else:
            self.motor2.set(int(self.stick.getRawButton(3)))
            self.Servo2.set(int(self.stick.getRawButton(4)))

    def testPeriodic(self):
        """This function is called periodically during test mode."""
        wpilib.LiveWindow.run()

if __name__ == "__main__":
    wpilib.run(MyRobot)