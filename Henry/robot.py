#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  5 15:51:40 2017

@author: chenquancheng
"""

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
        self.stick = wpilib.Joystick(0)
        self.Motor1 = wpilib.VictorSP(4)
        self.Motor2 = wpilib.VictorSP(5)
        self.Switch1 = wpilib.DigitalInput(0)
        self.Switch2 = wpilib.DigitalInput(1)
        self.Servo1 = wpilib.Servo(6)
        self.Servo2 = wpilib.Servo(7)
    
    def Power(x,y):
        return y
    
    def Curve(x,y):
        return x
        
        

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
        self.robot_drive.setInvertedMotor(0,True)
        self.robot_drive.setInvertedMotor(1,True)
        self.robot_drive.setInvertedMotor(2,True)
        self.robot_drive.setInvertedMotor(3,True)
        self.x=self.stick.getRawAxis(0)
        self.y=self.stick.getRawAxis(1)
        self.power = self.Power(self.x,self.y)
        self.curve = self.Curve(self.x,self.y)
        #self.robot_drive.arcadeDrive(self.stick)
        self.robot_drive.drive(self.power, self.curve)
        if self.stick.getRawButton(1)==True:
            self.Motor1.set(-1)
        if self.stick.getRawButton(2)==True:
            self.Motor1.set(0.5)
        if self.stick.getRawButton(1)==False and self.stick.getRawButton(2)==False:
            self.Motor1.set(0)
            #This number ranges from -1 to 1-fully reverse to fully forward
            #self.Servo1.set(0.8) #This number ranges from 0 to 1-fully left to fullt right
        if self.Switch1.get() == True:
            if self.stick.getRawButton(3)==True:
                self.Motor2.set(-1)
            if self.stick.getRawButton(4)==True:
                self.Motor2.set(0.5)
            if self.stick.getRawButton(3)==False and self.stick.getRawButton(4)==False:
                self.Motor2.set(0)
                #This number ranges from -1 to 1-fully reverse to fully forward
       

    def testPeriodic(self):
        """This function is called periodically during test mode."""
        wpilib.LiveWindow.run()

if __name__ == "__main__":
    wpilib.run(MyRobot)