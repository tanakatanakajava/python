# -*- coding: utf-8 -*-
"""
Created on Fri Jan  8 12:13:34 2021

"""
num=1
ans=0
count=0   
value=int(input("数>>"))

while 0<=value:
    
    count+=1
    ans+=value
    
    value=int(input("数"))
    
print("データ数",count)
print("合計:",ans)
print("平均",ans/count)


    