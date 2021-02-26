class Player:
    def __init__(self, name):
        self.name = name

    def attack(self, enemy):
        print(self.name + "は、" + enemy + "を攻撃した！")

class Wizard(Player):
    def __init__(self):
        super().__init__("魔法使い")

    def attack(self, enemy):
    self.__spell()←#プライベートメッソドは、クラス外では、呼び出せないため"""
    """"同じクラス内で呼び出す"""
        print(self.name + "は、" + enemy + "に炎を放った！")

    def __spell(self):
        print("ズバーン！")

print("=== パーティーでスライムと戦う ===")

hero = Player("勇者")
warrior = Player("戦士")
wizard = Wizard()

party = [hero, warrior, wizard]
for member in party:
    member.attack("スライム")

