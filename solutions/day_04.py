import collections as coll
import datetime as dt
import itertools as it
import math
from operator import itemgetter as ig
import pprint as pp
import re


def solve():

    data = open('data_inputs\day04_input.txt', 'r', encoding='utf-8').read().splitlines()
    sum_one = 0
    sum_two = 0

    for _, val in enumerate(data):
        a, b, c, d = splitIntoNums(val)

        # second range contained in first range or first range contained in second range
        if (a<=c and d<=b) or (c<=a and b<=d):
            # print("Here")
            sum_one += 1

        # pair of ranges must be completely to the left or right of each other
        # so make sure the end of one is out of bounds of the start of the other
        if not (b < c or d < a):
            sum_two += 1

    print("Part 1 Answer: ", sum_one)
    print("Part 2 Answer: ", sum_two)

    return


def splitIntoNums(val):
    a, b = val.split(',')
    item_one, item_two = a.split('-')
    item_three, item_four = b.split('-')

    c,d,e,f = [int(x) for x in [item_one, item_two, item_three, item_four]]
    
    return c,d,e,f


solve()
