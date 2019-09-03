#!/usr/bin/python

# File Usage: This file is to estimate LT of sample retention data
# Last Edit Date: 2019/7/18
# Author: Ian Qian Ting

import os, sys, math
import numpy as np
from scipy.optimize import leastsq
import pandas as pd
import matplotlib.pyplot as plt

#import csv data
datas = pd.read_csv('retention_data.csv')
#trim non-numeric index
datas.drop(["Media Source","Date"],1,inplace = True)
#print(datas['Install Day'])
shape = datas.shape
print "row count:", shape[0], "\ncolumn count:", shape[1]

row1 = np.array(datas.iloc[1])
print(row1)

x = np.array(range(0,shape[1])) 
print(x)
init_coef = [1, 1, 1]
#use f(x)=a*x**b+c to fit retention
#def fpowerfit(coef,x):
#  y = coef[0] * pow(x,coef[1]) + coef[2]
#  print "y: ", y
#  return y

p0 = [0.1, 0.1]
def flinefit(x,p):
  a = p[0]
  b = p[1]
  return x * a + b

def err(y,x,p):
  return y - flinefit(x,p)
#  return y - fpowerfit(coef,x)


opt_coef, status = leastsq(err, p0, args=(x,row1))
#print "power fit: ", opt_coef
print "line fit: ", opt_coef

#draw power fit curve
opt_y = fpowerfit(opt_coef, x)
plt.plot(x,row1,'r-',x,opt_y,'g-')
plt.show()

