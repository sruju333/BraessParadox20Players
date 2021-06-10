'''
Compute all Strongly Dominant Strategies and Equilibrium
'''
from strategy import l, n, length
from utility import u
import copy

SDSeq = []

player = []
res = []
fsds = []

#Part 1: Calculating Strongly Dominant Strategies of all Players
def checksublist(plist,p):
    for ele in plist:
        sds, sdu = [], []
        for i,j in zip(l,u):
            L = copy.deepcopy(ele)
            L.insert(p,i[p])
            if L==i:
                sds.append(i[p])
                sdu.append(j[p])

        compare(sds,sdu)

    if (len(fsds)==(length/2)):
        if list(set(fsds))==list('A'):
            SDSeq.append('A')
            print("Strongly Dominant Strategy of Player {} is A".format(p+1))
        elif list(set(fsds))==list('B'):
            SDSeq.append('B')
            print("Strongly Dominant Strategy of Player {} is B".format(p+1))
        else:
            print("Player {} has NO Strongly Dominant Strategy".format(p+1))
    else:
        print("Player {} has NO Strongly Dominant Strategy".format(p+1))


def compare(slist, ulist):
    if ulist[0]>ulist[1]:
        fsds.append(slist[0])
    elif ulist[1]>ulist[0]:
        fsds.append(slist[1])
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
    fsds = []


#Part 2: Printing Strongly Dominant Strategy Equilibrium, if it exists
if not SDSeq:
    print("NO Strongly Dominant Strategy Equilibrium")
else:
    if len(SDSeq)==n:
        print("Strongly Dominant Strategy Equilibrium:", SDSeq)
    else:
        print("NO Strongly Dominant Strategy Equilibrium")
