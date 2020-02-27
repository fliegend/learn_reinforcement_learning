# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 14:51:53 2020

@author: lijiancong
"""

import matplotlib.pyplot as plt
import numpy as np

lamda = 0.9
weights = []
T = 16
MAXT = 30

def weight(lamda, t):
    return (1-lamda)*np.power(lamda, t)

def base_func(t):
    return 0*t

x = np.linspace(1, MAXT,MAXT)
y = weight(lamda, x)
y1 = base_func(x)

plt.figure(figsize=(30,10))
markerline, stemlines, baseline = plt.stem(x, weight(lamda,x), ':','-')
plt.setp(markerline, color='black', linewidth=2)
plt.setp(stemlines, color='black', linewidth=1)
plt.setp(baseline, color='black', linewidth=2)


xf=x[np.where((x>=3)&(x<=4))]
plt.fill_between(xf,weight(lamda,xf),base_func(xf),color='black',alpha=0.25)
xf2 = x[np.where(x>=T)]
plt.fill_between(xf2,weight(lamda,xf2),base_func(xf2),color='black',alpha=0.25)
plt.xticks([])
plt.yticks([])
#plt.axis('off')

plt.show()

X = [0,0,1,1,1,1,0,0,0,0,1,1,0,0,0,1,0,0,0,0,0]
lamda = 0.5

def ET(x, lamda):
    et = 0
    result_x = []
    result_y =[]
    for i in range(len(X)):
        x = X[i]
        if x == 1:
            et += 1        
            result_y.append(et)
            result_x.append(i-1)
        et  *= lamda
        result_y.append(et)
        result_x.append(i)
    return result_x,result_y
X,Y = ET(X, lamda)

plt.figure(figsize=(20,5))


markerline, stemlines, baseline = plt.stem(X, Y, ':','-',":")
plt.setp(markerline, color='black', linewidth=2)
plt.setp(stemlines, color='black', linewidth=0.5)
plt.setp(baseline, color='black', linewidth=1)


plt.xticks([])
plt.yticks([])
#plt.axis('off')

plt.show()