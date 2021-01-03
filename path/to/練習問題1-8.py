# -*- coding: utf-8 -*-
"""
Created on Sun Jan  3 09:41:20 2021

"""

n=int (input("数> "))
fac=1

for i in range(0,n): #(1,n)だと４の階乗
    fac*=i             #
    
print(str(n)+"!=",fac,sep="")

#階乗を表示させるプログラム

# forの構文
# for 変数 in イテラブルオブジェクト

#イテラブルオブジェクト→配列とか

