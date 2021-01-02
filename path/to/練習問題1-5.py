# -*- coding: utf-8 -*-
"""
Created on Sat Jan  2 15:02:25 2021

"""

m=float(input("Mで入力してください"))

kg=float(input("kgで入力してください"))

bmi=float(kg/m**2)
print("bmi=" + str(bmi))
#strを忘れずにを忘れずに

if bmi<18.5:
    print("やせすぎ")

elif 18.5<=bmi<=25:
    print("いい感じ")
    
else :
    print("太りすぎ")

#bmiを表示させるプログラム

