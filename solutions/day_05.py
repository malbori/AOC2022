import collections as coll
import datetime as dt
import itertools as it
import math
from operator import itemgetter as ig
import pprint as pp
import re


def solve():

    # intial empty stack to incresase index by one for easy indexing based on input
    # also a tracker stack
    stacks = [
        [],
        ['Q','F','L','S','R'],
        ['T','P','G','Q','Z','N'],
        ['B','Q','M','S'],
        ['Q','B','C','H','J','Z','G','T'],
        ['S','F','N','B','M','H','P'],
        ['G','V','L','S','N','Q','C','P'],
        ['F','C','M'],
        ['M','P','V','W','Z','G','H','Q'],
        ['R','N','C','L','D','Z','G']
    ]

    # stacks = [
    # [],
    # ['N','Z'],
    # ['D','C','M'],
    # ['P']
    # ]

    pt_1 = ""

    # not re-writing the hard-coded stacks
    for _, v in enumerate(stacks):
        v.reverse()
    
    print(stacks)
    instructions = open('data_inputs\day05_input.txt', 'r', encoding='utf-8').read().splitlines()

    # use re import to find all the ints in a string.
    # just need the ints since the instructions are always move, from, to
    # re super useful. Stack Oveflow: question 11339210
    for _, order in enumerate(instructions):
        amount, from_stack, to_stack = map(int, re.findall(r'\d+', order))
        
        # pop from list and insert values into tracker list
        for i in range(amount):
            val = stacks[from_stack].pop()
            stacks[0].append(val)
        
        # Needed for pt_1 only
        # stacks[0].reverse()

        # move values from tracker stack to new stack
        tracker_len = len(stacks[0])
        for i in range(tracker_len):
            val = stacks[0].pop()
            stacks[to_stack].append(val)

        
    print("".join(x[-1] for i, x in enumerate(stacks[1:])))
    return


solve()
