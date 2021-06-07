'''
Compute all Strongly Dominant Strategies and Equilibrium
'''
from strategy import l, n
from utility import u
import copy

compare = []
Alist, Blist = [], []
nA, nB = [], []

def CheckForLess(list1, val):
    return(all(x < val for x in list1))

for k in range(n):
    for i, j in zip(l, u):
        if i[k]=='A':
            nA.append('A')
            compare = copy.deepcopy(j)
            compare.remove(j[k])
            val = j[k]
            if (CheckForLess(compare, val)):Alist.append("Yes")
            else: pass

        if i[k]=='B':
            nB.append('B')
            compare = copy.deepcopy(j)
            compare.remove(j[k])
            val = j[k]
            if (CheckForLess(compare, val)):Blist.append("Yes")
            else: pass

    if len(Alist)==len(nA):
        print("Strongly dominant strategy of player {} is A".format(k+1))
    elif len(Blist)==len(nB):
        print("Strongly dominant strategy of player {} is B".format(k+1))
    else:
        print("No Strongly Dominant strategy for player {}".format(k+1))

    Alist, Blist = [], []
    nA, nB = [], []
