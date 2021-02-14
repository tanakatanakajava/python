# -*- coding: utf-8 -*-
"""
Created on Sun Feb 14 14:22:25 2021

"""

import random

line = input().rstrip().split(",")
for enemy in line:
	print(enemy + "が現れた！")

#ランダムな値の範囲を決める
num=len(line)
print("敵は"+str(num)+"匹")

#ランダムな数を生成
attck=random.randrange(num)



print(line[attck]+"に会心の一撃")