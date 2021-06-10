'''
Compute all Weakly Dominant Strategies and Equilibrium
'''
from strategy import l, n, length
from utility import u
import copy

WDSeq = []

player = []
res = []
fwds = []
strict = []
splitA, splitB = [], []
wd = []

#Part 1: Calculating Weakly Dominant Strategies of all Players
def checksublist(plist,p):
    for ele in plist:
        wds, wdu = [], []
        for i,j in zip(l,u):
            L = copy.deepcopy(ele)
            L.insert(p,i[p])
            if L==i:
                wds.append(i[p])
                wdu.append(j[p])

        compare(wds,wdu)
        strictcmp(wds, wdu)

    for ele in fwds:
        if ele=='A':
            splitA.append(ele)
        elif ele=='B':
            splitB.append(ele)

    if (len(splitA)==(length/2)):
        if any(x=='A' for x in strict):
            wd.append('A')

    if (len(splitB)==(length/2)):
        if any(x=='B' for x in strict):
            wd.append('B')

    if not wd:
        print("Player {} has NO Weakly Dominant Strategy".format(p+1))
    else:
        WDSeq.append(wd)
        print("Weakly Dominant Strategy of Player {}: {}".format(p+1,wd))


def compare(slist, ulist):
    if ulist[0]>=ulist[1]:
        fwds.append(slist[0])
    if ulist[1]>=ulist[0]:
        fwds.append(slist[1])

def strictcmp(strlist, utilist):
    if utilist[0]>utilist[1]:
        strict.append(strlist[0])
    elif utilist[1]>utilist[0]:
        strict.append(strlist[1])
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
    fwds = []


#Part 2: Printing Weakly Dominant Strategy Equilibrium, if it exists
EQ = []
if not WDSeq:
    print("NO Weakly Dominant Strategy Equilibrium")
else:
    print("Weakly Dominant Strategy Equilibria: ")
    
