'''
Compute all Strategy Profiles for 20 players
'''
#Part 1: Compute all possible strategy profiles for 20 players and store it in list
import re
from itertools import product

strategy_list = ["A", "B"]
cartesian_product = []
length = 0
n = 4

for ele in range(n-1): #19
    if ele==0:
        cartesian_product = product(strategy_list,strategy_list)
    else:
        cartesian_product = product(strategy_list, cartesian_product)

cartesian_list = list(cartesian_product)
length = len(cartesian_list)

print("Number of Players: {}\nStrategy Set: {}\nTotal Number of Strategy Profiles: {}".format(int(n),set(strategy_list),length))


#Part 2: Data processing
x  = re.sub('[()]', '', str(cartesian_list))
x = x.replace("[","")
x = x.replace("]","")

L = []
for ele in x:
    if (ele=='A' or ele=='B'):
        L.append(ele)

count = 0
newL = []
l = []
for ele in L:
    count += 1
    newL.append(ele)
    if count%n==0: #20
        l.append(newL)
        newL = []
