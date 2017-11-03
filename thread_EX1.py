#!/usr/bin/env python
# -*- coding: utf-8 -*-
import threading
import time
def waitinput():
    global flag
    flag=0
    keyput=input('you can input a key value')
    if keyput=='':
        print('music stop')
        flag=1
    else:
        print('music continue')

	 
def music():
    print('music start')

def main():
 while 1:
    threads = []
    t1 = threading.Thread(target=music)
    t2 = threading.Thread(target=waitinput)
    threads.append(t1)
    threads.append(t2)
    for t in threads:
        t.setDaemon(True)
        t.start()
    time.sleep(5)
    if flag == 1:
        print(flag)
        return

main()
print('its over')
