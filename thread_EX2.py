# -*- coding: utf-8 -*-
import threading,time

def music():
    while input()!='':
     print('music '+time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
    return

def movie():
    print('movie ' +time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
    return

def main():
    threads=[]
    t1 = threading.Thread(target=music)
    t2 = threading.Thread(target=movie)
    threads.append(t1)
    threads.append(t2)
    for t in threads:
        t.setDaemon(True)
        t.start()
    time.sleep(4)
    return

main()
print('over')
