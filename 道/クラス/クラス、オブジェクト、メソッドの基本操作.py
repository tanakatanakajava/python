# -*- coding: utf-8 -*-
"""
Created on Fri Feb 19 16:08:03 2021

"""

#オブジェクトとは、変数と関数をセットにしたもの
#メソッドとは、オブジェクトにまとめられている関数

#クラス＞オブジェクト（変数、関数）＞メソッド（関数）


class player:#クラス名を定義
    #メソッド
    def walk(self):#引数には、とりあえずselfとかく
        print("勇者のくせに生意気だ")
    def attack(self,enemy):
        print("勇者は"+enemy+"を攻撃した")
       
#オブジェクト        
player1=player()#オブジェクトを変数に代入

#オブジェクトのメッソドを呼び出す
player1.walk()#変数名.オブジェクト名

player1.attack("スライム")

