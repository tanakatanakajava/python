# -*- coding: utf-8 -*-
"""
Created on Thu Jan  7 12:14:11 2021

"""

a=int(input("数字を入力"))
b=int(input("数字を入力"))
c=int(input("数字を入力"))

if a>b:
    temp=a
    a=b
    b=temp

if a>c:
    temp=a
    a=c
    c=temp
    
if b>c:
    temp=b
    b=c
    c=temp
    
print(a,b,c)
#数字を照準に並びかえる