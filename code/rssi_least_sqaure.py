#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct  7 13:28:47 2018

@author: erikzhou
"""

# Fit a line, ``y = mx + c``, through some noisy data-points:
import numpy as np
import math

#v0 = [-71.20,-64.33,-81.67,-58.60,-69.50,7.3,2.5,0.22,0.20,0.13,0.22,0.2]


dist = np.array([1.0, 3.0, 4.5, 7.0, 9.5, 12.5, 16.0, 19.0, 23.0, 26.0])          #log10(distance)
rssi = np.array([-47.0, -55.83, -55.93, -57.77, -67.53, -63.21, -71.21, -69.83, -70.66, -72.62])     #RSSI
log_dist = np.array(list(map(lambda x: round(math.log10(x),2),dist)))   #transform dist to log10(dist)

rssi_read =  -81.67
#i = list(rssi).index(rssi_read)

#print(log_dist)
#print(dist)
#test 13, -65.93;20.5 -69.28;8.9 -70.03




def least_square(log_dist,rssi):    
    A = np.vstack([log_dist, np.ones(len(log_dist))]).T     
    m, c = np.linalg.lstsq(A, rssi,rcond=-1)[0]
    
    return m,c

#from the  rssi_read= mlog10(dist) + c get the distance
def get_dist(m,c,rssi_read):
        return 10**((rssi_read - c)/m)
    
#trilateral localisation 
#known the distance of node x to three base station node find the least square fit of node x coordinates



#calculations
m,c = least_square(log_dist,rssi)
distance = get_dist(m,c,rssi_read)

print("m, c:{}, {} and the distance for {} is {}".format(m,c,rssi_read,round(distance,1)))