import collections as coll
import datetime as dt
import itertools as it
import math
from operator import itemgetter as ig
import pprint as pp
import re


def solve():

    data = open('data_inputs\day01_input.txt', 'r', encoding='utf-8').read().splitlines()
    # print(data)

    calorie_totals = [0]
    curr_elf = 0

    for i, v in enumerate(data):
        if v == "":
            curr_elf +=1
            calorie_totals.append(0)
        else:
            calorie_totals[curr_elf] += int(v)
    
    print(max(calorie_totals))
    
    #part two answer
    calorie_totals.sort()
    print(calorie_totals[-1]+ calorie_totals[-2] + calorie_totals[-3])

    return

solve()
