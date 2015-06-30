# -*- coding: utf-8 -*-
'''
Created on 2012-10-5
@author: Administrator
'''
from collections import defaultdict
import itertools
import time
 
a = [
        [ 0, 7, 0, 0, 0, 0, 0, 0, 0], #0
        [ 5, 0, 3, 0, 0, 6, 0, 0, 0], #1
        [ 0, 6, 2, 0, 8, 0, 7, 0, 0], #2
        #
        [ 0, 0, 0, 3, 0, 2, 0, 5, 0], #3
        [ 0, 0, 4, 0, 1, 0, 3, 0, 0], #4
        [ 0, 2, 0, 9, 0, 5, 0, 0, 0], #5
        #
        [ 0, 0, 1, 0, 3, 0, 5, 9, 0], #6
        [ 0, 0, 0, 4, 0, 0, 6, 0, 3], #7
        [ 0, 0, 0, 0, 0, 0, 0, 2, 0], #8
#        0, 1, 2, 3,|4, 5, 6,|7, 8
     ]
 
 
#a = [
#        [0, 0, 0, 0, 0, 0, 0, 0, 0], #0
#        [0, 0, 0, 0, 0, 0, 0, 0, 0], #1
#        [0, 0, 0, 0, 0, 0, 0, 0, 0], #2
#        #
#        [0, 0, 0, 0, 0, 0, 0, 0, 0], #3
#        [0, 0, 0, 0, 0, 0, 0, 0, 0], #4
#        [0, 0, 0, 0, 0, 0, 0, 0, 0], #5
#        #
#        [0, 0, 0, 0, 0, 0, 0, 0, 0], #6
#        [0, 0, 0, 0, 0, 0, 0, 0, 0], #7
#        [0, 0, 0, 0, 0, 0, 0, 0, 0], #8
##        0, 1, 2, 3,|4, 5, 6,|7, 8
#     ]
 
#===============================================================================
# 得到坐标点和值，相当于稀疏矩阵:(X,Y):value
#===============================================================================
exists_d = dict(((h_idx, y_idx), v) for h_idx, y in enumerate(a) for y_idx , v in enumerate(y)  if v)
 
 
h_exist = defaultdict(dict)
v_exist = defaultdict(dict)
 
for k, v in exists_d.iteritems():
    h_exist[k[ 0]][k[ 1]] = v
    v_exist[k[ 1]][k[ 0]] = v
 
 
permutations = list(itertools.permutations(range(1, 10), 9))
 
h_d = {}
 
now = time.time()
for hk, hv in h_exist.iteritems():
     
    q = filter(lambda x:all((x[k] == v for k, v in hv.iteritems())), permutations)
    w = filter(lambda x:all((x[vk] != v for vk , vv in v_exist.iteritems() for k, v in vv.iteritems() if k != hk)), q)
 
    h_d[hk] = w
     
print time.time() - now 
 
def test(x, y):
    return all((y[i] not in [x_[i] for x_ in x] for i in range(9)))
 
def test2(x):
    return len(set(x)) != 9
 
s = set(range(9))
 
sudokus = []
 
def test3(f, s, t):
    if len(set((f[0], f[1], f[2], s[0], s[1], s[2], t[0], t[1], t[2]))) != 9:
        return 1
    if len(set((f[3], f[4], f[5], s[3], s[4], s[5], t[3], t[4], t[5]))) != 9:
        return 1
    if len(set((f[6], f[7], f[8], s[6], s[7], s[8], t[6], t[7], t[8]))) != 9:
        return 1
    return 0
 
def test4(f, s):
    if len(set((f[0], f[1], f[2], s[0], s[1], s[2]))) != 6:
        return 1
    if len(set((f[3], f[4], f[5], s[3], s[4], s[5]))) != 6:
        return 1
    if len(set((f[6], f[7], f[8], s[6], s[7], s[8]))) != 6:
        return 1
    return 0
 
def solve_sudoku(h_d, h_idx=None, reserves=None, solves=None):
     
    if solves is None:
        solves = []
     
    if h_idx is None :
        h_idx = 0
    for l0 in h_d[h_idx]:
#        print l0
#        print reserves, l0 , h_idx
        if reserves == None:
            _reserves = [l0, ]
            solve_sudoku(h_d, h_idx + 1, _reserves, solves)
        else:
            if not test(reserves, l0):
                continue
            if h_idx in (1 , 4, 7):
                if test4(reserves[h_idx - 1], l0):
                    continue
            elif h_idx in (2, 5, 8) :
                if test3(reserves[h_idx - 2], reserves[h_idx - 1], l0):
                    continue
                     
            _reserves = list(reserves)
            _reserves.append(l0)
            if h_idx < 8:
                solve_sudoku(h_d, h_idx + 1, _reserves, solves)
            if h_idx == 8:
                solves.append(_reserves)
    else:
        if h_idx == 0:
            return solves
                 
 
 
 
if __name__ == '__main__':
#(8, 7, 9, 1, 2, 3, 4, 6, 5)
#(5, 4, 3, 7, 9, 6, 2, 1, 8)
#(1, 6, 2, 5, 8, 4, 7, 3, 9)
#(7, 1, 8, 3, 4, 2, 9, 5, 6)
#(9, 5, 4, 6, 1, 8, 3, 7, 2)
#(3, 2, 6, 9, 7, 5, 8, 4, 1)
#(6, 8, 1, 2, 3, 7, 5, 9, 4)
#(2, 9, 7, 4, 5, 1, 6, 8, 3)
#(4, 3, 5, 8, 6, 9, 1, 2, 7)
 
    now = time.time()
    x = solve_sudoku(h_d)
    for i in x:
        for ii in i:
            print ii
    print time.time() - now
