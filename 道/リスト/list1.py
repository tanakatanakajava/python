# -*- coding: utf-8 -*-
"""
Created on Sat Feb 13 15:37:28 2021

"""

#readlinesは、一度にすべての行を標準入力で読み込む関数
import sys
array=input()

for line in sys.stdin.readlines():
    array.append(line.rstrip())
    #print(line.rstrip())

print(array)
"""
for line in sys.stdin.readlines():
    print(line.rstrip())
    
"""

"""
#readlinesは、一度にすべての行を標準入力で読み込む関数
import sys
array=[]
for line in sys.stdin.readlines():
    array.append(line.rstrip())
    #print(line.rstrip())

print(array)    
"""