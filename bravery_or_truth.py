# -*- coding: utf-8 -*-
"""
    bravery or truth
    just for fun!
    done by < aa.smpro@gmail.com >
"""
from random import *

players_num = int(input('number of players : '))
players = [[input(('player {} name : ').format(i + 1)) or str(i + 1), 'truth'] for i in range(0, players_num)]
last_player = randint(0, players_num - 1)
exchange = {"truth": "bravery", "bravery": "truth", }
while True:
    next_player = randint(0, players_num - 2)
    if last_player is not next_player:
        print('{}  :  {}  >>  {}'.format(players[last_player][0], players[next_player][0], players[next_player][1]))
        players[next_player][1] = exchange[players[next_player][1]]
        last_player = next_player
        if input() == 'q': break
