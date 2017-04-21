#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""

:author: FIL - IEEA - Univ. Lille1.fr <http://portail.fil.univ-lille1.fr>_

:date: 2017, march

"""

from game_2048 import *

commands = { "U" : "up", "L" : "left", "R" : "right", "D" : "down" }

def read_next_move():
    """
    read a new move

    :CU: none
    """
    L=['U','D','L','R']
    a=str(input ('Your Move ? ((U)p, (D)own, (L)eft, (R)ight) '))
    for e in range(4):
        if a.upper == L[e]:
            return a
        a=str(input ('Your Move ? ((U)p, (D)own, (L)eft, (R)ight) '))



def play():
    """
    main game procedure
    
    """
    grid = grid_init()
    grid_print(grid)
    while not is_grid_over(grid) and grid_get_max_value(grid) < 2048:
        move = read_next_move()
        grid = grid_move(grid, commands[move])
        grid_add_new_tile(grid)
        grid_print(grid)
        grid_score(grid)
    if grid_get_max_value(grid) == 2048:
        print("You Won !!")
    else:
        print("You Lose ;-(")


def usage():
    print('Usage : {:s}'.format(sys.argv[0]))
    exit(1)

if __name__ == '__main__':
    import sys

    play()
    exit(0)
