# -*- coding: utf-8 -*-
"""
Created on Tue Feb 16 23:15:28 2021

"""

import random

def attack(enemy):
    print("勇者は、" + enemy + "を攻撃した。")
    hit = random.randint(1,10)
    if hit < 6:
        print(enemy + "に、" + str(hit) + "のダメージを与えた！")
    else:
        print("クリティカルヒット！" + enemy + "に、100のダメージを与えた！！")

enemies = ["スライム", "モンスター", "ドラゴン"]
for enemy in enemies:
    # print("勇者は、" + enemy + "を攻撃した。")
    attack(enemy)