# -*- coding: utf-8 -*-
"""
Created on Tue Feb 23 12:12:41 2021

"""
class Greeting:
    def __init__(self):
        self.msg = "hello"
        self.target = "paiza"

    def say_hello(self):
        print(self.msg + " " + self.target)

class Hello(Greeting):
    # ここにオーバライドするメソッドを記述する
    def say_hello (self,target):
        print(self.msg+" "target)#targetにSELFはつけない


player = Hello()
player.say_hello("python") 
#変更し大変巣(target)に引き渡す

#hello python