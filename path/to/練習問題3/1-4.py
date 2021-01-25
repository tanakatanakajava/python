# -*- coding: utf-8 -*-
"""
Created on Mon Jan 25 12:23:35 2021

"""
speed=int(input("時速を入力"))

speed=speed*1000/60

print("分速:%dm/min"%(speed))

speed=speed/60
print("秒速:%dm/s"%(speed))

