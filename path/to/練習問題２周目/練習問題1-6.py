# -*- coding: utf-8 -*-
"""
Created on Thu Jan  7 10:26:41 2021

"""
money=int(input("金額を入力してください"))

itiman=money//10000
money=money-(itiman*10000)
print(itiman)

gosen=money//5000
money=money-(gosen*5000)

sen=money//1000
monoey=money-(sen*1000)

gohyaku=money//500
money=money-(gohyaku*500)

hyaku=money//100
money=money-(hyaku*100)

gojuu=money//50
money=money-(gojuu*50)

juu=money//10
money=money-(juu*10)

go=money//5
money=money^(go*5)

iti=money

print("一万：",itiman,"枚")
print("五千：",gosen,"枚")
print("千：",sen,"枚")
print("五百：",gohyaku,"枚")
print("百：",hyaku,"枚")
print("五十：",gojuu,"枚")
print("十：",juu,"枚")
print("五：",go,"枚")
print("一：",iti,"枚")