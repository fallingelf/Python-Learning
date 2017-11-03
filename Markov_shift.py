#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Markov process:已知马氏转移矩阵，求状态的分布
import numpy as np
import random

def Markov(P,initial_state,num_shift):                 #马氏链转移模块
    state = []                                                            #状态序列
    s=initial_state                                                   #初始状态
    for i in range(0,num_shift):
        state.append(s)
        u = random.random()                                  #随机数用于决定跳转状态
        if u <=P[s-1,0]:
            s=1
        elif P[s-1,0]<u<=P[s-1,0]+P[s-1,1]:
            s=2
        else:
            s=3
    return state

if __name__=='__main__':
    P=np.mat([[0.65,0.28,0.07],[0.15,0.67,0.18],[0.12,0.36,0.52]])                   #转移矩阵
    shift_stain=Markov(P,1,10000)                                                                  #马氏链初始化
    wgt_1=shift_stain.count(1)/len(shift_stain)                                                #各个状态在链中的比重
    wgt_2 = shift_stain.count(2)/len(shift_stain)
    wgt_3 = shift_stain.count(3)/len(shift_stain)
    print(wgt_1,wgt_2,wgt_3)