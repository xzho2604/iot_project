#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 30 16:35:21 2018

@author: erikzhou
"""

# Fit a line, ``y = mx + c``, through some noisy data-points:
import numpy as np
import matplotlib.pyplot as plt

#given input of x1,y1,r1  x2,y2,r2  x3,y3,r3 
#output the best least squre fit of coordinates (u1,u2)
def trilocation(x1,y1,r1,x2,y2,r2,x3,y3,r3):
    v1 = np.array([x3-x1,
                   x3-x2,
                   x1-x2])
    
    v2= np.array([y3-y1,
                  y3-y2,
                  y1-y2])
    
    y = np.array([(r1**2 - r3**2) - (x1**2 - x3**2) - (y1**2 - y3**2),
                  (r2**2 - r3**2) - (x2**2 - x3**2) - (y2**2 - y3**2),
                  (r2**2 - r1**2) - (x2**2 - x1**2) - (y2**2 - y1**2)])
    
    
    #v1 v2 element wise mul by 2
    v1 = np.array(list(map(lambda x:2*x,v1)))
    v2 = np.array(list(map(lambda x:2*x,v2)))
    A = np.vstack([v1, v2]).T
    
    m, c = np.linalg.lstsq(A, y,rcond=None)[0]
    return m,c


#plot the trilocation fit 
def plot_trilocation(x1,y1,r1,x2,y2,r2,x3,y3,r3,u1,u2):
    circle1 = plt.Circle((x1, y1), r1, color='r',fill=False)
    # now make a circle with no fill, which is good for hi-lighting key results
    circle2 = plt.Circle((x2, y2), r2, color='b', fill=False)
    circle3 = plt.Circle((x3, y3), r3, color='g', fill=False)
    
    ax = plt.gca()
    ax.cla() # clear things for fresh plot
    
    # change default range so that new circles will work
    ax.set_xlim((0, 100))
    ax.set_ylim((0, 100))
    
    plt.plot(u1, u2, 'bo')
    
    ax.add_artist(circle1)
    ax.add_artist(circle2)
    ax.add_artist(circle3)

    return


#give the base station input and range output predicted node x location 
(x1,y1,r1,x2,y2,r2,x3,y3,r3) = (50,70,24,20,20,35,70,30,32)
m,c = trilocation(x1,y1,r1,x2,y2,r2,x3,y3,r3)
print("The Cooordinates of Node x is", m,c)
plot_trilocation(x1,y1,r1,x2,y2,r2,x3,y3,r3,m,c)




 