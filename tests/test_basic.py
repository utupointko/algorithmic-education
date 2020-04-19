# -*- coding: utf-8 -*-

from collections import deque
from algoedu import main

# This is our map which we are converting to main.Area

dun = ["#########################################################&#######",
       "#.......#...#.........#...........#...............#.....#&#.-...#",
       "#######.~...#........#..........#...................#...#&#.#...#",
       "&&&&&&#.#...........#...........#~###################...###.#####",
       "#######.#...#####.##............#...................#.....§.....#",
       "#.......#...#&&#....##..........#...................#.....#####-#",
       "#####+###...####....##.......#####################..#.....#.....#",
       "#..##........................#&&#................#..#.....#.....#",
       "#...##...........#########...####.............#..#..#.....#.....#",
       "#....##..................#......#..###############..#.....#.....#",
       "#.....##.................#.#....#..#...#...#...#....#.....#.....#",
       "#......##.......#######..#.#....#....#...#...#...#..#.....#.##..#",
       "#...............#&&&&&#..#.#....#####################.....#.##..#",
       "#........#####..#&&&&&#..#.#.............#................##.#..#",
       "#........#&&&#..#######....#.............#................#.##..#",
       "#........#####.............#####.....#...#...#....###...####.#..#",
       "#..............##########.............#..#..#.....#&#...#&#.##..#",
       "#..............#........#..............#...#......###...####.#..#",
       "#.##...###..####........#..#####........#.#...............#..#..#",
       "#..............-........§..#........############..........####..#",
       "####.#.........#........#..#........#....#.....#.########.......#",
       "#.....#........##########..#.............#.......#&&#..###-####+#",
       "#.....##...................#.............#.......#####.#&#......#",
       "#.......#..................#.............#.......~.....#&#......#",
       "########################################################&########"]

rev = {}
tmp_terrain = []

for tile in main.config.TERRAIN_CHARACTERS:
    tmp = main.config.TERRAIN_CHARACTERS[tile]
    rev[tmp] = tile

for y in range(len(dun)):
    tmp_terrain.append([])
    for x in range(len(dun[y])):
        tmp_terrain[y].append(rev[dun[y][x]])

test_area = main.Area()
test_area.terrain = tmp_terrain
test_area.width = len(tmp_terrain[0])
test_area.height = len(tmp_terrain)

# An instance of the pathfinder.
pathfinder = main.Pathfinder(test_area)


def test_Pathfinder_find_point():
    r = pathfinder.find_point(2, 2, 2, 2, use_diagonals=True, abort=False)
    assert r == deque([])
    r = pathfinder.find_point(2, 2, 2, 4, use_diagonals=True, abort=False)
    assert r == None
    r = pathfinder.find_point(6, 6, 4, 12, use_diagonals=True, abort=False)
    assert r == deque([(6, 7), (6, 8), (7, 9), (8, 10), (9, 11), (8, 12), (7, 12), (6, 12), (5, 12), (4, 12)])

    r = pathfinder.find_point(21, 21, 3, 3, use_diagonals=True, abort=False)
    assert r == None
    r = pathfinder.find_point(15, 12, 7, 8, use_diagonals=True, abort=False)
    assert r == deque([(14, 11), (13, 10), (12, 9), (11, 8), (10, 8), (9, 8), (8, 8), (7, 8)])


def test_Pathfinder_is_point_findable():
    r = pathfinder.is_point_findable(2, 2, 2, 2, use_diagonals=True, abort=False)
    assert r == True
    r = pathfinder.is_point_findable(2, 2, 2, 4, use_diagonals=True, abort=False)
    assert r == False
    r = pathfinder.is_point_findable(6, 6, 4, 12, use_diagonals=True, abort=False)
    assert r == True
    r = pathfinder.is_point_findable(21, 21, 3, 3, use_diagonals=True, abort=False)
    assert r == False
    r = pathfinder.is_point_findable(15, 12, 7, 8, use_diagonals=True, abort=False)
    assert r == True


def test_Pathfinder_find_tile():
    r = pathfinder.find_tile(2, 2, [5, 3, 2, (2, 3), (6, 7)], use_diagonals=True, best_path=True, abort=False)
    assert r == None
    r = pathfinder.find_tile(1, 1, [8, 9, 12, (3, 4), (2, 1)], use_diagonals=True, best_path=True, abort=False)
    assert r == None


def test_Pathfinder_nearest():
    r = pathfinder.nearest(2, 17, [1, 1, 1, (6, 6), (7, 7)], use_diagonals=True, abort=False)
    assert r == None
    r = pathfinder.nearest(8, 8, [8, 9, 12, (4, 2), (8, 11)], use_diagonals=True, abort=False)
    assert r == None