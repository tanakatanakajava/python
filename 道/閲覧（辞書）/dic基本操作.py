# -*- coding: utf-8 -*-
"""
Created on Sun Feb 14 15:43:10 2021
"""

# 辞書の基本操作
enemies = {"ザコ":"スライム", "中ボス":"ドラゴン", "ラスボス":"魔王"}
print(enemies)
print(enemies["ザコ"])
print(len(enemies))

#辞書に追加
enemies["雑魚2"]="メタルスライム"
print(enemies)
print(len(enemies))

#辞書に上書き
enemies["中ボス"]="レッドドラゴン"
print(enemies)
print(len(enemies))

#辞書から削除
del enemies["ザコ"]
print(enemies)
print(len(enemies))


