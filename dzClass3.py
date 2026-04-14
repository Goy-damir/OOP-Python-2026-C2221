class Character:
    def __init__(self, armor, hp, regdamage):
        self.armor = armor
        self.hp = hp
        self.regdamage = regdamage
    def Deffend(self):
        self.hp -= 10
        self.armor -= 20
        print("your hp = ", (self.hp), "and your armor = ", (self.armor))
    def Attack(self):
        self.regdamage = 10
        print("your regdamage = ", (self.regdamage))

class Weird(Character):
    def __init__(self, armor, hp, regdamage, mgdamage, mgArmor):
        self.armor = armor
        self.hp = hp
        self.regdamage = regdamage
        self.mgdamage = mgdamage
        self.mgArmor = mgArmor
    def Deffend(self):
        self.mgArmor -= 40
        print("your hp = ", (self.hp), "and your armor = ", (self.armor))
        print("your magic armor = ", (self.mgArmor))
    def Attack(self):
        self.mgdamage = 30
        print("your magic damage = ", (self.mgdamage))

c = Character(50, 100, 10)
w = Weird(50, 100, 10, 15, 60)
c.Attack()
c.Deffend()
w.Attack()
w.Deffend()
