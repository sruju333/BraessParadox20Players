'''
Computing all pure strategy Nash Equilibria
'''
from strategy import l, n, length
from utility import u
import copy
import numpy as np

player = []
res = []
nash = []
nashEq = []

#Part 1: Calculating Best Response Correspondence of all Players
def checksublist(plist,p):
    for ele in plist:
        strat, uti = [], []
        for i,j in zip(l,u):
            L = copy.deepcopy(ele)
            L.insert(p,i[p])
            if L==i:
                strat.append(i[p])
                uti.append(j[p])

        compare(strat,uti)

    nashEq.append(nash)


def compare(slist, ulist):
    if ulist[0]>ulist[1]:
        nash.append(slist[0])
    elif ulist[1]>ulist[0]:
        nash.append(slist[1])
    else:
        pass


for k in range(n):
    chk = 0
    for i, j in zip(l, u):
        for chk in range(n):
            if chk==k:
                copyi = copy.deepcopy(i)
                copyi.remove(i[chk])
                copyj = copy.deepcopy(j)
                copyj.remove(j[chk])

        player.append(tuple(copyi))

    player = list(set(player))
    res = [list(ele) for ele in player]

    checksublist(res,k)

    player = []
    res = []
    nash = []


#Part 2: Finding all pure strategy Nash Equilibria, if they exist
nashEq = np.array(nashEq)
nashEq = np.transpose(nashEq)
EQ = []
print(nashEq)

if nashEq.size==0:
    print("NO Pure Strategy Nash Equilibrium")
else:
    if np.all(nashEq == nashEq[0]):
        print("Nash Equilibrium:", nashEq[0])
    else:
        for ele in nashEq:
            if len(set(ele)) == 1:
                EQ.append(list(ele))
        if not EQ:
            print("NO Pure Strategy Nash Equilibrium")
        else:
            print("All Pure Strategy Nash Equilibria:", EQ)
