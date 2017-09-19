# -*- coding: utf-8 -*-
"""
Created on Tue Sep 19 12:53:02 2017
1D and 2D lists - Stockticker Portfolio
@author: William Neal
"""
player_names = ["Ted","Jed","Ned"]
stocks = ["IBM", "Coca Cola", "BYD", "Alitalia"]
num_players = len(player_names)
num_stocks = len(stocks)
portfolio = [0]*num_players*num_stocks
#Add 30 stocks to the BYD of Ned
stock_number=2
player_number=2
portfolio[(player_number)*num_stocks+stock_number]+=30
print portfolio

print "Let's do this a different way:"
portfolio = [[0 for x in range(num_stocks)] for y in range(num_players)] 
print portfolio
#Add 30 stocks to the BYD of Ned
stock_number=2
player_number=2
portfolio[stock_number][player_number]+=30
portfolio[0][1]+=40

print portfolio

