# -*- coding: utf-8 -*-
"""
Created on Thu Feb 18 09:59:48 2021

"""

# キーワード引数
def say_hello(greeting="hello",target=" world"):
    print(greeting+target)

say_hello()
say_hello("こんにちは","皆さん")
#こんにちは皆さん
say_hello("good morning")
#good morning world

say_hello(greeting="こんにちは",target="皆さん")
#こんにちは皆さん
say_hello(target="こんにちは",greeting="皆さん")
#皆さんこんにちは

say_hello(target="こんにちは")
#helloこんにちは
say_hello(greeting="皆さん")
#皆さん world


