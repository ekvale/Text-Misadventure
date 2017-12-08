import random

class Weapon:
    def __init__(self):
        raise NotImplementedError("Do not create raw Weapon objects")

    def __str__(self):
        return self.name

class gawainSword(Weapon):
    def __init__(self):
        self.name = "The Gawain Sword"
        self.description = "Forged for one purpose and one destiny... to kill dragons!"
        self.damage = random.randrange(200, 1000)
        self.value = 5000

class sharpStick(Weapon):
    def __init__(self):
        self.name = "Stick"
        self.description = "A stick that has been whittled to a point. Good for poking"
        self.damage = 10
        self.value = 1

class ironaxe(Weapon):
    def __init__(self):
        self.name = "Deadly Axe"
        self.description = "An axe with a finely honed edge, and a good firm stock."
        self.damage = random.randrange(50)
        self.value = 100

class blackMagicSword(Weapon):
    def __init__(self):
        self.name = "Sword of Black Skull"
        self.description = "A sword with a shrunken head at the base of the hilt. Looks sharp. Might be cursed?"
        self.damage = random.randrange(75)
        self.value = 1
class geode(Weapon):
    def __init__(self):
        self.name = "Geode"
        self.description = "A large geode, good for smashing, great for selling"
        self.damage = random.randrange(20)
        self.value = 300
class QuestItem:
    def __init__(self):
        raise NotImplementedError("Do not create raw Quest Item objects.")

    def __str__(self):
        return self.name

class Toe(QuestItem):
    def __init__(self):
        self.name = "Toe"
        self.description = "A giants toe that has been removed from a human-like foot."
        self.damage = 1
        self.value = 10
class Eye(QuestItem):
    def __init__(self):
        self.name = "Eye"
        self.description = "A wizard eyeball removed from it's socket, it throbs with magical power."
        self.damage = 2
        self.value = 10
class lizardLeg(QuestItem):
    def __init__(self):
        self.name = "Lizard Leg"
        self.description = "A disarticulated section of a rather large lizards leg."
        self.damage = 4
        self.value = 10
class owletWing(QuestItem):
    def __init__(self):
        self.name = "Owlet Wing"
        self.description = "A small feathery wing"
        self.value = 10

class catHair(QuestItem):
    def __init__(self):
        self.name = "Cat Hair"
        self.description = "Wet sticky, smells bad. A clump of hair."
        self.value = 10


class Consumable:

    def __init__(self):
        raise NotImplementedError("Do not create raw Consumable objects.")

    def __str__(self):
        return"{}(+{} HP)".format(self.name, self.healing_value)

class CrustyBread(Consumable):
    def __init__(self):
        self.name = "Crusty Bread"
        self.description = "Stale, but still void of mold. Good enough."
        self.healing_value = 10
        self.value = 10

class HealingPotion(Consumable):
    def __init__(self):
        self.name = "Healing Potion"
        self.description = "An elixir with some questiable floaties in it... looks fine..."
        self.healing_value = random.randrange(75)
        self.value = 120

class ScrollofMajorHealing(Consumable):
    def __init__(self):
        self.name = "Scroll of Healing Armor"
        self.description = "Reads... Klaatu-barada-nikto... Or something pretty close to that."
        self.healing_value = 200
        self.value = 200

class GingerBread(Consumable):
    def __init__(self):
        self.name = "Gingerbread"
        self.description = "Parts of the recently slain gingerbread man. It's still bleeding, but it bleeds frosting" \
                           "so not all bad!"
        self.healing = 10
        self.value = 15

class Armor:
    def __init__(self):
        raise NotImplementedError("Do not create raw Consumable objects.")

    def __str__(self):
        return"{}+{} HP)".format(self.name, self.armor_value)

class lionCloth(Armor):
    def __init__(self):
        self.name = "A tattered banana hammock made out of a potato sack"
        self.description = "You wonder if the witches might not have took your clothing while you were out..." \
                    "at least they left you with this...rag."
        self.armor_value = 1
        self.value = 1

class snakeLeatherHelmet(Armor):
    def __init__(self):
        self.name = "Snake Leather Helmet"
        self.description = "It smells terrible, but the scales offer protection, \n" \
                       " and elasticity of fresh snake skin really helps with the fit."
        self.armor_value = 75
        self.value = 250

class ratPelt(Armor):
    def __init__(self):
        self.name = "Rat Pelt"
        self.description = "A quilt of rat hides sown together with tendons, suprisingly warm."
        self.armor_value = 45
        self.value = 120

class shieldOfXichulu(Armor):
    def __init__(self):
        self.name = "The Xichulu Shield"
        self.description = "The Legendary Shield of Xichulu"
        self.armor_value = 650
        self.value = 4000

class Enchanted:
    def __init__(self):
        raise NotImplementedError("Do not create raw Weapon objects")

    def __str__(self):
        return self.name

class enchantedCrown(Enchanted):
    def __init__(self):
        self.name = "The Enchanted Crown of Xichulu"
        self.description = "The Crown of Ancient Xichulu"
        self.armor_value = 10000
        self.mp = 500
        self.value = 1000000
