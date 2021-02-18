# -*- coding: utf-8 -*-
"""
Created on Tue Feb 16 14:15:21 2021
"""
#かけ算九九
def multiply(x, y):#渡される引数
    return x * y#戻り値

#渡す引数
for step in range(1, 10):
    for num in range(1, 10):
        print(multiply(step, num), end="")#改行対策
        if num < 9:
            print(", ", end="")#改行対策
    print("")
