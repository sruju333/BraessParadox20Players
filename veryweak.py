'''
Compute all Very Weakly Dominant Strategies and Equilibrium
'''
from strategy import l, n, length
from utility import u
import copy
import itertools

VWDSeq = []

player = []
res = []
fvwds = []
splitA, splitB = [], []
vwd = []

#Part 1: Calculating Very Weakly Dominant Strategies of all Players
def checksublist(plist,p):
    for ele in plist:
        vwds, vwdu = [], []
        for i,j in zip(l,u):
            L = copy.deepcopy(ele)
            L.insert(p,i[p])
            if L==i:
                vwds.append(i[p])
                vwdu.append(j[p])

        compare(vwds,vwdu)

    for ele in fvwds:
        if ele=='A':
            splitA.append(ele)
        elif ele=='B':
            splitB.append(ele)

    if (len(splitA)==(length/2)):
        vwd.append('A')

    if (len(splitB)==(length/2)):
        vwd.append('B')

    if not vwd:
        print("Player {} has NO Very Weakly Dominant Strategy".format(p+1))
    else:
        VWDSeq.append(vwd)
        print("Very Weakly Dominant Strategy of Player {}: {}".format(p+1,vwd))


def compare(slist, ulist):
    if ulist[0]>=ulist[1]:
        fvwds.append(slist[0])
    if ulist[1]>=ulist[0]:
        fvwds.append(slist[1])


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
    fvwds = []


#Part 2: Printing Very Weakly Dominant Strategy Equilibrium, if it exists
if not VWDSeq:
    print("NO Very Weakly Dominant Strategy Equilibrium")
else:
    print("Very Weakly Dominant Strategy Equilibria: ")
    all_possibility = list(itertools.product(*VWDSeq))
    print(all_possibility)
