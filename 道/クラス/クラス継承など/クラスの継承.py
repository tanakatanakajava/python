# -*- coding: utf-8 -*-
"""
Created on Tue Feb 23 11:36:14 2021

"""
#スーパークラス【親クラス】の作成
class box:
    def __init__ (self,item):
        self.item=item
        
    def open(self):
        print("宝箱を開いた."+self.item+"を手に入れた")

#サブクラスの作成（ __init__ )メッソド（コンストラクタ）はいらない
class jewelrybox(box): #サブクラス名(親クラス名):
    def look (self): 
        print("宝箱はキラキラと輝いている")#追加する動作

cherst=box("剣")
cherst.open()

#オブジェクトの作成
jewelrycherst=jewelrybox("指輪")
jewelrycherst.look()
jewelrycherst.open()
#定義されたていないメッソドが呼び出されたとき自動的に親クラスのメッソドが呼び出される


#スーパークラス【親クラス】の作成
#サブクラスの作成
        #（ __init__ )メッソド（コンストラクタ）はいらない
     #サブクラス名(親クラス名):

#オブジェクトの作成
#変数名＝クラス名（引数）
