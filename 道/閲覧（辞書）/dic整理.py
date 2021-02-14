# -*- coding: utf-8 -*-
"""
Created on Sun Feb 14 23:35:19 2021

"""


weapons={"イージスソード":40,"ウィンドスピア":12,"アースブレイカー":99}
print(weapons)

#あいうえお順に並べる+list化
print(sorted(weapons))

print(weapons)

#辞書とキーのセットで表示（タプル：内容の更新負荷）
print(sorted(weapons.items()))