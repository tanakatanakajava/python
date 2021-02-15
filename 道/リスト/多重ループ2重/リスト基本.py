# -*- coding: utf-8 -*-
"""
Created on Mon Feb 15 09:18:04 2021

"""

# 2次元リストを作成する

player = "忍者"
team_a = [player, "戦士", "魔法使い"]
print(team_a)
print(team_a[1])

team_b = [team_a[0], team_a[1], team_a[2]]
print(team_b)
print(team_b[0])

team_c = ["勇者", "戦士", "魔法使い"]
team_d = ["盗賊", "忍者", "商人"]
team_e = ["スライム", "ドラゴン", "魔王"]

teams = [team_c, team_d, team_e]
print(teams)
print(teams[1])#['盗賊', '忍者', '商人']
print(teams[2][0])#スライム
print(teams[2][1])#ドラゴン
print(teams[2][2])#魔王
