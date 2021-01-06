# coding: utf-8 
"""
Created on Wed Jan  6 13:08:49 2021
"""

ten=int(input("数字を入力"))
origin=ten

first= ten // 2**7
ten= ten % 2**7

two = ten //2**6
ten = ten %2**5

three = ten //2**5
ten   = ten % 2**4

four  = ten //2**4
ten   = ten %2**4

five  = ten //2**3
ten   = ten % 2**3

six   = ten //2**2
ten   = ten %2**2

seven = ten//2**1
ten   = ten%2**1

binary = str(first) + str(two)+  str(three)+ str(four) + str(five) + str(six) + str(seven)
#２行にするとエラーになる

print(origin,":",binary,sep="")
