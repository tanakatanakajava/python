# -*- coding: utf-8 -*-
"""
Created on Sun Jan  3 22:50:37 2021

"""

n=int (input("数＞ "))
print(str(n)+':',end='')#改行しない出力

for i in range(0,n):
    print("*",end='') 
    
    #print('*'*n)でも可能
print()#改行だけ出力
    
