# -*- coding: utf-8 -*-
"""
Created on Sat Jan  2 15:22:56 2021

"""
day=int(input("数字を入力してください"))

if int(day)%6==0:
    print("日曜日")

elif day%6==1:
    print("月曜日")

elif day%6==2:
    print("火曜日")
    
elif day%6==3:
    print("水曜日")
    
elif day%6==4:
    print("木曜日")

else:
    print("土曜日")


    