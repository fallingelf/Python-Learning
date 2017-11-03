#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy as np
import mayavi.mlab as mlab

mlab.figure(fgcolor=(0, 0, 0), bgcolor=(1, 1, 1))    #更改背景色
s=np.random.normal(size=(21, 21))
#mlab.barchart(s)        #x,y为矩阵p的坐标,可以省略
#mlab.imshow(s)           # the colormap
x, y = np.mgrid[-10:10:21j, -10:10:21j]
mlab.mesh(x,y,s)
mlab.vectorbar()        #颜色bar
mlab.show()