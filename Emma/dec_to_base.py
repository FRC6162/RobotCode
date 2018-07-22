#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 31 12:53:22 2017
This program converts numbers from decimal to a specified base
and from that base back to decimal
@author: wneal
"""
from math import *

def letterize(num):
    #Changes a numeric value into a character value
    #Single digits merely become characters
    #Double digit numbers from 10 to 35 are mapped onto 
    #letters of the alphabet
    #Good luck if you try to use a base above 36!!!
    if num < 10:
        return str(num)
    if num >= 10:
        return chr(num+55)


def convert_to_base(number, base):
    #Converts from a decimal number to a specified base
    answer = [] #Initialize the answer list
    while number > 0: #Repeat the process until the number is 0
        #Append the remainder at each step:
        answer.append(letterize(number%base))
        #Divide the number:
        number = int(number/base)
    #Reverse the answer:
    answer.reverse()
    #Convert the answer into a string:
    stringanswer = "" #Initialize a blank string
    for i in range(0,len(answer)):
        stringanswer+=answer[i] #Add each character to the string
    return stringanswer

def convert_to_numbers(num):
    #Converts numeric and alphabetical characters to a numeric integer
    if ord(num)>=48 and ord(num)<=57: #If it is a number
        return ord(num)-48
    if ord(num)>=65 and ord(num)<=90: #If it is a letter
        return ord(num)-55
    
def convert_to_dec(number, base):
    #Takes a number in a base between 2 and 35 and converts to decimal:
    list1 = []
    for i in number:
        list1.append(i)
    list1.reverse()
    #print ("Convert to Dec: ", list1)
    for i in range(0, len(list1)):
        list1[i] = convert_to_numbers(list1[i])
    #print("List1", list1)   
    total = 0
    for i in range(0,len(list1)):
        #print ("Check!:", total, list1[i], base, i)
        total+=list1[i]*base**i
    return total


#Show the conversion functions converting to a base and back:
for i in range(10,4000):
    a = convert_to_base(i,2)
    b = convert_to_dec(a, 2)
    print (i, a, b)
    
       