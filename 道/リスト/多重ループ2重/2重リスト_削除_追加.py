# -*- coding: utf-8 -*-
"""
Created on Mon Feb 15 09:49:32 2021
"""


teams = [["勇者", "戦士"], ["盗賊", "忍者", "商人"], ["スライム", "ドラゴン", "魔王"], ["魔法使い"]]
print(teams)

teams.append(["メタルモンスター", "シルバーモンスター", "ブラックモンスター"])
print(teams)
print(len(teams))

#要素を特定の場所に追加
teams[0].append("レッドドラゴン")
print(teams)
print(len(teams))
print(len(teams[0]))

#要素の削除
del teams[1]
print(teams)
print(len(teams))

del teams[0][1]
print(teams)
print(len(teams))
print(len(teams[0]))

