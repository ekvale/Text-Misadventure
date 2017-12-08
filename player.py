import items
import world
import random
import pyglet
import ascii
import enemies

class Player:
    def __init__(self):
        self.inventory = [items.sharpStick(), items.CrustyBread(), items.lionCloth()]
        self.cauldron = []
        self.x = world.start_tile_location[0]
        self.y = world.start_tile_location[1]
        self.pcname = "The Forgotten One"
        self.pcClass = "Cave Explorer-- Starting to regret this life decision..."
        self.hp = 100
        self.mp = 0
        self.gold = 66
        self.mana = 0
        self.victory = False
        self.experience = 0
        self.lvl = 0
    def is_alive(self):
        return self.hp > 0

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def move_north(self):
        self.move(dx=0, dy=-1)

    def move_south(self):
        self.move(dx=0, dy=1)

    def move_east(self):
        self.move(dx=1, dy=0)

    def move_west(self):
        self.move(dx=-1, dy=0)

    def transport_to_nine(self):
        self.move(dx=1, dy=3)

    def transport_to_six(self):
        self.move(dx=-1, dy=-3)

    def print_inventory(self):

        print("***************************** \n"
              "Inventory: ")
        for item in self.inventory:
            print('*********' + str(item) + "*****")
            print(item.description)

    def character_info(self):
        print(ascii.pc)
        print(self.pcname)
        print(self.pcClass)
        print("Gold: {}".format(self.gold))
        print("Mana: {}".format(self.mana))
        print("Experience: {}".format(self.experience))
        best_armor = self.most_defensive_armor()
        best_weapon = self.most_powerful_weapon()
        print("Your best weapon is your {} with {} damage.".format(best_weapon, best_weapon.damage))
        print("Your best armor is your {} with {} addition to hp".format(best_armor, best_armor.armor_value))
        print("Character HP: {}".format(self.hp))
        print("Character Attack: {}".format(best_weapon.damage))
        print("Level: {}".format(self.lvl))

    def level_up(self):
        levels = [5, 10, 15, 20, 25, 30, 35]
        self.lvl = len([x for x in levels if self.experience > x])
        self.hp = 100 + (1.5 * self.lvl)
        print("You are in {}.".format(self.lvl))

    def naming_stone(self):
        self.pcname = str(input("What is your name?"))
        self.pcClass = str(input("What is your class: (W)arrior, (M)age, or (R)ouge?"))
        if self.pcClass == "W" or "w":
            self.pcClass = "Warrior"
        elif self.pcClass == "M" or "m":
            self.pcClass = "Mage"
        else:
            self.pcClass = "Rouge"



    def most_powerful_weapon(self):
        max_damage = 0
        best_weapon = None
        for item in self.inventory:
            try:
                if item.damage > max_damage:
                    best_weapon = item
                    max_damage = item.damage * (self.lvl * 1.25)
            except AttributeError:
                pass
        return best_weapon

    def most_defensive_armor(self):
        max_defense = 0
        best_armor = None
        for item in self.inventory:
            try:
                if item.armor_value > max_defense:
                    best_armor = item
                    max_defense = item.armor_value
                    self.hp = self.hp + max_defense
            except AttributeError:
                pass
        return best_armor

    def attack(self):
        best_weapon = self.most_powerful_weapon()
        room = world.tile_at(self.x, self.y)
        enemy = room.enemy
        print("You use {} against {} for {} damage!".format(best_weapon.name,
                                              enemy.name, best_weapon.damage))
        enemy.hp -= best_weapon.damage
        if not enemy.is_alive():
            print("You killed {}.".format(enemy.name))
            self.level_up()
        else:
            print("{} HP is {}.".format(enemy.name, enemy.hp))


    def heal(self):
        consumables = [item for item in self.inventory
                       if isinstance(item, items.Consumable)]
        if not consumables:
            print("You don't have any items to heal you!")
            return
        for i, item in enumerate(consumables, 1):
            print("Choose an item to use to heal: ")
            print("{}.{}".format(i, item))

        valid = False
        while not valid:
            choice = input("")
            try:
                to_eat = consumables[int(choice)-1]
                self.hp = min(100, self.hp + to_eat.healing_value)
                self.inventory.remove(to_eat)
                print("Current HP: {}".format(self.hp))
                valid = True
            except(ValueError, IndexError):
                print("Invalid choice, try again.")

    def modify_player(self, player):
        if self.enemy.is_alive():
            player.hp = player.hp - self.enemy.damage
            print("Enemy does {} damage. You have {} HP remaining.".format(self.enemy.damage, player.hp))
    def heal(self):
        consumables = [item for item in self.inventory
                       if isinstance(item, items.Consumable)]
        if not consumables:
            print("You don't have any items to heal you!")
            return
        for i, item in enumerate(consumables, 1):
            print("Choose an item to use to heal: ")
            print("{}.{}".format(i, item))

        valid = False
        while not valid:
            choice = input("")
            try:
                to_eat = consumables[int(choice)-1]
                self.hp = min(100, self.hp + to_eat.healing_value)
                self.inventory.remove(to_eat)
                print("Current HP: {}".format(self.hp))
                valid = True
            except(ValueError, IndexError):
                print("Invalid choice, try again.")

    def modify_player(self, player):
        if self.enemy.is_alive():
            player.hp = player.hp - self.enemy.damage
            print("Enemy does {} damage. You have {} HP remaining.".format(self.enemy.damage, player.hp))

    def trade(self):
        room = world.tile_at(self.x, self.y)
        room.check_if_trade(self)
    def getquest(self):
        room = world.tile_at(self.x, self.y)
        room.check_if_trade(self)

    def drop_item(self):
        quest_item = [item for item in self.inventory if isinstance(item, items.QuestItem)]
        if not quest_item:
            print("You don't have anything for the cauldron!")
            return
        for i, item in enumerate(quest_item, 1):
            print("Choose an item to drop into the pot: ")
            print("{}.{}".format(i, item))


        valid = False
        while not valid:
            choice = input("")
            try:
                to_drop = quest_item[int(choice)-1]
                print("You have dropped {} into the witches cauldron.".format(to_drop.name))
                self.cauldron.append(to_drop)
                self.inventory.remove(to_drop)
                valid = True
            except(ValueError, IndexError):
                print("Invalid choice, try again.")

    def pick_up_item(self):
        quest_item = [item for item in self.cauldron if isinstance(item, items.QuestItem)]
        if not quest_item:
            print("You don't have anything in the cauldron!")
            return
        for i, item in enumerate(quest_item, 1):
            print("Choose an item to pick out of the pot: ")
            print("{}.{}".format(i, item))
        valid = False
        while not valid:
            choice = input("")
            try:
                to_pick = quest_item[int(choice) - 1]
                print("You have plucked {} out of the witches cauldron. But, it's wet now... gross"
                      "and you have burns on your fingers,"
                      "and there is a bit of newt parts stuck to your forearm...".format(to_pick.name))
                self.cauldron.remove(to_pick)
                self.inventory.append(to_pick)
                valid = True
            except(ValueError, IndexError):
                print("Invalid choice, try again.")

    def look_around(self):
        print("You begin to search the cavern, turning over every stone looking behind every stalagmite... when...")
        rand = random.randrange(10)
        if rand < 4:
            print("You found a couple of worms, which you ate... No effect.")
        elif rand < 7:
            print("You got bit by giant centipedes.")
            sting = random.randrange(10)
            self.hp = self.hp - sting
            print("You lost {} and have {} life left.".format(sting, self.hp))
        else:
            print("You found a large geode, this may fetch a pretty penny."
                  "You put it in your inventory.")
            self.inventory.append(items.geode())

    def speak(self):
        if self.lvl < 4:
            #spookywitch = pyglet.media.load("resources/witchgroan.wav", streaming=False)
            #spookywitch.play()
            print("I'd beat thee but I'd infect my hands...' The witch snarls")
            print("You get the feeling, the witches will not help for now.")
        else:
            print("You have been a good adventurer, now take this... we grow impatient.")
            self.inventory.append(items.shieldOfXichulu())
            print(ascii.shield)
            print("You have been given the legendary Shield of Xichulu!")

    def help(self):
        print("""
        1. The goblins are there to help... 
        2. You get mana from exploring...
        3. Feel free to help me with comments and suggestions.
        Please send commments or suggestions to ekvale@gmail.com
        
        
        
        """)
    def riddle(self):
        print("""It has a golden head 
            It has a golden tail 
                but it has no body?""")
        answer = "A golden coin" or "Golden coin" or "A golden coin" or "golden coin" or "gold coin" or "a gold coin"
        guess = input("What sayest thou?")
        if guess == answer:
            print("Right you are, please accept this gift. It is most rare, The Gawain Sword")
            ##fanfare = pyglet.media.load("resources/fanfare.wav", streaming=True)
            ##fanfare.play()
            print(ascii.sword)
            self.inventory.append(items.gawainSword())
        else:
            self.hp = self.hp - 75
            print("Ethereal fire leaps from hilt of a great sword and scalds your body with it's heat. ")
            print("Hp".format(self.hp))
            return "Only the wise shall receive great power."

    def burnt_offerings(self):
        print("""Do you wish to leave burnt offerings?""")
        choice = input("(Y)es or (N)o")
        if choice == "Y" or "y":
            print("Curious smell... Hemlock, dried burdock and a trace of frog... no human flesh."
                  "Must be something more too it.")
        else:
            print("Probably smart, I mean dark gods don't usually come bearing gifts... or do they?")


    def quit(self):
        quit()

