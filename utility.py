'''
Compute Utilities of all 20 players
'''
#Part 1: Compute all possible strategy profiles for 20 players and store it in list
import re
from itertools import product

strategy_list = ["A", "B"]
cartesian_product = []
length = 0

for ele in range(4): #19
    if ele==0:
        cartesian_product = product(strategy_list,strategy_list)
    else:
        cartesian_product = product(strategy_list, cartesian_product)

cartesian_list = list(cartesian_product)
length = len(cartesian_list)

print("Number of Players: {}\nStrategy Set: {}\nTotal Number of Strategy Profiles: {}".format(int(20),set(strategy_list),length))


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
    if count%5==0: #20
        l.append(newL)
        newL = []


#Part 3: Writing all strategy profile to a text file
file = open("Braess20Players.txt", "w")

for ele in l:
    file.write(str(ele))
    file.write("\n")

file.close()
