import collections as coll
import datetime as dt
import itertools as it
import math
from operator import itemgetter as ig
import pprint as pp
import re
import string


def solve():

    ruck_sacks = open('data_inputs\day03_input.txt', 'r', encoding='utf-8').read().splitlines()
    part1(ruck_sacks)
    part2(ruck_sacks)

    return

def part1(ruck_sacks):
    sum = 0
    for _, items in enumerate(ruck_sacks):
        item1, item2 = splitItems(items)

        # castring string to set returns an iterable with unique letters. Can retrieve intersection
        # of the two sets for the matching char
        match = set(item1) & set(item2)
        #grab first element in set of 1
        match = next(iter(match))

        # thank god for built-in ord function
        # ord 'a' is 97. So subtact 96 to get priority 1 for lowercase
        # ord 'A' is 65. So subtact 38 to get priority 27 for uppercase

        if match.islower():
            sum += ord(match) - 96
        else:
            sum += ord(match) - 38

    print(sum)
    return 

# pretty sure this only works assuming the entire input is divisble by 3
def part2(ruck_sacks):

    item_count = 0
    group_items = []
    sum = 0
    
    for _, items in enumerate(ruck_sacks):

        item_count += 1
        group_items.append(items)

        if item_count % 3 == 0:

            match = common_item(group_items[0], group_items[1], group_items[2])

            if match.islower():
                sum += ord(match) - 96
            else:
                sum += ord(match) - 38
            # reset the items
            group_items = []

    print(sum)
    return 

# slice the item form the rucksack into two parts
def splitItems(item):

    n = len(item)
    if n%2 == 0:
        s1 = slice(0,n//2)
        s2 = slice(n//2,n)
    else:
        s1 = slice(0,n//2+1)
        s2 = slice(n//2+1,n)

    return item[s1], item[s2]

# split into 3 bags and find the common item
def common_item(bag_one, bag_two, bag_three):
    return next(iter(set(bag_one) & set(bag_two) & set(bag_three)))


solve()
