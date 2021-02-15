# -*- coding: utf-8 -*-
"""
Created on Mon Feb 15 09:33:18 2021

"""
team_a = ["勇者", "戦士"]
team_b = ["盗賊", "忍者", "商人"]
team_c = ["スライム", "ドラゴン", "魔王"]
team_d = ["鷹","虎","バッタ"]    
teams=[team_a,team_b,team_c,team_d]
"""print(teams)
print(teams[0])
print(teams[0][1])"""

#要素の更新（置き換え）
teams[0][0]="魔導士"
print(teams)
#リストの長さ
print(len(teams))#team_a~dの敬4つ
print(len(teams[0]))#team_aの要素2つ
