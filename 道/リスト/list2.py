# -*- coding: utf-8 -*-
"""
Created on Sat Feb 13 16:12:45 2021

"""

import sys
enemy=input()
for line in sys.stdin.readlines():
	# ここに、文字列を分割して、出力するコードを書く
	enemy = line.rstrip().split(",")
	print(enemy[0]+"が"+enemy[1]+"匹現れた")