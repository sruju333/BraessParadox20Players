'''
Compute Maxmin Values and Maxmin Strategies of all Players
'''
from strategy import l, n, length
from utility import u
import copy

player = []
res = []
_minu, _mins = [], []
maxu = 0

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

    maxs = []
    maxu = max(_minu)
    for i, j in zip(_minu, _mins):
        if i==maxu:
            maxs.append(j)

    #Printing maxmin value and strategy of each player
    print("Player {} Maxmin Value: {}".format(p+1,maxu))
    print("Player {} Maxmin Strategy: {}".format(p+1,set(maxs)))


def compare(slist, ulist):
    if ulist[0]<ulist[1]:
        _minu.append(ulist[0])
        _mins.append(slist[0])
    elif ulist[1]<ulist[0]:
        _minu.append(ulist[1])
        _mins.append(slist[1])
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
