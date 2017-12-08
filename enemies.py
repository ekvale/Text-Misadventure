import random
import player
import items
import ascii

class Enemy:
    def __init__(self):
        raise NotImplementedError("Do not create raw Enemy objects.")

    def __str__(self):
        return self.name

    def is_alive(self):
        return self.hp > 0


class Kikimora(Enemy):

    def __init__(self):
        self.name = "Kikimora"
        self.hp = 10
        self.damage = random.randrange(5)
        self.image = ascii.kikimora
class GingerBreadMan(Enemy):
    def __init__(self):
        self.name = "The Gingerbread Man"
        self.hp = 25
        self.damage = random.randrange(25)
        self.image = ascii.gingerbreadman


class ToNoMe(Enemy):
    def __init__(self):
        self.name = "To-No-Me"
        self.hp = 3
        self.damage = random.randrange(10)
        self.image = ascii.tonome

class Tesso(Enemy):
    def __init__(self):
        self.name = "Tesso"
        self.hp = 10
        self.damage = random.randrange(15)
        self.image = ascii.Tess


class Tsuchinoko(Enemy):
    def __init__(self):
        self.name = "Tsuchinoko"
        self.hp = 80
        self.damage = random.randrange(30)
        self.image = ascii.Tsuchinoko

class GingerBreadLord(Enemy):
    def __init__(self):
        self.name = "GingerBreadLord"
        self.hp = 1000
        self.damage = random.randrange(5)
        self.image = ascii.gingerbreadlord

class WhiteDragon(Enemy):
    def __init__(self):
        self.name = "Xichulu, The Blood-Letter"
        self.hp = 800
        self.damage = random.randrange(125)
        self.image = ascii.dragonhead

class BlackDragon(Enemy):
    def __init__(self):
        self.name = "Old Man of One Thousand Iron Tears"
        self.hp = 1600
        self.damage = random.randrange(176)
        self.image = ascii.oldman