# -*- coding: utf-8 -*-
"""
Created on Sat Jan  2 16:32:20 2021
"""

year=int(input("西暦を入力してください"))

if year%400==0 :
    print("うるう年です")

elif year%100!=0 and year%100==0:
    print("うるう年ではありません")
    
elif year%400!=0 and year%4==0:
    print("うるう年です")

else :
    print("うるう年ではありません")


    
    
    
