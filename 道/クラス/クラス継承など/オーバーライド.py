"""
オーバーライドとは親クラスと同じ名前のメソッドを子クラスで新たに定義することで、
子クラスで定義されたメソッドが優先"""

#今回の場合は、open

class Box:
    def __init__(self, item):
        self.item = item

    def open(self):
        print("宝箱を開いた。" + self.item + "を手に入れた。")

class Magicbox(Box):
    """def look (self):
        print("宝箱は輝いている")"""
    
    def open(self):
        print("宝箱を開いた。"+self.item+"が襲ってきた")

box = Box("鋼鉄の剣")
box.open()#宝箱を開いた。鋼鉄の剣を手に入れた。

magicbox=Magicbox("モンスター")

"""magicbox.look()#宝箱は輝いている"""
magicbox.open()#宝箱を開いた。モンスターが襲ってきた（openメッソドを書き換える感じ)
