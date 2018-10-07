#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 30 16:35:21 2018

@author: erikzhou
"""

# Fit a line, ``y = mx + c``, through some noisy data-points:
import numpy as np
import matplotlib.pyplot as plt
import math

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
    return round(m,1),round(c,1)


#plot the trilocation fit 
def plot_trilocation(x1,y1,r1,x2,y2,r2,x3,y3,r3,u1,u2):
    circle1 = plt.Circle((x1, y1), r1, color='r',fill=False)
    # now make a circle with no fill, which is good for hi-lighting key results
    circle2 = plt.Circle((x2, y2), r2, color='b', fill=False)
    circle3 = plt.Circle((x3, y3), r3, color='g', fill=False)
    
    ax = plt.gca()
    ax.cla() # clear things for fresh plot
    
    # change default range so that new circles will work
    ax.axis('equal')
    ax.axis([0,50,0,50])
    plt.plot(u1, u2, 'bo')
    
    ax.add_artist(circle1)
    ax.add_artist(circle2)
    ax.add_artist(circle3)

    return

def get_dist(m,c,r):
        return 10**((r - c)/m)

v0 = [-71.20,-64.33,-81.67,-58.60,-69.50,7.3,2.5,0.22,0.20,0.13,0.22,0.2]
#v0 =[-64.33,-65.83,-73.50,-60.00,-58.17,19.5,2.5,0.21,0.21,0.17,0.21,0.2]
#v0 = [-63.40,-64.30,-72.60,-56.40,-67.50,13,2.7,0.20,0.20,0.20,0.20,0.2]
coordinate = v0[5:7]
#Base station Coordinates
base = {0:[0,0], 1:[25,2], 2:[29.2,-1],3:[8.8,5],4:[17.4,0]}

#give the base station input and range output predicted node x location 
m = -18.549794068963205; c = -45.88914172179528     #constants of the least sqaure for RSSI
distance = [round(get_dist(m,c ,r),1) for r in v0[:5]]       # distance for each base station
print(distance)
print(base)
(x1,y1,r1,x2,y2,r2,x3,y3,r3) = (base[0][0],base[0][1],distance[0],base[3][0],base[3][1],distance[3],base[4][0],base[4][1],distance[4])
u1,u2 = trilocation(x1,y1,r1,x2,y2,r2,x3,y3,r3)
err = round(math.sqrt((u1-coordinate[0])**2 + (u2 - coordinate[1])**2),1)

print("The Node X location is", u1,u2)
print("the right location is " , coordinate)
print("the error is ",err)
plot_trilocation(x1,y1,r1,x2,y2,r2,x3,y3,r3,u1,u2)




 