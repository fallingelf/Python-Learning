#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np
import mayavi.mlab as mlab

mlab.figure(fgcolor=(0, 0, 0), bgcolor=(1, 1, 1))    #更改背景色
p=np.random.normal(size=(20, 20))
mlab.barchart(p)        #x,y为矩阵p的坐标,可以省略
mlab.vectorbar()        #颜色bar
mlab.show()