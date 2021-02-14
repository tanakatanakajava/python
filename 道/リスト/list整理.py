# -*- coding: utf-8 -*-
"""
Created on Sun Feb 14 20:48:53 2021
"""
# リストの整列
wepon=["イージスソード","ウィンドスピア","アースブレイカー","稲妻ハンマー"]
print(wepon)

#あいうえお順に表示させる
print(sorted(wepon))

#さっきと逆順
print(sorted(wepon,reverse=True))

#数字で並び替え
wepon2=["4.イージスソード","1.ウィンドスピア","3.アースブレイカー","2.稲妻ハンマー"]
print(sorted(wepon2))

#同じ数字の場合は、あいうえお順で並べる
#漢字やカタカナの場合は文字コード順
wepon2=["4.イージスソード","1.ウィンドスピア","1.アースブレイカー","2.稲妻ハンマー"]
print(sorted(wepon2))

