import world, npc
import ascii, enemies
import game
from player import Player
import pyglet

class MapTile:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.roomsafe = []

    def intro_text(self):
        raise NotImplementedError("Create a subclass instead!")

    def modify_player(self, player):

        pass
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
            player.score += 1
            print("+{} score increased.".format(player.score))

    def intro_text(self):
        if self.quest_claimed:
            return """ Nothing remains of the Flying Circus. Just the smell of burnt frog flesh.
            ****************************************************
            The goblin fixes his piercing black eyes at your being."""
        else:
            return """
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
            player.score += 1
            print("Your score: {}.".format(player.score))
            self.quest_claimed = True

    def intro_text(self):
        if self.quest_claimed:
            return """
            The time portal is gone... it now looks like any other part of the cave."""
        else:
            return """As you step through the time portal,
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
            player.score += 1
            print("+{} score increased.".format(player.score))

    def intro_text(self):
        if self.quest_claimed:
            return """ You're transported back in time … "
              "you find yourself in Georgia during the midst"
              " of a congressional campaign.
            There is a defaced poster of Newt Gingrich on the wall."""
        else:
            return """
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
            player.score += 1
            print("+{} score increased.".format(player.score))

    def intro_text(self):
        if self.quest_claimed:
            return """
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
            player.score += 1
            print("+{} score increased.".format(player.score))

    def intro_text(self):
        if self.quest_claimed:
            return """ 
             The strange mystical creature is still waiting to talk to you."""
        else:
            return """Welcome, welcome... a far off voice is calling out too you. I have something you might want,
            if you'd like to get rid of the witches haunt. I will give it nearly free...
            of course a little gold will go to me.
             *********************************************************************************************
             There is small ghostly outline of a goblin-like creature in the corner. He beacons you over..."""


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
            player.score += 1
            print("+{} score increased.".format(player.score))

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
        self.summon_dark_lord = False
        super().__init__(x, y)

    def modify_player(self, player):
        pass

    def summoning(self):
        if self.summon_dark_lord == True:
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