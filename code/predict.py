#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  5 12:29:28 2018

@author: erikzhou
"""
import os
import numpy as np
import math


os.chdir("/Users/erikzhou/Desktop/git_prac/iot_project/data02")
cwd = os.getcwd()
print(cwd)

#v0 = [-71.20,-64.33,-81.67,-58.60,-69.50,7.3,2.5,0.22,0.20,0.13,0.22,0.2]
#v0 =[-64.33,-65.83,-73.50,-60.00,-58.17,19.5,2.5,0.21,0.21,0.17,0.21,0.2]
#v0 = [-63.40,-64.30,-72.60,-56.40,-67.50,13,2.7,0.20,0.20,0.20,0.20,0.2]
#v0=[-59.40,-79.50,-68.25,-63.30,-73.80,2.3,2,0.21,0.21,0.17,0.21,0.2]
#v0=[-71.60,-62.00,-85.11,-61.80,-65.60,24.2,4.4,0.20,0.20,0.18,0.20,0.2]

#v0=[-66.90,-80.00,-77.50,-67.00,-59.80,11.1,3.3,0.20,0.20,0.20,0.20,0.20]
#v0=[-70.50,-74.40,-79.00,-64.10,-48.90,14.5,2.8,0.20,0.20,0.20,0.20,0.20]
#v0=[-72.70,-69.60,-74.50,-63.90,-58.90,14.5,4,0.20,0.20,0.20,0.20,0.20]


#v = list(map(lambda x: 10**(x/100),v) )
v = v0[:5]        #sample vector 
origin = v0[5:7]    #origin coordinates
w = v0[7:]          #the weight of each base station reading


nearest ={};
coordinate_v = {}

#assign weight according to weight_c
def add_weight(weight_c,v):
    #assign weight to v
    index ={}
    i = 0
    weight = [0,0,0,0,0]
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
    return weight


#for a given test point reading predict x,y output
def dot_product(v):
    #read from test.txt file line by line:x1 x2 x3 x4 x5 x y
    f = open('clean_record.txt', 'r')
    for line in f.readlines():#reads the whole file into memory and returns its contents as a list of its lines.
        #assme input for each line would be x1 x2 x3 x4 x5 x y
        v1 = line.rstrip().split(',')
        #print(v1)
        v1 = list(map(lambda x: float(x),v1))     
        
        #each line would be x1 x2 x3 x4 x5 x y find vector and coordinates
        coordinate = v1[5:7]
        vector = v1[:5]
        global w
        global coordinate_v
        
        
        #assign weight to vector
        weight_c = [1,0,0,0,0]

        #print(vector)
       # vector = list(map(lambda x: 10**(x/100),vector) )
           
        vd = [round(a - b,1) for a, b in zip(vector, v)]
        #print("before weight:" , vd)
        vd = [round(a * b,1) for a, b in zip(w, vd)]    #apply count weigth to the difference
        vd = [round(a * b,1) for a, b in zip(add_weight(weight_c,v),vd)]
        #print("after weight:" , vd)

        #record the the dot product value and the coordinates in the dict
        # (x,y):dot_val
        nearest[tuple(coordinate)] = np.dot(vd,vd)
        coordinate_v[tuple(coordinate)] = vector
        
    f.close
    return nearest

#given 3 coordinates find the centre of the triangle output a coordinate
#input : [(x,y)...]
def find_gravity(near_xs,near_ys):
    u1 = round(np.mean(near_xs),1)
    u2 = round(np.mean(near_ys),1)
    
    return u1, u2

#take sample vectore RSSI readings from 5 base stations return the index of the best 3
#and then find the centre of the 3 readings
def base_filter(v):
    best_index=[]
    for _ in range(3):
        best_index.append(v.index(max(v)))
        v.remove(max(v))
        
    #now we have the best index find the centre of the coordinates
    #x coordinates of the best base stations
    xs = [base[x][0] for x in best_index]
    ys = [base[y][1] for y in best_index]
    
    return find_gravity(xs,ys)

    

#each base station coordinates
base = {0:[0,0], 1:[25,2], 2:[29.2,-1],3:[8.8,5],4:[17.4,0]}
#find the top 3 smallest dot product coordinates
#we have dot_val:[x,y]
nearest = dot_product(v)
order_nearest = sorted(nearest.items(), key=lambda kv: kv[1]) #[((5.7, 5.0), 0.0),...]



print("Dot_val:    Coordinates:")
print("=======================================")
near_xs = []
near_ys = []
for key in order_nearest:
    ((x,y),dot_val) = key
    
    near_xs.append(x)
    near_ys.append(y)
#    #c = list(map(lambda x: round(math.log(x,10)*100,1),(nearest[key])))
    print("{:10.4f}".format(round(dot_val,4)), "    ","({:4.1f},{:4.1f})".format(x,y), coordinate_v[(x,y)])
   

print()
print("Original vector:      ")
print("=======================================")
print("{:10.4f}".format(round(0,4)), "    ","({:4.1f},{:4.1f})".format(origin[0],origin[1]), v)

#find the centre of the nearest 3 points as the predicted location of node x
nei= 3 #choice of number of neigbhours to predict
u1, u2 = find_gravity(near_xs[:nei],near_ys[:nei])
u3,u4 = base_filter(v)

u5 = (u1+u3)/2
u6 = (u4+u2)/2
print("The Prediced    :({},{})".format(u1,u2), u5, u6)
err = round(math.sqrt((u1-origin[0])**2 + (u2-origin[1])**2),1)
err_new = round(math.sqrt((u5-origin[0])**2 + (u6-origin[1])**2),1)
print("The error is    :", err)
print("The new error is    :", err_new)
    
