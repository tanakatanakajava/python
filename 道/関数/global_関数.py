# -*- coding: utf-8 -*-
"""
Created on Tue Feb 16 16:24:56 2021

"""

# スコープを理解する

message = "paiza"
a = 10
b = 20

def sum(x, y):
    a = 3
    global message#global 変数 は、グローバル変数に
                            #代入、変更するときに使う
    message += "paiza"
    print(message + " " + str(a))#paizapaiza 3
    return x + y

num = sum(a, b)
print(num)
print(message + " " + str(a))#10

