#!/usr/bin/env python
# -*- coding: UTF-8 -*-

try:
    fh = open("testfile.txt", "r")
    fh.write("这是一个测试文件，用于测试异常!!")
except:
    print ("Error: 没有找到文件或读取文件失败")
else:
    print('成功写入')
finally:                                                                                       #不管有无异常总是执行finally
    print('over')