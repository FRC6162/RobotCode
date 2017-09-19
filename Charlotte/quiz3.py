#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 11 13:58:50 2017

@author: chenquancheng
"""


import random
num_questions=10
score = 0
for i in range(0,num_questions):
    a = int(random.random()*10)+1
    b = int(random.random()*10)+1
    x = int(random.random()*4)+1
    if x == 1:
        print a, " + ", b
        user_answer = input("Answer here:")
        answer = a + b
        if user_answer == answer:
            print "You are correct!"
            score = score + 1
        else:
            print "Sorry. This is not correct."
    if x == 2:
        print a, " - ", b
        user_answer = input("Answer here:")
        answer = a-b
        if user_answer == answer:
            print "You are correct!"
            score = score + 1
        else:
            print "Sorry. This is not correct."
    if x == 3:
        print a, " * ", b
        user_answer = input("Answer here:")
        answer = a*b
        if user_answer == answer:
            print "You are correct!"
            score = score + 1
        else:
            print "Sorry. This is not correct."
    if x == 4:
        print a*b, " / ", b
        user_answer = input("Answer here(Answer with the largest integer that is less than the actual quotient.):")
        answer = a
        if user_answer == answer:
            print "You are correct!"
            score = score + 1
        else:
            print "Sorry. This is not correct."
print "Your score is: "
print score, " out of ", num_questions, " questions correct."
