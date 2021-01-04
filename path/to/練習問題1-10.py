# -*- coding: utf-8 -*-
"""
Created on Mon Jan  4 16:19:46 2021
"""

n = int(input('数> '))
for j in range(1,n+1) :
    print(str(j)+':',end='') # 改行しない出力
    
    for i in range(0,j) :
        print('■',end='')
    print() # 改行だけ出力