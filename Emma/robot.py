# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 16:13:16 2017

@author: fy
"""

#!/usr/bin/env python3
"""
    This is a good foundation to build your robot code on
"""
from networktables import NetworkTables
sd = NetworkTables.getTable('SmartDashboard')
import wpilib
#From networktables import NetworkTables
#wpilib: contains many classes and functions
#for programming FRC robots.
#wpilib.IterativeRobot:
import hal
import threading
from ._impl.utils import match_arglist, HasAttribute
from .sendablebuilder import SendableBuilder

__all__ = ["SmartDashboard"]
class Data:
    def __init__(self, sendable):
        self.sendable = sendable
        self.builder = SendableBuilder()

class SmartDashboard:
    """The bridge between robot programs and the SmartDashboard on the laptop

    When a value is put into the SmartDashboard, it pops up on the
    SmartDashboard on the remote host. Users can put values into and get values
    from the SmartDashboard.
    
    These values can also be accessed by a NetworkTables client via the
    'SmartDashboard' table::
    
        from networktables import NetworkTables
        sd = NetworkTables.getTable('SmartDashboard')
        
        # sd.putXXX and sd.getXXX work as expected here
    
    """
    # The NetworkTable used by SmartDashboard
    table = None
    # A table linking tables in the SmartDashboard to the SmartDashboardData
    # objects they came from.
    tablesToData = {}
    mutex = threading.RLock()
    def getTable(cls):
        if cls.table is None:
            from networktables import NetworkTables
            cls.table = NetworkTables.getTable("SmartDashboard")
            hal.report(hal.UsageReporting.kResourceType_SmartDashboard,
                       hal.UsageReporting.kSmartDashboard_Instance)
        return cls.table
    def putData(cls, *args, **kwargs):
        """
        Maps the specified key (name of the :class:`.Sendable` if not provided) 
        to the specified value in this table.
        The value can be retrieved by calling the get method with a key that
        is equal to the original key.

        Two argument formats are supported: 
        
        - key, data
        - value
        
        :param key: the key (cannot be None)
        :type  key: str
        :param data: the value
        :type data: :class:`.Sendable`
        :param value: the value
        :type value: :class:`.Sendable`
        """
        with cls.mutex:
            key_arg = ("key", [str])
            data_arg = ("data", [HasAttribute("initSendable")])
            value_arg = ("value", [HasAttribute("initSendable")])
            templates = [[key_arg, data_arg],
                         [value_arg],]

            index, results = match_arglist('SmartDashboard.putData',
                                       args, kwargs, templates)
            if index == 0:
                key = results['key']
                data = results["data"]
            elif index == 1:
                data = results["value"]
                key = data.getName()
            else:
                raise ValueError("only (key, data) or (value) accepted")

            sddata = cls.tablesToData.get(key, None)
            if sddata is None or sddata.sendable != data:
                if sddata is not None:
                    sddata.builder.stopListeners()

                sddata = Data(data)
                cls.tablesToData[key] = sddata
                dataTable = cls.getTable().getSubTable(key)
                sddata.builder.setTable(dataTable)
                data.initSendable(sddata.builder)
                sddata.builder.updateTable()
                sddata.builder.startListeners()
                dataTable.getEntry('.name').setString(key)            
        if data is None:
            raise KeyError("SmartDashboard data does not exist: '%s'" % key)
        return data.sendable
    def getEntry(cls, key):
        """Gets the entry for the specified key.
        
        :param key: the key name
        :rtype: :class:`.NetworkTableEntry`
        """
        table = cls.getTable()
        return table.getEntry(key)
    def containsKey(cls, key):
        """Checks the table and tells if it contains the specified key.

        :param key: key the key to search for
        
        :returns: true if the table as a value assigned to the given key
        """
        table = cls.getTable()
        return table.containsKey(key)
    def getKeys(cls, types=0):
        """Get the keys stored in the SmartDashboard table of NetworkTables.

        :param types: bitmask of types; 0 is treated as a "don't care".
        
        :returns: keys currently in the table
        """
        table = cls.getTable()
        return table.getKeys(types)
    def setPersistent(cls, key):
        """Makes a key's value persistent through program restarts.
        The key cannot be null.

        :param key: the key name
        """
        table = cls.getTable()
        table.setPersistent(key)
    def clearPersistent(cls, key):
        """Stop making a key's value persistent through program restarts.
        The key cannot be null.

        :param key: the key name
        """
        table = cls.getTable()
        table.clearPersistent(key)
    def isPersistent(cls, key):
        """Returns whether the value is persistent through program restarts.
        The key cannot be null.

        :param key: the key name
        
        :returns: True if the value is persistent.
        """
        table = cls.getTable()
        return table.isPersistent(key)
    def setFlags(cls, key, flags):
        """Sets flags on the specified key in this table. The key can
        not be null.

        :param key: the key name
        :param flags: the flags to set (bitmask)
        """
        table = cls.getTable()
        table.setFlags(key, flags)
    def clearFlags(cls, key, flags):
        """Clears flags on the specified key in this table. The key can
        not be null.

        :param key: the key name
        :param flags: the flags to clear (bitmask)
        """
        table = cls.getTable()
        table.clearFlags(key, flags)
    def getFlags(cls, key):
        """ Returns the flags for the specified key.

        :param key: the key name
        
        :returns: the flags, or 0 if the key is not defined
        """
        table = cls.getTable()
        return table.getFlags(key)
    def delete(cls, key):
        """Deletes the specified key in this table. The key can
        not be null.

        :param key: the key name
        """
        table = cls.getTable()
        table.delete(key)
    def putBoolean(cls, key, value):
        """Put a boolean in the table.

        :param key: the key to be assigned to
        :param value: the value that will be assigned
        
        :return False if the table key already exists with a different type
        """
        table = cls.getTable()
        return table.putBoolean(key, value)
    def setDefaultBoolean(cls, key, defaultValue):
        """Gets the current value in the table, setting it if it does not exist.
        
        :param key: the key
        :param defaultValue: the default value to set if key doens't exist.
        
        :returns: False if the table key exists with a different type
        """
        table = cls.getTable()
        return table.setDefaultBoolean(key, defaultValue)
    def getBoolean(cls, key, defaultValue):
        """Returns the boolean the key maps to. If the key does not exist or is of
        different type, it will return the default value.
        
        :param key: the key to look up
        :type  key: str
        :param defaultValue: returned if the key doesn't exist
        
        :returns: the value associated with the given key or the given default value
                  if there is no value associated with the key
        """
        table = cls.getTable()
        return table.getBoolean(key, defaultValue)
    def putNumber(cls, key, value):
        """Put a number in the table.
        
        :param key: the key to be assigned to
        :param value: the value that will be assigned
        
        :returns: False if the table key already exists with a different type
        """
        table = cls.getTable()
        return table.putNumber(key, value)
    def setDefaultNumber(cls, key, defaultValue):
        """Gets the current value in the table, setting it if it does not exist.
        
        :param key: the key
        :param defaultValue: the default value to set if key doens't exist.
        
        :returns: False if the table key exists with a different type
        """
        table = cls.getTable()
        return table.setDefaultNumber(key, defaultValue)
    def getNumber(cls, key, defaultValue):
        """Returns the number the key maps to. If the key does not exist or is of
        different type, it will return the default value.
        
        :param key: the key to look up
        :type  key: str
        :param defaultValue: returned if the key doesn't exist
        
        :returns: the value associated with the given key or the given default value
                  if there is no value associated with the key
        """
        table = cls.getTable()
        return table.getNumber(key, defaultValue)
    def putString(cls, key, value):
        """Put a string in the table.
        
        :param key: the key to be assigned to
        :param value: the value that will be assigned
        
        :returns: False if the table key already exists with a different type
        """
        table = cls.getTable()
        return table.putString(key, value)
    def setDefaultString(cls, key, defaultValue):
        """Gets the current value in the table, setting it if it does not exist.
        
        :param key: the key
        :param defaultValue: the default value to set if key doens't exist.
        
        :returns: False if the table key exists with a different type
        """
        table = cls.getTable()
        return table.setDefaultString(key, defaultValue)
    def getString(cls, key, defaultValue):
        """Returns the string the key maps to. If the key does not exist or is of
        different type, it will return the default value.
        
        :param key: the key to look up
        :type  key: str
        :param defaultValue: returned if the key doesn't exist
        
        :returns: the value associated with the given key or the given default value
                  if there is no value associated with the key
        """
        table = cls.getTable()
        return table.getString(key, defaultValue)
    def putBooleanArray(cls, key, value):
        """Put a boolean array in the table.
        
        :param key: the key to be assigned to
        :param value: the value that will be assigned
        
        :returns: False if the table key already exists with a different type
        """
        table = cls.getTable()
        return table.putBooleanArray(key, value)
    def setDefaultBooleanArray(cls, key, defaultValue):
        """Gets the current value in the table, setting it if it does not exist.
        
        :param key: the key
        :param defaultValue: the default value to set if key doens't exist.
        
        :returns: False if the table key exists with a different type
        """
        table = cls.getTable()
        return table.setDefaultBooleanArray(key, defaultValue)
    def getBooleanArray(cls, key, defaultValue):
        """Returns the boolean array the key maps to. If the key does not exist or is of
        different type, it will return the default value.
        
        :param key: the key to look up
        :type  key: str
        :param defaultValue: returned if the key doesn't exist
        
        :returns: the value associated with the given key or the given default value
                  if there is no value associated with the key
        """
        table = cls.getTable()
        return table.getBooleanArray(key, defaultValue)
    def putNumberArray(cls, key, value):
        """Put a number array in the table.
        
        :param key: the key to be assigned to
        :param value: the value that will be assigned
        
        :returns: False if the table key already exists with a different type
        """
        table = cls.getTable()
        return table.putNumberArray(key, value)
    def setDefaultNumberArray(cls, key, defaultValue):
        """Gets the current value in the table, setting it if it does not exist.
        
        :param key: the key
        :param defaultValue: the default value to set if key doens't exist.
        
        :returns: False if the table key exists with a different type
        """
        table = cls.getTable()
        return table.setDefaultNumberArray(key, defaultValue)
    def getNumberArray(cls, key, defaultValue):
        """Returns the number array the key maps to. If the key does not exist or is of
        different type, it will return the default value.

        :param key: the key to look up
        :type  key: str
        :param defaultValue: returned if the key doesn't exist
        
        :returns: the value associated with the given key or the given default value
                  if there is no value associated with the key
        """
        table = cls.getTable()
        return table.getNumberArray(key, defaultValue)
    def putStringArray(cls, key, value):
        """Put a string array in the table
        
        :param key: the key to be assigned to
        :type key: str
        :param value: the value that will be assigned
        :type value: list(str)
        
        :returns: False if the table key already exists with a different type
        :rtype: bool
        """
        table = cls.getTable()
        return table.putStringArray(key, value)
    def setDefaultStringArray(cls, key, defaultValue):
        """If the key doesn't currently exist, then the specified value will
        be assigned to the key.
        
        :param key: the key to be assigned to
        :type key: str
        :param defaultValue: the default value to set if key doesn't exist.
        :type defaultValue: list(str)
        
        :returns: False if the table key exists with a different type
        :rtype: bool
        """
        table = cls.getTable()
        return table.setDefaultStringArray(key, defaultValue)
    def getStringArray(cls, key, defaultValue):
        """Returns the string array the key maps to. If the key does not exist or is
        of different type, it will return the default value.
        
        :param key: the key to look up
        :type key: str
        :param defaultValue: the value to be returned if no value is found
        :type defaultValue: list(str)
        
        :returns: the value associated with the given key or the given default value
                  if there is no value associated with the key
        :rtype: list(str)
        """
        table = cls.getTable()
        return table.getStringArray(key, defaultValue)
    def putRaw(cls, key, value):
        """Put a raw value (byte array) in the table.
        
        :param key: the key to be assigned to
        :param value: the value that will be assigned
        
        :returns: False if the table key already exists with a different type
        """
        table = cls.getTable()
        return table.putRaw(key, value)
    def setDefaultRaw(cls, key, defaultValue):
        """Gets the current value in the table, setting it if it does not exist.
        
        :param key: the key
        :param defaultValue: the default value to set if key doens't exist.
        
        :returns: False if the table key exists with a different type
        """
        table = cls.getTable()
        return table.setDefaultRaw(key, defaultValue)    
    def getRaw(cls, key, defaultValue):
        """Returns the raw value (byte array) the key maps to. If the key does not exist or is of
        different type, it will return the default value.

        :param key: the key to look up
        :type  key: str
        :param defaultValue: returned if the key doesn't exist
        
        :returns: the value associated with the given key or the given default value
                  if there is no value associated with the key
        """
        table = cls.getTable()
        return table.getRaw(key, defaultValue)    
    def updateValues(cls):
        with cls.mutex:
            for data in cls.tablesToData.values():
                data.builder.updateTable()


class MyRobot(wpilib.IterativeRobot):#Builds on a base class

    def robotInit(self):#This is a function or method
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
        self.camera1 =  wpilib.CameraServer.launch('vision.py:main')
        
            
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