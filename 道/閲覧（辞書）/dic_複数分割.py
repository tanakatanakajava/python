# -*- coding: utf-8 -*-
"""
Created on Sun Feb 14 16:55:03 2021

"""

enemies = {"ザコ":"スライム", "中ボス":"ドラゴン", "ラスボス":"魔王"}
print(enemies)
print(enemies["中ボス"])

for rank in enemies:
	print(enemies[rank] + "が、あらわれた！")
for (rank, enemy) in enemies.items():
	print(rank + "の" + enemy + "が、あらわれた！")