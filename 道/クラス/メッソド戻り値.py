# -*- coding: utf-8 -*-
"""
Created on Sun Feb 21 15:12:53 2021
"""

# coding: utf-8
# クラスで、引数と戻り値のあるメソッドを作る

class item:
    
    tax=1.
    def __init__(self,price,quqntity):
        #変数の宣言、値を受け取る
        self.price=price
        self.quqntity=quqntity
        
    def total(self):
        #実際に計算する部分（戻り値）
        return int(self.price*self.quqntity*item.tax)

apple=item(120,15)
print("ごうけいは"+str(apple.total())+"￥です")
                #変数.戻り値の関数()
#メッソドの戻り値

"""変数にも代入できる
total=apple.total
print("ごうけいは"+str(total)+"￥です")
"""

