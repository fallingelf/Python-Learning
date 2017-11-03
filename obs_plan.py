#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import re

def readlog(obs_log):
    T=[];R=[];X=[]
    obs_log = open(obs_log, 'r')
    logterms = obs_log.readlines()
    for term in logterms:
        # print(term)
        if term[0] == '#':
            # print('this is #')
            continue
        elif term[0] == 'R':
            R.append(int(term[2:4]) + float(term[5:7]) / 60)
            R.append(int(term[8:10]) + float(term[11:13]) / 60)
        elif term[0] == 'S':
            S = re.findall(re.compile(r'S=(\S+)'), term)
            for str in term.split():
                if str[0] == 'T':
                    T.append(int(str[1]))
                    T.append(int(str[3:5]) + float(str[6:8]) / 60)
                    T.append(int(str[9:11]) + float(str[12:14]) / 60)
                elif str[0] == '?':
                    X.append(int(str[1]))
        else:
            print('Format Error!')
    obs_log.close()
    return R,S,T,X

def schedule(R,T,X,OLT):
    OLT=OLT/60             #convert into time in hrs

    return Z

if __name__=='__main__':
    obs_log=r'C:\Users\wqs\Desktop\OBS\2.logtxt\obs_log.txt'
    [R,S,T,X]=readlog(obs_log)
    print(R, S, T, X)
    OLT=20;                                   #overlap time in min.


    Z=schedule(R,T,X,OLT)


    print(Z)