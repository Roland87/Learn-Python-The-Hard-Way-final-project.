import pytest
from gothonweb.planisphere import *

def test_room():
    gold = Room("Gold Room",
                """This room has gold in it you can grab. There's a
                door t the north.""")
    assert gold.name == "Gold Room"
    assert gold.paths == {}

def test_room_paths():
    center = Room("Center", "Test room in the center.")
    north = Room("North", "Test room in the north.")
    south = Room("South", "Test room in the south.")

    center.add_paths({'north': north, 'south': south})
    assert center.go('north') == north
    assert center.go('south') == south

def test_map():
    start = Room("Start", "You can go west and down a hole.")
    west = Room("Trees", "There are threes here, you can go east.")
    down = Room("Dungeon", "It's dark down here, you can go up.")

    start.add_paths({'west': west, 'down': down})
    west.add_paths({'east': start})
    down.add_paths({'up': start})

    assert start.go('west') == west
    assert start.go('west').go('east') == start
    assert start.go('down').go('up') == start

def test_gothon_game_map():
    start_room = load_room(START)
    assert start_room.go('shoot!') == generic_death
    assert start_room.go('dodge!') == generic_death

    room = start_room.go('tell a joke')
    assert room == laser_weapon_armory