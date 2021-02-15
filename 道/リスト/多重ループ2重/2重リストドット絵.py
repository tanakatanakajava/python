# -*- coding: utf-8 -*-
"""
Created on Mon Feb 15 11:41:35 2021

"""

# coding: utf-8
# Your code here!

# ドット絵を表示する

enemy_img = [[0,0,1,1,1,1,1,1,1,1,1,1,1,1,0,0],
             [1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1],
             [1,0,0,1,1,1,0,0,0,1,1,1,0,0,0,1],
             [1,1,0,0,0,0,1,1,0,0,0,0,0,0,1,1],
             [0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0],
             [0,0,0,1,1,1,0,0,0,0,0,1,1,1,0,0],
             [0,0,0,0,1,1,1,0,0,0,0,0,0,1,1,1]]

for line in enemy_img:
    for dot in line:
        print(dot,end="")#endで、改行対策
    print()#改行
    
    
    
    
for line in enemy_img:
    for dot in line:
        if dot ==1:
            print("#",end="")#endで、改行対策
        else:
            print(" ",end="")
    
    print()#改行