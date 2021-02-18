# -*- coding: utf-8 -*-
"""
Created on Wed Feb 17 00:07:13 2021

"""
# 引数のデフォルト値

def introduce(unko,name="村人",):#(変数="**")で、引数のデフォルト値　　
    print("私は"+name+"です."+unko)

introduce("エスパー","嘘です")#私はエスパーです.


def intro(name):#(変数="**")で、引数のデフォルト値　　
    print("私は"+name+"です.")
intro("村人")#私は村人です.


def introduce(greeting, *names):#アスタリスクをつける
    for name in names:
        print("私は" + name + "です。" + greeting)

introduce("こんにちは", "勇者", "村人", "兵士")
"""
私は勇者です。こんにちは
私は村人です。こんにちは
私は兵士です。こんにちは
"""

def introduce(**people):
    for name, greeting in people.items():
        print("私は" + name + "です。" + greeting)

introduce(hero = "はじめまして", villager = "こんにちは", soldier = "よろしくお願いします")
"""
私はheroです。はじめまして
私はvillagerです。こんにちは
私はsoldierです。よろしくお願いします
"""

