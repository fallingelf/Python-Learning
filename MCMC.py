#!/usr/bin/env python
# -*- coding: utf-8 -*-

#MCMC sampling algrithm：已知分布概率，求处于此分布之下的状态链
import numpy as np
import random

def MCMC(p,q,initial_state,num_shift):
    state = []
    s=initial_state
    state.append(s)
    for i in range(0,num_shift):
        u = random.random()
        if u <=q[s-1,0]:
            t=1
        elif q[s-1,0]<u<=q[s-1,0]+q[s-1,1]:
            t=2
        else:
            t=3                                                                        #下一时刻采样结果
        u = random.random()
        if u>=p[t-1]*q[t-1,s-1]:                                              #转移接受率
            t=s
        state.append(t)
        s=t
    return state

if __name__=='__main__':
    q=np.mat([[0.6,0.2,0.2],[0.5,0.4,0.1],[0.2,0.3,0.5]])                    #任意的马氏转移矩阵
    p=[0.286,0.489,0.225]                                                                #平衡概率分布，即目标分布给出，求满足此的状态链
    shift_stain=MCMC(p,q,1,100000)
    shift_stain=shift_stain[int(len(shift_stain)/2):len(shift_stain)]    #忽略链前部分状态处于搜寻阶段的数据
    wgt_1 = shift_stain.count(1)/len(shift_stain)
    wgt_2 = shift_stain.count(2)/len(shift_stain)
    wgt_3 = shift_stain.count(3)/len(shift_stain)
    print(wgt_1,wgt_2,wgt_3)