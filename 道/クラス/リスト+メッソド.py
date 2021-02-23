# -*- coding: utf-8 -*-
"""
Created on Sun Feb 21 20:14:46 2021
@author: ic201236
"""
#文字列とメッソド
text="pYthon"
print(text.capitalize())#先頭の文字を大文字、それ以外を小文字にする
#Python

print(text.upper())#すべて大文字(PYTHON)

players = "勇者,戦士,魔法使い,忍者"
list = players.split(",")
print(list)#['勇者', '戦士', '魔法使い', '忍者']

list.remove("忍者")#忍者を削除
print(list)#['勇者', '戦士', '魔法使い']

list.append("ばか")#ばかを追加
print(list)#['勇者', '戦士', '魔法使い', 'ばか']

