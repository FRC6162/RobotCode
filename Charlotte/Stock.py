#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 12 13:17:47 2017

@author: chenquancheng
"""
#Stock Ticker - Basic Program - Nested Loops
import random
player_names = []
stock_names = ["Apple","BMO","Ford","Microsoft","Google"]
stock_prices = [100,100,100,100,100]
portfolio = []
money=[]
winners = []
num_players = input("How many players are there?")
print "Please input players' names here one by one."
for i in range(0,num_players):
    player_names.append(raw_input())
    money.append(5000)
    for m in range(0,len(stock_names)):
        portfolio.append(0)
num_rounds = input("How many rounds would you like to have?")
for round in range(0,num_rounds):
    print "It is round ", round+1
    for i in range(0,len(stock_prices)):
        stock_prices[i] += int(211*random.random())-105
    for player in range(0,len(player_names)):
        print player_names[player], ",it is your turn."
        for stock in range(0,len(stock_names)):
            if random.random() < 0.2 and stock_prices[stock] > 0 and stock_prices[stock] < 200 and round != 0:
                percentage = int(20*random.random()+1)
                print "If you have",stock_names[stock],",you get a dividend of ", percentage,"% for ",stock_names[stock]
                money[player] += stock_prices[stock]*portfolio[player*5+stock-1]*percentage/100.0
            if stock_prices[stock] < 0:
                portfolio[player*5+stock-1] = 0
            if stock_prices[stock] > 200:
                portfolio[player*5+stock-1] = portfolio[player*5+stock-1]*2
                stock_prices[stock] = 100
        answer = ""
        while answer != "F":
            print "You have",money[player],"CAD now"
            answer = raw_input("Would you like to buy,to sell,or to finish your turn? You can type 'B' for buy, 'S' for sell, and F to finish your turn.")
            if answer == "B":
                for b in  range(0,len(stock_names)):
                    print b+1,stock_names[b],"$",stock_prices[b]
                stock_number = input("Which stock would you like to buy(Type 1 - 5)?") 
                print "You can afford",int(money[player]/stock_prices[stock_number-1]),"shares of",stock_names[stock_number-1]
                num = input("How much would you like to buy?")
                money[player] -= (stock_prices[stock_number-1])*num
                portfolio[player*len(stock_names)+stock_number-1] += num
                for i in range(player*len(stock_names),player*len(stock_names)+len(stock_names)):
                    print "You have",portfolio[i],"shares of",stock_names[i%5]
            if answer == "S":
                for b in  range(0,len(stock_names)):
                    print b+1,stock_names[b],"$",stock_prices[b]
                for i in range(player*len(stock_names),player*len(stock_names)+len(stock_names)):
                    print "You have",portfolio[i],"shares of",stock_names[i%5]
                stock_number = input("Which stock would you like to sell(Type 1 - 5)?")
                num = input("How much would you like to sell?")
                money[player] += (stock_prices[stock_number-1])*num
                portfolio[player*len(stock_names)+stock_number-1] -= num
                for i in range(player*len(stock_names),player*len(stock_names)+len(stock_names)):
                    print "You have",portfolio[i],"shares of",stock_names[i%5] 
for i in range(0,len(stock_prices)):   
    stock_prices[i] += int(211*random.random())-105
for i in range(0,num_players):
    sum = 0
    for m in range(i*len(stock_names),i*len(stock_names)+len(stock_names)):
        sum += portfolio[m]*stock_prices[m%len(stock_names)]
    money[i] += sum
print "Now the stock prices are: \n 1- Apple $",stock_prices[0],"\n 2- BMO $",stock_prices[1],"\n 3- Ford $",stock_prices[2],"\n 4- Micorsoft $",stock_prices[3], "\n 5- Google $",stock_prices[4]
max = 0
for i in range(0,num_players):
    print player_names[i],",You have",money[i],"CAD"
    if(money[i] > max):
        max = money[i]
        winner = player_names[i]
for i in range(0,num_players):
    if(money[i] == max):
        winners.append(player_names[i])
for m in range(0,len(winners)):
    print winners[m]
print "You are the winner(s)"

    
                    
        
        


