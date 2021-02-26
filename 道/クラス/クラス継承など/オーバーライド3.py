# -*- coding: utf-8 -*-
"""
Created on Tue Feb 23 12:17:14 2021

"""

# coding: utf-8
# メソッドをオーバーライドしよう2

class Greeting:
    def __init__(self):
        self.msg = "hello"
        self.target = "paiza"
    
    def say_hello(self):
        print(self.msg + " " + self.target)

class Hello(Greeting):
    def say_hello(self):
        print(self.msg + " " + self.target)
        print("YEAH YEAH YEAH!")

"""
player = Greeting()
player.say_hello()
"""
player=Hello()
player.say_hello()

#hello paiza
#YEAH YEAH YEAH!