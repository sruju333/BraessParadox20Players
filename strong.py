'''
Compute all Strongly Dominant Strategies and Equilibrium
'''
from strategy import l, n
from utility import u
import copy

copyi, copyj = [], []
comparei, comparej = [], []
appi, appj = [], []
val = 0

def check(list1, list2,chk):
    for i, j in zip(l,u):
        res = checksublist(i,list1)
        if res:
            comparei = copy.deepcopy(i)
            comparei = [z for z in comparei if not z in list1 or list1.remove(z)]
            appi.append(comparei[0])
            comparej = copy.deepcopy(j)
            comparej = [z for z in comparej if not z in list2 or list2.remove(z)]
            appj.append(comparej[0])

    val = compare(appi, appj)

    if val==0:
        print("Player {} has NO Strongly Dominant Strategy".format(chk+1))
    else:
        print("Strongly Dominant Strategy of Player {} is {}".format(chk+1, val))

def checksublist(lis1, lis2):
    i,j = 0,0
    while i < len(lis1) and j < len(lis2):
        if lis1[i] == lis2[j]:
            j += 1
        i += 1

    has_as_subset = (j == len(lis2))
    return has_as_subset


def compare(l1, l2):
    if l2[0][0]>l2[1][0]:
        return l1[0][0]
    elif l2[1][0]>l2[0][0]:
        return l1[1][0]
    else:
        pass


for k in range(n):
    for i, j in zip(l, u):
        for chk in range(n):
            if chk==k:
                copyi = copy.deepcopy(i)
                copyi.remove(i[chk])
                copyj = copy.deepcopy(j)
                copyj.remove(j[chk])
                check(copyi,copyj,chk)
