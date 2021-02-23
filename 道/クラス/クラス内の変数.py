# -*- coding: utf-8 -*-
"""
Created on Sun Feb 21 20:45:18 2021

"""

# coding: utf-8
# アクセス制限を理解する

#＿＿変数で、クラスの中でしか呼び出せない変数（プライベート変数）
class Player:
    def __init__(self, job, weapon):
        self.job = job
        self.__weapon = weapon

    def walk(self):
        print(self.job + "は荒野を歩いていた")#戦士は荒野を歩いていた
        self.__attack("スライム")
        
    #__メソッド名→クラスの中でしか呼び出せないメッソド
    def __attack(self, enemy):
        print(self.__weapon + "で" + enemy + "を攻撃")#剣でスライムを攻撃

player1 = Player("戦士", "剣")
player1.walk()
#player1.__attack("スライム")
#print(player1.__weapon)





