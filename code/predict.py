#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  5 12:29:28 2018

@author: erikzhou
"""
import os
import numpy as np
import math

#cwd = os.getcwd()
#os.chdir("/iot")
#print(cwd)

#v = [-62.00 ,-84.33 ,-70.00 ,-64.75 ,-59.75] #5 3.2
#v = [-59.50, -76.50, -57.50, -70.75, -62.33] # 5.7 5
#v = [-64.75 ,0 ,-58.25 ,0 ,-65.50] #19 3.1]
#v = [-69.33 ,-75.00 ,-54.50 ,-87.33 ,-71.00] #21 1.4]
#v = [-62.25, 0, -66.00, 0, -59.75]# 7.5 3.3
#v = [-62.25, -78.67, -66.00, -85.00, -59.75]# 7.5 3.3
#v =[-63.50,-78.00,-63.00,-85.50,-59.50] #7.5,3.3]
#v = [1,1,1,1,1]
#v = [-82.25,-78.00, -71.25, -75.67, -61.33] #39,     -2




#-83.50,-80.00,-77.50,-76.00,-63.00,39,-2
#-84.50,-73.00,-83.00,0.00,0.00,39,-12.5
#v= [-68.00,-70.50,-52.50,-87.00,-70.50] #21,1.4
#-64.50,-75.00,-58.50,-88.00,-64.00,19,3.1
#-63.50,-78.00,-63.00,-85.50,-59.50,7.5,3.3
v= [0.00,-79.50,-68.00,-86.00,-68.50] #3.7,3.1

#v = list(map(lambda x: 10**(x/100),v) )

nearest ={};
coordinate_v = {}
weight_c = [1.2,0.8,0.3,0.2,0.1]
weight = [0,0,0,0,0]
#assign weight to v
index ={}
i = 0
#weight = {index:value}
for e in v:
    index[i] = e
    i += 1
    
value_order = sorted(index.items(), key=lambda kv: kv[1], reverse = True)
#print(value_order)

start =0
for e in value_order:
    (i, val) = e
    weight[i] =weight_c[start]
    start += 1
    
#print(weight)

#assign weight element wise to v according to weight
v = [round(a * b,1) for a, b in zip(weight, v)]





#for a given test point reading predict x,y output
def dot_product(v):
    #read from test.txt file line by line:x1 x2 x3 x4 x5 x y
    f = open('new1.txt', 'r')
    for line in f.readlines():#reads the whole file into memory and returns its contents as a list of its lines.
        #assme input for each line would be x1 x2 x3 x4 x5 x y
        v1 = line.rstrip().split(',')
        #print(v1)
        v1 = list(map(lambda x: float(x),v1))     
        
        #each line would be x1 x2 x3 x4 x5 x y find vector and coordinates
        coordinate = v1[-2:]
        vector = v1[:-2]
        
        #assign weight to vector
        vector = [round(a * b,1) for a, b in zip(weight, vector)]
        
        #print(vector)
       # vector = list(map(lambda x: 10**(x/100),vector) )
        vd = [a - b for a, b in zip(vector, v)]

        #record the the dot product value and the coordinates in the dict
        # (x,y):dot_val
        nearest[tuple(coordinate)] = np.dot(vd,vd)
        coordinate_v[tuple(coordinate)] = vector
        
    f.close
    return nearest


#find the top 3 smallest dot product coordinates
#we have dot_val:[x,y]
nearest = dot_product(v)
order_nearest = sorted(nearest.items(), key=lambda kv: kv[1]) #[((5.7, 5.0), 0.0),...]

print("Original vectore is :      ",v)
print("Dot_val:    Coordinates:")
for key in order_nearest:
    ((x,y),dot_val) = key
#    #c = list(map(lambda x: round(math.log(x,10)*100,1),(nearest[key])))
    print("{:10.4f}".format(round(dot_val,4)), "    ","({:4.1f},{:4.1f})".format(x,y), coordinate_v[(x,y)])
   
    
    

