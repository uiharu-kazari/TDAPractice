#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  7 16:42:44 2018

@author: cx513
"""

import numpy as np
import dionysus as d
import matplotlib.pyplot as plt
from matplotlib import pyplot
from mpl_toolkits.mplot3d import Axes3D
from math import log
from math import cos
from math import sin
from math import pi
import math
import random
import pandas as pd

#ts.get_h_data('002337', start='2015-01-01', end='2015-03-16') #两个日期之间的前复权数据


def normalizedprice(price):
#loglist=list(map(log,p))
    arr=np.array(price)
    return np.divide(arr[1:],arr[0:-1])
        

def slidingwindow(tsd, N, tau=1):
    initial=np.array([tsd[0:N:tau]])
    for i in range(1,len(tsd)-N*tau+1):
        temp=np.array([tsd[i:N+i:tau]])
        initial=np.concatenate((initial,temp),axis=0)
    return initial

def circle(k):
    coor=np.zeros([k,3])
    for i in range(k):
        coor[i,0]=cos(i/k*2*pi)*np.random.normal(1,0.05)
        coor[i,1]=sin(i/k*2*pi)*np.random.normal(1,0.05)
        coor[i,2]=np.random.normal(0,0.1)
    return coor

def sphere(k):
    coor=np.zeros([k*k,3])
    for i in range(k):
        phi=i/k*2*pi
        #print('phi:',phi)
        for j in range(k):
            theta=j/k*pi
            #print('theta:',theta)
            coor[i*k+j,0]=sin(theta)*cos(phi)#*np.random.normal(1,0.1)
            coor[i*k+j,1]=sin(theta)*sin(phi)#*np.random.normal(1,0.1)
            coor[i*k+j,2]=cos(theta)#*np.random.normal(1,0.1)
    return coor

def geomill(arr,skeletondim=2,elevation=45,azimuth=30):
    #3D illustration
    fig = pyplot.figure()
    ax = Axes3D(fig)
    ax.view_init(elev=elevation, azim=azimuth)
    ax.scatter(arr[:,0],arr[:,1],arr[:,2])
    pyplot.show()
    #VR complex
    filtration = d.fill_rips(circ, skeletondim, 2)
    #persistent homology
    ph = d.homology_persistence(filtration)
    dgms = d.init_diagrams(ph, filtration)
    d.plot.plot_bars(dgms[1], show = True)
    return ax,dgms






'''

s = pd.read_csv('SNEdata.csv')
s.plot()
p=s.Adj_Close

fig = pyplot.figure()
ax = Axes3D(fig)
swdata=slidingwindow(normalizedprice(p),3)
swdata=slidingwindow(p,3)

sequence_containing_x_vals = swdata[0:-1:5,0]
sequence_containing_y_vals = swdata[0:-1:5,1]
sequence_containing_z_vals = swdata[0:-1:5,2]

ax.view_init(elev=45., azim=30)
ax.scatter(sequence_containing_x_vals, sequence_containing_y_vals, sequence_containing_z_vals)
pyplot.show()


filtration = d.fill_rips(swdata, 2, 2.1)

ph = d.homology_persistence(filtration)

dgms = d.init_diagrams(ph, filtration)

d.plot.plot_bars(dgms[1], show = True)'''