# -*- coding: utf-8 -*-
"""
Created on Sun Feb 21 14:11:05 2021
"""



class Enemy:
    def __init__(self, name):
        self.name = name

    def attack(self):
        print(self.name + "は勇者を攻撃した")

enemies = []
enemies.append(Enemy("スライム"))
enemies.append(Enemy("モンスター"))
enemies.append(Enemy("ドラゴン"))

for enemy in enemies:#for 変数 in リスト
    enemy.attack()
    #変数.メッソド()
