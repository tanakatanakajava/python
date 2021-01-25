# -*- coding: utf-8 -*-
"""
Created on Mon Jan 25 11:10:02 2021

"""

height=float(input("身長をM単位で入力してください"))
weight=float(input("体重をkgで入力してください"))

print("BMI=%f"%(weight/height/height))

bmi=weight/height/height

if (bmi<18.5):
    print("やせてる")
elif (18.5<=bmi<22.5):
    print("標準")
else :
    print("太りすぎ")


