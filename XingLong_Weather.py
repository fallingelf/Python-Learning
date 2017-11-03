#!/usr/bin/env python
# -*- coding: utf-8 -*-
import urllib.request
import re
import time
import pygame
import datetime
import threading
#获取整个网页内容
def getHtml(url):
    page = urllib.request.urlopen(url)  # urllib.urlopen()方法用于打开一个URL地址
    html = page.read()                        #  read()方法用于读取URL上的数据，向getHtml()函数传递一个网址，并把整个页面下载下来。
    return html
 #正则匹配数据
def getdata(html):
    reg =r'<graph caption=\'(湿度)\' xAxisName=\'(时间)[\s\S]{1596}(\d{2}:\d{2})[\s\S]{9}(\d{2}.\d{2})'
    datre = re.compile(reg)             #把正则表达式编译成一个正则表达式对象.
    datlist = re.findall(datre, html)   #读取html中包含正则表达式的数据。
    return datlist
#找错机制----若数据的时间与当前时间误差大，则陷入死循环，并提示
def checkout(url,i):
    html=getHtml(url)
    html=html.decode("gbk")
    datatime = datetime.datetime.now()
    shijian = datatime.strftime('%H:%M')
    data=getdata(html)
    global humidity
    humidity=float(data[0][3])
    nowtime=data[0][2]
    if int(shijian[4:5]) - int(nowtime[4:5]) <=1:
        print(u'时间：',nowtime, '        ',u'湿度：',humidity)
        return
    elif i == 5:
        print(nowtime,'!=',shijian)
        print('Something is wrong')
        print('\n'+'Please key Enter to continue!')
        while input()!='':
            print('Please key Enter to continue!')
        i=1
    else:
        i += 1
        checkout(mainurl,i)

#10秒的等待输入----子线程
def inputvalue():                                                                                                #10s等待期间，若key Enter,则停止音乐，否则继续monitor
    global flag1
    print('you can input Enter to stop alarm and monitor in 5s       ')
    while input()!='':
        print('Input error! Please key Enter or leave it !')
    else:
        pygame.mixer.music.stop()
        print('you stop all')
        flag1=1
    return

#再次开始监测网页数据
def remonit():
    print('you can key Enter to continue monitoring        ')
    while  input() != '':
        print('Input error! Please key Enter or leave it !')
    return 1                                                                                                                                      #马上开始监测

#将10秒的等待输入加入线程
def waitinput():
    threads = []
    t = threading.Thread(target=inputvalue)
    threads.append(t)
    t.setDaemon(True)
    t.start()
    time.sleep(10)
    return

#主程序
def main(mainurl):
    checkout(mainurl, i=1)                                                         #查询数据
    if humidity >= 90:
        if pygame.mixer.music.get_busy():                               #判断： humidity大于90播放音乐
            x=1
        else:
            print('music start')
            pygame.mixer.music.play(loops=10)
        waitinput()
        if flag1==0:
            print('Time over! Stop keying')
    else:                                                                                    #判断： 小于90停止音乐
        if pygame.mixer.music.get_busy():
            pygame.mixer.music.stop()
        else:
            return
    return


mainurl = 'http://www.xinglong-naoc.org/weather/weatherchart1.jsp'                 #目标网站
pygame.mixer.init()
pygame.mixer.music.load('C:\\Monitor_Weather\\sound.mp3')              #加载音乐流
while 1:
    flag1 = 0
    flag2 = 0
    main(mainurl)
    if flag1==1:                                                             #监控停止
        flag2=remonit()
    print('\n' + 'Monitoring!')
    if flag2==0:
        time.sleep(40)                                                    # 每60秒访问网站一次