'''
Calculate Utility/Outcome corresponding to all Strategy Profiles
'''
from strategy import l

#Part 1: Calculating utility
u = []
sub = []
nA = 0
nB = 0

for ele in l:
    for element in ele:
        if element=='A':
            nA += 1
        elif element=='B':
            nB +=1
        else:
            pass

    #Calculating utility for each strategy profile
    for element in ele:
        if element=='A':
            payoff = (-25 - (nA/50))
            sub.append(payoff)
        elif element=='B':
            payoff = (-25 -(nB/50))
            sub.append(payoff)

    u.append(sub)
    sub = []
    nA, nB = 0, 0


#Part 2: Writing all strategy profile and utilities to a text file
output = []

for (item1, item2) in zip(l, u):
    output.append(str(item1)+ " - " +str(item2))

file = open("Braess20Players.txt", "w")

for op in output:
    file.write(str(op))
    file.write("\n")

file.close()
