'''
Compute Utilities of all 20 players
'''
#Part 1: Compute all possible strategy profiles for 20 players and store it in list
import re
import numpy as np
from itertools import product
from math import ceil

strategy_list = ["A", "B"]
cartesian_product = []
length = 0
dict = {}

for ele in range(2): #19
    if ele==0:
        cartesian_product = product(strategy_list,strategy_list)
    else:
        cartesian_product = product(strategy_list, cartesian_product)

cartesian_list = list(cartesian_product)
length = len(cartesian_list)

i = 1
for ele in cartesian_list:
    dict.update({ele:i})
    i += 1

print("Number of Players: {}\nStrategy Set: {}\nTotal Number of Strategy Profiles: {}".format(int(20),set(strategy_list),length))
