'''
Compute all Minmax Values and Minmax Strategy Profiles against each player.
'''
from strategy import l, n, length
from utility import u
import copy

player = []
res = []
minu = 0
_maxu, _maxs = [], []
M = []

#Part 1: Calculating Minmax Value and Strategy of all Players
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

    mins = []
    minu = min(_maxu)
    for i, j in zip(_maxu, _maxs):
        if i==minu:
            mins.append(j)

    print("Player {} Minmax Value: {}".format(p+1,minu))
    print("Player {} Minmax Strategy: {}".format(p+1,mins))
    M.append(mins)


def compare(slist, ulist):
    if ulist[0]>ulist[1]:
        _maxu.append(ulist[0])
        _maxs.append(slist[0])
    elif ulist[1]>ulist[0]:
        _maxu.append(ulist[1])
        _maxs.append(slist[1])
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
    _maxu, _maxs = [], []
