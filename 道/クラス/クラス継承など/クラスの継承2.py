# -*- coding: utf-8 -*-
"""
Created on Tue Feb 23 17:37:04 2021
"""
class Player:#親クラス
    def __init__(self, name):
        self.name = name

    def attack(self, enemy):
        print(self.name + "は、" + enemy + "を攻撃した！")

class Wizard(Player):#子クラス
    def attack(self, enemy):
        print("ズバーン！")
        print(self.name + "は、" + enemy + "に炎を放った！")

print("=== パーティーでスライムと戦う ===")
hero = Player("勇者")
warrior = Player("戦士")
wizard = Wizard("魔法使い")
"""こういうやり方もあり
team = []
team.append(Player("勇者"))
team.append(Player("魔法使い"))
team.append(Warrior("戦士"))
"""

party = [hero, warrior, wizard]
for member in party:
    member.attack("スライム")

"""
=== パーティーでスライムと戦う ===
勇者は、スライムを攻撃した！
戦士は、スライムを攻撃した！
魔法使いは、スライムに炎を放った！
"""
