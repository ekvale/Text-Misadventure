from player import *
import world
from collections import OrderedDict
import items
import pyglet, os, sys, jsonpickle
import ascii
import enemies
import pickle



def play():
    print("""
                    Witch Cave: Double Boil, Toil, and Trouble
            A text-adventure game that will challenge even the literate.
                    By: Eric Kvale for Computer Science I Fall 2017 
 ********************************************************************************
*                    /   \              /'\       _                              *
*\_..           /'.,/     \_         .,'   \     / \_                            *
*    \         /            \      _/       \_  /    \     _                     *
*     \__,.   /              \    /           \/.,   _|  _/ \                    *
*          \_/                \  /',.,''\      \_ \_/  \/    \                   *
*                           _  \/   /    ',../',.\    _/      \                  *
*             /           _/m\  \  /    |         \  /.,/'\   _\                 *
*           _/           /MMmm\  \_     |          \/      \_/  \                *
*          /      \     |MMMMmm|   \__   \          \_       \   \_              *
*                  \   /MMMMMMm|      \   \           \       \    \             *
*                   \  |MMMMMMmm\      \___            \_      \_   \            *
*                    \|MMMMMMMMmm|____.'  /\_            \       \   \_          *
*                    /'.,___________...,,'   \            \   \        \         *
*                   /       \          |      \    |__     \   \_       \        *
*                 _/        |           \      \_     \     \    \       \_      *
*                /                               \     \     \_   \        \     *
*                                                 \     \      \   \__      \    *
*                                                  \     \_     \     \      \   *
*                                                   |      \     \     \      \  *
*                                                    \            |            \ *
 ********************************************************************************""")


    print("You are in a dark cave."
          " In the middle, there is a cauldron boiling. "
          "With a clasp of thunder, three witches suddenly appear before you. ")

    input(">")
    #spooky = pyglet.media.load("resources/seacave.wav", streaming=True)
    #spooky.play()

    world.parse_world_dsl()
    player = Player()

    while player.is_alive() and not player.victory:
        room = world.tile_at(player.x, player.y)
        print(room.intro_text())
        room.modify_player(player)
        if player.is_alive() and not player.victory:
            choose_action(room, player)
        elif not player.is_alive():
            print(ascii.grimreaper)
            print("You have failed. The witches feast on your body, and throw your soul into the underworld.")
            input("")

def get_available_actions(room, player):
    actions = OrderedDict()
    print("Choose an action: ")
    if player.inventory:
        action_adder(actions, 'i', player.print_inventory, "Print Inventory")
    if isinstance(room, world.EnemyTile) and room.enemy.is_alive():
        action_adder(actions, 'a', player.attack, "Attack")

    else:
        if world.tile_at(room.x, room.y -1):
                action_adder(actions, 'n', player.move_north, "Go North")
        if world.tile_at(room.x, room.y + 1):
            action_adder(actions, "s", player.move_south, "Go South")
        if world.tile_at(room.x + 1, room.y):
            action_adder(actions, "e", player.move_east, "Go East")
        if world.tile_at(room.x - 1, room.y):
            action_adder(actions, "w", player.move_west, "Go West")
    if isinstance(room, world.BossTile) and room.enemy.is_alive():
      action_adder(actions, 'a', player.attack, "Attack")
    if isinstance(room, world.VictoryTile) and room.enemy.is_alive():
        action_adder(actions, 'a', player.attack, "Attack")

    if player.is_alive:
        action_adder(actions, "c", player.character_info, "Character Info")
        action_adder(actions, "i", player.print_inventory, "View Inventory")
        action_adder(actions, "l", player.look_around, "Look Around")
        action_adder(actions, "?", player.help, "Help")
        action_adder(actions, "q", player.quit, "Quit")
    if isinstance(room, world.TraderTile):
        action_adder(actions, 't', player.trade, "Trade")
    if isinstance(room, world.StartTile):
        action_adder(actions, 'd', player.drop_item, "Drop in Cauldron")
    if isinstance(room, world.StartTile):
        action_adder(actions, 'p', player.pick_up_item, "Pick out of Cauldron")
    if player.hp < 100:
        action_adder(actions, "h", player.heal, "Heal")
    if isinstance(room, world.StartTile):
        action_adder(actions, "v", player.speak, "Speak to the Witch")
    if isinstance(room, world.TenTile):
        action_adder(actions, "g", player.getquest, "Talk to Quest Giver")
    if isinstance(room, world.TwoTile):
        action_adder(actions, "g", player.getquest, "Talk to Quest Giver")
    if isinstance(room, world.ThreeTile):
        action_adder(actions, "g", player.getquest, "Talk to Quest Giver")
    if isinstance(room, world.FourTile):
        action_adder(actions, "g", player.getquest, "Talk to Quest Giver")
    if isinstance(room, world.EightTile):
        action_adder(actions, "g",  player.getquest, "Talk to Quest Giver")
    if isinstance(room, world.SevenTile):
        action_adder(actions, "g", player.getquest, "Talk to the Quest Giver")
    if isinstance(room, world.SixTile):
        action_adder(actions, "z",  player.transport_to_nine, "Magic Portal")
    if isinstance(room, world.NineTile):
        action_adder(actions, "z", player.transport_to_six, "Magic Portal")
    if isinstance(room, world.FiveTile):
        action_adder(actions, "r", player.riddle, "Riddle")
    if isinstance(room, world.SixTile):
        action_adder(actions, "b", player.burnt_offerings, "Burnt Offerings")
    if isinstance(room, world.ThreeTile):
        action_adder(actions, "o", player.naming_stone, "Use the Naming Stone")

    #
    return actions

def action_adder(action_dict, hotkey, action, name):
    action_dict[hotkey.lower()] = action
    action_dict[hotkey.upper()] = action
    print("{}:{}".format(hotkey, name))

def choose_action(room, player):
    action = None
    while not action:
        available_actions = get_available_actions(room, player)
        action_input = input("Action: ")
        action = available_actions.get(action_input)
        if action:
            action()

        else:
            print("Invalid action!")

play()