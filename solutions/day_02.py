import collections as coll
import datetime as dt
import itertools as it
import math
from operator import itemgetter as ig
import pprint as pp
import re

def solve():

    choice_values = {'X' : 1, 'Y': 2, 'Z': 3}
    won, loss, draw = 6, 0, 3

    win = {
        'C': 'X',
        'A': 'Y',
        'B': 'Z'
    }

    draws = {
        'A': 'X',
        'B': 'Y',
        'C': 'Z'
    }

    losses = {
        'A': 'Z',
        'B': 'X',
        'C': 'Y'
    }

    total_score_pt1 = 0
    total_score_pt2 = 0

    data = open('data_inputs\day02_input.txt', 'r', encoding='utf-8').read().splitlines()

    for i , v in enumerate(data):
        enemy_choice, my_choice = v.split(' ')

        if win[enemy_choice] == my_choice:
            total_score_pt1 += won + choice_values[my_choice]
        elif draws[enemy_choice] == my_choice:
            total_score_pt1 += draw + choice_values[my_choice]
        else:
            total_score_pt1 += choice_values[my_choice] + loss
    
    for i , v in enumerate(data):
        enemy_choice, result = v.split(' ')

        if result == 'Z':
            # winning
            total_score_pt2 += won + choice_values[win[enemy_choice]]
        elif result == 'Y':
            # draw
            total_score_pt2 += draw + choice_values[draws[enemy_choice]]
        else:
            # lost
            total_score_pt2 += choice_values[losses[enemy_choice]] + loss

    print(total_score_pt1)
    print(total_score_pt2)

    return


solve()
