# -*- coding: utf-8 -*-
"""
Created on Fri Feb 12 16:33:20 2021

"""

line = input().rstrip().split(",")
#rstripは、開業を削除
#splitは、引数でした文字で分割する
print(line)

print(len(line))
#リストの要素数を表示

for enemy in line:#変数 in オブジェクト(リスト)
    print(enemy+"が現れた")