import random
import enemies
import npc
import items
import pyglet
import player
import ascii

class MapTile:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.roomsafe = []

    def intro_text(self):
        raise NotImplementedError("Create a subclass instead!")

    def modify_player(self, player):

        pass


class BossTile(MapTile):
    def __init__(self, x, y):
            self.enemy = enemies.WhiteDragon()
            self.alive_text = "A looming specter of death, an avalance of pain, a demi-God, the " \
                              "bringer of death... Xichula"

            self.dead_text = "The unholy corpse of Xichula" \
                             " is strewn across the ground." \
                "You scoop up some more treasure, filtering out the guts and scales as you go along."

            super().__init__(x, y)

    def intro_text(self):
        text = self.alive_text if self.enemy.is_alive() else self.dead_text

        return text

    def modify_player(self, player):
        if self.enemy.is_alive():
            ##dragongrowl = pyglet.media.load("resources/dragonnoise.wav", streaming=False)
            print(ascii.dragonhead)
            ##dragongrowl.play()
            player.hp = player.hp - self.enemy.damage
            print("Enemy does {} damage. You have {} HP remaining.".format(self.enemy.damage, player.hp))



class StartTile(MapTile):
    def __init__(self, x, y):
        self.first_time = False
        super().__init__(x, y)




    def modify_player(self, player):
        self.first_time = True
        if items.Eye in player.cauldron:
            print("Yes, you are almost there, my toad, my warted Hero...")
        if len(player.cauldron) >= 5:
            player.victory = True

            print("""
                The witches look at your items with suspicion,
                 but decide to go through with the incantation of the spell:
        **************************** 
                Take lizard's leg and owlet's wing,
                      And hair of cat that used to sing,
                      In the cauldron they all shall go;
                        Stirring briskly, to and fro.    
                    When the color is of a hog,    
                    Add eye of newt and toe of frog.     
                    Bubble all i' the charmed pot;    
                    Bubble all 'til good and hot.    
                    Pour the broth into a cup of stone,    
                    And stir it well with a mummy's bone.
                    
                    You take the resulting broth offered to you and drink...
         As the fog clears, you find yourself at a computer terminal;
        your adventure is at an end.""")




    def intro_text(self):
        if self.first_time:
            return """
            The witches stand before you, glaring; they seem to be expecting something from you. """
        else:
            return """
    
    The witches speak in unison:
    "Mortal, we have summoned thee, make haste!
    And go forth into the farrow'd waste.
    Find eye of newt, and toe of frog,
    And deliver thus to this Scottish bog.
    Lizard's leg, and owlet's wing,
    And hair of cat that used to sing.
    Bring them forth --and suffer no 'arm.
    Leave us and go!
    'Tis no more to be said,
    Save if you fail, then thou be stricken, dead.
    ***********************************************
    """

class VictoryTile(MapTile):
    def __init__(self, x, y):
            self.enemy = enemies.GingerBreadLord()


            super().__init__(x, y)

    def intro_text(self):
        living = "A Gingerbread Lord attacks!"
        living_intro = "The sticky handed bandit has positioned himself, " \
                       "sharpening a candy-cane shiv" \
                 "while slouching against a marble arch. " \
                 "He lurches forward with executing a lethal ginger chop. " \
                "This is not your grandmas cookie."
        barrier = "Previously obstructed by the delicious villain," \
                  " you discover a marble arch with a wizards seal" \
                  " blocking all entry. " \
                  "You spy an inscription on a nearby shrine. It reads: 'XICHULU'"

        if self.enemy.is_alive() and self.enemy.hp > 999:
            print(living_intro)

        text = living if self.enemy.is_alive() else barrier

        return text

    def modify_player(self, player):
        if self.enemy.is_alive():
            xran = random.randrange(100)
            if xran < 25:
                print("The Gingerbead Lord leaps high into the air, and plunges from a great depth at you"
                      "with his candy-cane saber-- licked to a deadly point!")
            elif xran < 50:
                print("The Gingerbread Lord prances toward you."
                      "He leaps at you daintily with a lethal canter.")
            elif xran < 75:
                "'Come a little closer' the Gingerbread Lord taunts, 'The oven is still warm!"
            else:
                print("I plunge my doughed hands at you, I lick at you with frosted tongue," 
                "I hit, and scourge and scour and scrub," 
                "You will not survive my sugared threat" 
                " MY dough it RISES!")
            print(ascii.gingerbreadlord)
            player.hp = player.hp - self.enemy.damage
            print("Enemy does {} damage. You have {} HP remaining.".format(self.enemy.damage, player.hp))
            player.inventory.append(items.GingerBread())

class TraderTile(MapTile):
    def __init__(self, x, y):
        self.trader = npc.Trader()
        super().__init__(x, y)

    def trade(self, buyer, seller):
        for i, item in enumerate(seller.inventory, 1):
            print("{}. {} - {} Gold".format(i, item.name, item.value))
            while True:
                user_input = input("Choose an item or press Q to exit ")
                if user_input in ["Q", "q"]:
                    return
                else:
                    try:
                        choice = int(user_input)
                        to_swap = seller.inventory[choice - 1]
                        self.swap(seller, buyer, to_swap)
                    except ValueError:
                        print("Invalid choice!")

    def swap(self, seller, buyer, item):
        if item.value > buyer.gold:
            print("That's too expensive")
            return
        seller.inventory.remove(item)
        buyer.inventory.append(item)
        seller.gold = seller.gold + item.value
        buyer.gold = buyer.gold - item.value
        print("Trade complete!")

    def check_if_trade(self, player):
        while True:
            print("Would you like to (B)uy, (S)ell, or (Q)uit?")
            user_input = input()
            if user_input in ["Q", "q"]:
                return
            elif user_input in ["B", "b"]:
                print("Here's whats available to buy: ")
                self.trade(buyer=player, seller=self.trader)
            elif user_input in ["S", 's']:
                print("Here's whats available to sell: ")
                self.trade(buyer=self.trader, seller=player)
            else:
                print("Invalid choice!")

    def intro_text(self):
        return """
        
        A diminutive creature with leaden eyes and soft-tufts of fur shooting from his elfin ears. Sits
        behind a shoddy wodden cart. He taps the bottom of bag of coins.
         "Yes, I am the trader your are looking for... 
        I have many wears... May I interest in you my wears?
         Or perhaps you've something to offer?" """

class EnemyTile(MapTile):
    def __init__(self, x, y):
        self.already_dead = False
        loot = [items.ratPelt(), items.snakeLeatherHelmet(), items.ScrollofMajorHealing(), items.CrustyBread(),
                items.blackMagicSword(),
                items.ironaxe(), items.ratPelt()]
        self.loot = random.choice(loot)
        r = random.random()
        if r < 0.25:
            self.enemy = enemies.GingerBreadMan()
            self.alive_text = """A wild Gingerbread Man appears! \n
                               He taunts you with his sugary hand! \n 
                                 He blinds you with his powdered sugar! \n 
                            He imprisons you in sticky residue. You break free! \n
                            """
            self.dead_text = """
                            A man he was, how sweet he was, \n 
                              dead err his prime, \n
                                and now all that's left of this man is sweetness and grime.\n
                                    He's off to candycane arches in fairyfloss clouds\n
                              Where milkshakes rivers flow...\n"""
        elif r < 0.50:
            self.enemy = enemies.Kikimora()
            self.alive_text = "The ghastly apparation of a Kikimora appears!" \
                              "Her giant crow feet scratch out with razor sharp claws."
            self.dead_text = "The corpse of a Kikimora" \
                             " rots on the ground."
        elif r < 0.80:
           self.enemy = enemies.ToNoMe()
           self.alive_text = "A blind man appears... No, his eyes are sown into his hands! He unleashes an other worldly" \
                             " moan, and rushes at you"
           self.dead_text = " A the blind mans corpse lies in front of you, but the eyes in hands still blink."
        elif r < 0.95:
            self.enemy = enemies.Tesso()
            self.alive_text = 'Suddenly, the cave is overcome with a plague of rats! They rush at you in mass!'
            self.dead_text = " An enormous pile of dead rats litters the cave floor."
        else:
            self.enemy = enemies.Tsuchinoko()
            self.alive_text = "A cryptid serpintine demon, rears it's ancient head."
            self.dead_text = " The skin of Tsuchinoko lies here, the bones and body have mysteriously left."

        super().__init__(x, y)



    def intro_text(self):
        text = self.alive_text if self.enemy.is_alive() else self.dead_text

        return text

    def modify_player(self, player):
        if self.enemy.is_alive():
            print(self.enemy.image)
            player.hp = player.hp - self.enemy.damage
            print("Enemy does {} damage. You have {} HP remaining.".format(self.enemy.damage, player.hp))
            player.mana += 1
            print("+{} mana increased.".format(player.mana))
            kill_count = 0
        if not self.enemy.is_alive() and self.already_dead == False:
            "You defeated {}!".format(self.enemy.name)
            self.gold = random.randint(1, 50)
            player.gold = player.gold + self.gold
            print("+{} Gold.".format(self.gold))
            self.experience = random.randrange(1, 10)
            player.experience = player.experience + self.experience
            print("+{} EXP".format(self.experience))
            player.inventory.append(self.loot)
            print("You search {}, and found a {} among their body.".format(self.enemy, self.loot))
            self.already_dead = True




class FindGoldTile(MapTile):
    def __init__(self, x, y):
        self.gold = random.randint(1, 50)
        self.gold_claimed = False
        super().__init__(x, y)

    def modify_player(self, player):
        if not self.gold_claimed:
            self.gold_claimed = True
            player.mana += 1
            player.gold = player.gold + self.gold
            print("+{} mana increased.".format(player.mana))
            #foundcoins = pyglet.media.load("resources/foundcoins.wav", streaming=False)
            #foundcoins.play()
            print("+{} gold added.".format(self.gold))
        else:
            self.looked_already = False
            rand = random.randrange(10)
            if self.looked_already == False and rand > 5:
                print("While searching you are pricked by a posioned bush."
                      "************************************************")
                player.hp -= random.randrange(50)
                print("Ouch, you have {} HP remaining"
                      "******************************".format(player.hp))
                self.looked_already = True
            elif self.looked_already == False and rand < 5:
                player.gold = player.gold + self.gold
                print("+{} gold added.".format(self.gold))
                self.looked_already = True

    def intro_text(self):
        if self.gold_claimed:
            return"""
            Another unremarkable part of the cave
             you must forge onwards
             
             """
        else:
            return"""
            
            Someone dropped some gold. You pick it up.
            
            """



class ItemTile(MapTile):
    def __init__(self, x, y):
        lst = [items.blackMagicSword(), items.ironaxe(), items.HealingPotion(), items.sharpStick(),
               items.ScrollofMajorHealing(), items.ironaxe(), items.CrustyBread()]
        self.gold = random.randint(1, 10)
        self.lst = random.choice(lst)
        self.looked_already = False
        self.inventory_claimed = False
        super().__init__(x, y)

    def modify_player(self, player):
        if not self.inventory_claimed:
            self.inventory_claimed = True
            player.mana += 1
            print("+{} mana increased.".format(player.mana))
            player.inventory.append(self.lst)
            print("+{} item added.".format(self.lst))

    def intro_text(self):
        if self.inventory_claimed:
            return"""
            Another unremarkable part of the woods
             you must forge onwards"""
        else:
            return"You found {}".format(self.lst.name)
class TenTile(MapTile):
    def __init__(self, x, y):
        self.quest_claimed = False
        self.questgiver = npc.QuestGiver10()
        super().__init__(x, y)

    def getquest(self, buyer, seller):
        for i, item in enumerate(seller.inventory, 1):
            print("{}. {} - {} Gold".format(i, item.name, item.value))
            while True:
                user_input = input("Choose an item or press Q to exit ")
                if user_input in ["Q", "q"]:
                    return
                else:
                    try:
                        choice = int(user_input)
                        to_swap = seller.inventory[choice - 1]
                        self.swap(seller, buyer, to_swap)
                    except ValueError:
                        print("Invalid choice!")

    def swap(self, seller, buyer, item):
        if item.value > buyer.gold:
            print("That's too expensive")
            return
        seller.inventory.remove(item)
        buyer.inventory.append(item)
        seller.gold = seller.gold + item.value
        buyer.gold = buyer.gold - item.value
        print("Trade complete!")

    def check_if_trade(self, player):
        while True:
            print("Hello, I am {}, at your service.".format(npc.QuestGiver10().name))
            print("Would you like to (T)rade, (S)ell, or (L)eave?")
            user_input = input()
            if user_input in ["L", "l"]:
                return
            elif user_input in ["T", "t"]:
                print("Here's whats available to trade: ")
                self.getquest(buyer=player, seller=self.questgiver)
            elif user_input in ["S", 's']:
                print("Here's whats available to sell: ")
                self.getquest(buyer=self.questgiver, seller=player)
            else:
                print("Invalid choice!")

    def intro_text(self):
        return print(ascii.goblin1 + """
        You notice a shimmering outline of a mystical being...""")

    def modify_player(self, player):
        if not self.quest_claimed:
            self.quest_claimed = True
            player.mana += 1
            print("+{} mana increased.".format(player.mana))

    def intro_text(self):
        if self.quest_claimed:
            return"""
            Another unremarkable part of the cave
             you must forge onwards... 
             The strange mystical creature is still waiting to talk to you."""
        else:
            return"""You are in the kitchen.
             Looking out into the cafeteria,
              you see students reaching for Pepto-Bismol
               while trying to stomach the latest version of the Chef's Surprise.
                You see the Chef as he finishes dumping fresh meat into his 50-quart stewing pot.
                 There are clumps of cat hair on the butcher's block.
             You hear the Chef muttering to himself, "Prepared properly, cat tastes much like chicken...
             *********************************************************************************************
             There is small ghostly outline of a goblin-like creature in the corner. He beacons you over..."""
class SevenTile(MapTile):
    def __init__(self, x, y):
        self.quest_claimed = False
        self.questgiver = npc.QuestGiver7()
        super().__init__(x, y)

    def getquest(self, buyer, seller):
        for i, item in enumerate(seller.inventory, 1):
            print("{}. {} - {} Gold".format(i, item.name, item.value))
            while True:
                user_input = input("Choose an item or press Q to exit ")
                if user_input in ["Q", "q"]:
                    return
                else:
                    try:
                        choice = int(user_input)
                        to_swap = seller.inventory[choice - 1]
                        self.swap(seller, buyer, to_swap)
                    except ValueError:
                        print("Invalid choice!")

    def swap(self, seller, buyer, item):
        if item.value > buyer.gold:
            print("That's too expensive")
            return
        seller.inventory.remove(item)
        buyer.inventory.append(item)
        seller.gold = seller.gold + item.value
        buyer.gold = buyer.gold - item.value
        print("Trade complete!")

    def check_if_trade(self, player):
        while True:
            print(ascii.aliengoblin)
            print("Hello, I am {}, at your service.".format(npc.QuestGiver7().name))
            print("Would you like to (T)rade, (S)ell, or (L)eave?")
            user_input = input()
            if user_input in ["L", "l"]:
                return
            elif user_input in ["T", "t"]:
                print("Here's whats available to trade: ")
                self.getquest(buyer=player, seller=self.questgiver)
            elif user_input in ["S", 's']:
                print("Here's whats available to sell: ")
                self.getquest(buyer=self.questgiver, seller=player)
            else:
                print("Invalid choice!")

    def modify_player(self, player):
        if not self.quest_claimed:
            self.quest_claimed = True
            player.mana += 1
            print("+{} mana increased.".format(player.mana))

    def intro_text(self):
        if self.quest_claimed:
            return""" Nothing remains of the Flying Circus. Just the smell of burnt frog flesh.
            ****************************************************
            The goblin fixes his piercing black eyes at your being."""
        else:
            return"""
            You find yourself walking into a scene where the cast of
             Monty Python's Flying Circus is performing the "Crunchy Frog" sketch.
              You see the confectioner as he replies,
               "If we took the bones out it wouldn't be crunchy now, would it?"
                You see a box of "Crunchy Frog" chocolates,
                 the contents of which contains a dozen nicely cleaned whole frogs
                  that have been carefully hand-dipped in the finest chocolate.
                  *************************************************************
                  An disfigured goblin fades in and out existence in the corner. He whistles at you."""
class NineTile(MapTile):
    def __init__(self, x, y):
        self.quest_claimed = False
        super().__init__(x, y)

    def modify_player(self, player):
        if not self.quest_claimed:
            player.mana += 1
            print("Your mana: {}.".format(player.mana))
            self.quest_claimed = True


    def intro_text(self):
        if self.quest_claimed:
            return"""
            The time portal is gone... it now looks like any other part of the cave."""
        else:
            return"""As you step through the time portal,
             your head begins to spin you're disoriented and then awaken.
              You find yourself at the outside door of a dormitory kitchen.
               Listening, you hear the Chef yelling,
                "Stop! Stop!" while several cats inside are singing
                 a serenade of the "Meow Mix" commercial theme.
                  Suddenly, the repeated thump of a cleaver puts an abrupt end to the music."""

class TwoTile(MapTile):
    def __init__(self, x, y):
        self.quest_claimed = False
        self.questgiver = npc.QuestGiver2()
        super().__init__(x, y)

    def getquest(self, buyer, seller):
        for i, item in enumerate(seller.inventory, 1):
            print("{}. {} - {} Gold".format(i, item.name, item.value))
            while True:
                user_input = input("Choose an item or press Q to exit ")
                if user_input in ["Q", "q"]:
                    return
                else:
                    try:
                        choice = int(user_input)
                        to_swap = seller.inventory[choice - 1]
                        self.swap(seller, buyer, to_swap)
                    except ValueError:
                        print("Invalid choice!")

    def swap(self, seller, buyer, item):
        if item.value > buyer.gold:
            print("That's too expensive")
            return
        seller.inventory.remove(item)
        buyer.inventory.append(item)
        seller.gold = seller.gold + item.value
        buyer.gold = buyer.gold - item.value
        print("Trade complete!")

    def check_if_trade(self, player):
        while True:
            print(ascii.piggoblin)
            print("Hello, I am {}, at your service.".format(npc.QuestGiver2().name))
            print("Would you like to (T)ake, (D)rop, or (Q)uit?")
            user_input = input()
            if user_input in ["Q", "q"]:
                return
            elif user_input in ["T", "t"]:
                print("Here's whats available to take: ")
                self.getquest(buyer=player, seller=self.questgiver)
            elif user_input in ["D", 'd']:
                print("Here's whats available to drop: ")
                self.getquest(buyer=self.questgiver, seller=player)
            else:
                print("Invalid choice!")

    def modify_player(self, player):
        if not self.quest_claimed:
            self.quest_claimed = True
            player.mana += 1
            print("+{} mana increased.".format(player.mana))

    def intro_text(self):
        if self.quest_claimed:
            return""" You're transported back in time … "
              "you find yourself in Georgia during the midst"
              " of a congressional campaign.
            There is a defaced poster of Newt Gingrich on the wall."""
        else:
            return"""
            You're transported back in time … "
              "you find yourself in Georgia during the midst"
              " of a congressional campaign.
            There is a campaign poster of Newt Gingrich,
             the Speaker of the House of Representatives,
              on the wall, with his large eyes looking right at you."""
class ThreeTile(MapTile):
    def __init__(self, x, y):
        self.quest_claimed = False
        self.questgiver = npc.QuestGiver3()
        super().__init__(x, y)

    def getquest(self, buyer, seller):
        for i, item in enumerate(seller.inventory, 1):
            print("{}. {} - {} Gold".format(i, item.name, item.value))
            while True:
                user_input = input("Choose an item or press Q to exit ")
                if user_input in ["Q", "q"]:
                    return
                else:
                    try:
                        choice = int(user_input)
                        to_swap = seller.inventory[choice - 1]
                        self.swap(seller, buyer, to_swap)
                    except ValueError:
                        print("Invalid choice!")

    def swap(self, seller, buyer, item):
        if item.value > buyer.gold:
            print("That's too expensive")
            return
        seller.inventory.remove(item)
        buyer.inventory.append(item)
        seller.gold = seller.gold + item.value
        buyer.gold = buyer.gold - item.value
        print("Trade complete!")

    def check_if_trade(self, player):
        while True:
            print(ascii.jokergoblin)
            print("Hello, I am {}, at your service.".format(npc.QuestGiver3().name))
            print("Would you like to (T)ake, (D)rop, or (Q)uit?")
            user_input = input()
            if user_input in ["Q", "q"]:
                return
            elif user_input in ["T", "t"]:
                print("Here's whats available to take: ")
                self.getquest(buyer=player, seller=self.questgiver)
            elif user_input in ["D", 'd']:
                print("Here's whats available to drop: ")
                self.getquest(buyer=self.questgiver, seller=player)
            else:
                print("Invalid choice!")

    def modify_player(self, player):
        if not self.quest_claimed:
            self.quest_claimed = True
            player.mana += 1
            print("+{} mana increased.".format(player.mana))

    def intro_text(self):
        if self.quest_claimed:
            return"""
            The ghastly goblin is singing a strange song:
            'Sing of a song of six-pence, Xichulu was a witch, four and twenty-blackbirds,
            dying in the ditch'"""
        else:
            return print(ascii.stonehedge + """
             There is a row of obelisks several meters tall and a witches face carved in all,
             THe blood of something oozes out,
             One statue has it's mouth agape,
             The seems to be humming a tune.
              ***************************************************************
              You notice a shimmering outline of a mystical being...""")
class FourTile(MapTile):
    def __init__(self, x, y):
        self.quest_claimed = False
        self.questgiver = npc.QuestGiver4()
        super().__init__(x, y)

    def getquest(self, buyer, seller):
        for i, item in enumerate(seller.inventory, 1):
            print("{}. {} - {} Gold".format(i, item.name, item.value))
            while True:
                user_input = input("Choose an item or press Q to exit ")
                if user_input in ["Q", "q"]:
                    return
                else:
                    try:
                        choice = int(user_input)
                        to_swap = seller.inventory[choice - 1]
                        self.swap(seller, buyer, to_swap)
                    except ValueError:
                        print("Invalid choice!")

    def swap(self, seller, buyer, item):
        if item.value > buyer.gold:
            print("That's too expensive")
            return
        seller.inventory.remove(item)
        buyer.inventory.append(item)
        seller.gold = seller.gold + item.value
        buyer.gold = buyer.gold - item.value
        print("Trade complete!")

    def check_if_trade(self, player):
        while True:
            print("Hello, I am {}, at your service.".format(npc.QuestGiver4().name))
            print("Would you like to (T)ake, (D)rop, or (Q)uit?")
            user_input = input()
            if user_input in ["Q", "q"]:
                return
            elif user_input in ["T", "t"]:
                print("Here's whats available to take: ")
                self.getquest(buyer=player, seller=self.questgiver)
            elif user_input in ["D", 'd']:
                print("Here's whats available to drop: ")
                self.getquest(buyer=self.questgiver, seller=player)
            else:
                print("Invalid choice!")

    def intro_text(self):
        return """
        You notice a shimmering outline of a mystical being..."""

    def modify_player(self, player):
        if not self.quest_claimed:
            self.quest_claimed = True
            player.mana += 1
            print("+{} mana increased.".format(player.mana))

    def intro_text(self):
        if self.quest_claimed:
            return""" 
             The strange mystical creature is still waiting to talk to you."""
        else:
            return print(ascii.dwarf + """Welcome, welcome... a far off voice is calling out too you. I have something you might want,
            if you'd like to get rid of the witches haunt. I will give it nearly free...
            of course a little gold will go to me.
             *********************************************************************************************
             There is small ghostly outline of a goblin-like creature in the corner. He beacons you over...""")
class EightTile(MapTile):
    def __init__(self, x, y):
        self.quest_claimed = False
        self.questgiver = npc.QuestGiver8()
        super().__init__(x, y)

    def getquest(self, buyer, seller):
        for i, item in enumerate(seller.inventory, 1):
            print("{}. {} - {} Gold".format(i, item.name, item.value))
            while True:
                user_input = input("Choose an item or press Q to exit ")
                if user_input in ["Q", "q"]:
                    return
                else:
                    try:
                        choice = int(user_input)
                        to_swap = seller.inventory[choice - 1]
                        self.swap(seller, buyer, to_swap)
                    except ValueError:
                        print("Invalid choice!")

    def swap(self, seller, buyer, item):
        if item.value > buyer.gold:
            print("That's too expensive")
            return
        seller.inventory.remove(item)
        buyer.inventory.append(item)
        seller.gold = seller.gold + item.value
        buyer.gold = buyer.gold - item.value
        print("Trade complete!")

    def check_if_trade(self, player):
        while True:
            print(ascii.clowngoblin)
            print("Hello, I am {}, at your service.".format(npc.QuestGiver8().name))
            print("Would you like to (T)ake, (D)rop, or (Q)uit?")
            user_input = input()
            if user_input in ["Q", "q"]:
                return
            elif user_input in ["T", "t"]:
                print("Here's whats available to take: ")
                self.getquest(buyer=player, seller=self.questgiver)
            elif user_input in ["D", 'd']:
                print("Here's whats available to drop: ")
                self.getquest(buyer=self.questgiver, seller=player)
            else:
                print("Invalid choice!")

    def intro_text(self):
        return """
        You notice a shimmering outline of a mystical being..."""

    def modify_player(self, player):
        if not self.quest_claimed:
            self.quest_claimed = True
            player.mana += 1
            print("+{} mana increased.".format(player.mana))

    def intro_text(self):
        if self.quest_claimed:
            return print(ascii.clowngoblin + """
            Another unremarkable part of the cave
             you must forge onwards... 
             The strange mystical creature is still waiting to talk to you.""")
        else:
            return print(ascii.candles, """A few lit candles, and some a turned over table and chairs... and not much more...
             *********************************************************************************************
             There is small ghostly outline of a goblin-like creature in the corner. He beacons you over...""")


class SixTile(MapTile):
    def __init__(self, x, y):
            self.enemy = enemies.BlackDragon()
            super().__init__(x, y)
    def modify_player(self, player):
        pass

    def summoning(self):
        enemies.BlackDragon()

    def intro_text(self):
        return """
        Something is strange about this room, it glows an errie red. The walls seem to breath in and out with your 
        own breath. There is a floating mirror in the center of the room. There is a small glowing alter with
         burnt offerings on an inlaid alter. 
        """


class FiveTile(MapTile):
    def __init__(self, x, y):
        self.quest_claimed = False
        self.questgiver = npc.QuestGiver8()
        super().__init__(x, y)


    def intro_text(self):
        quest_claimed = False
        if quest_claimed:
            return """
            You still remember they day you were honored to receive such a precious gift,
            now bath it in the blood it was born for."""
        else:
            return """
        As you traverse what looks like an impassable rock face, you accidentally put you hand on an old urn.
        If falls and crashes on the craggy rocks below. Upon inspection you find a cartouche. You decipher some text,
        it's a riddle. Do you dare attempt it? 
        
        """



world_dsl = """
|  |  |VT|  |  |  |  |  |
|  |  |EN|  |  |  |  |  |
|  |  |EN|  |  |  |  |  |
|  |05|EN|EN|EN|  |  |  |
|02|02|03|04|EN|FG|FG|BL|
|07|FG|ST|06|TT|  |  |  |
|  |  |08|EN|EN|  |  |  |
|  |  |  |  |  |  |  |  |
|  |  |  |10|09|  |  |  |
"""

def is_dsl_valid(dsl):
    if dsl.count("|ST|") != 1:
        return False
    if dsl.count("|VT|") == 0:
        return False
    lines = dsl.splitlines()
    lines = [l for l in lines if l]
    pipe_counts = [line.count("|") for line in lines]
    for count in pipe_counts:
        if count != pipe_counts[0]:
            return False

    return True
tile_type_dict = {"VT": VictoryTile,
                  "EN": EnemyTile,
                  "ST": StartTile,
                  "FG": FindGoldTile,
                  "TT": TraderTile,
                  "IT": ItemTile,
                  "BL": BossTile,
                  "10": TenTile,
                  "09": NineTile,
                  "08": EightTile,
                  "07": SevenTile,
                  "06": SixTile,
                  "05": FiveTile,
                  "04": FourTile,
                  "03": ThreeTile,
                  "02": TwoTile,
                  "  ": None}
world_map = []
start_tile_location = None

def parse_world_dsl():
    if not is_dsl_valid(world_dsl):
        raise SyntaxError("DSL is invalid!")

    dsl_lines = world_dsl.splitlines()
    dsl_lines = [x for x in dsl_lines if x]

    for y, dsl_row in enumerate(dsl_lines):
        row = []
        dsl_cells = dsl_row.split("|")
        dsl_cells = [c for c in dsl_cells if c]
        for x, dsl_cell in enumerate(dsl_cells):
            tile_type = tile_type_dict[dsl_cell]
            if tile_type == StartTile:
                global start_tile_location
                start_tile_location = x, y
            row.append(tile_type(x, y) if tile_type else None)

        world_map.append(row)



def tile_at(x, y):
    if x < 0 or y < 0:
        return None
    try:
        return world_map[y][x]
    except IndexError:
        return None