import collections as coll
import datetime as dt
import itertools as it
import math
from operator import itemgetter as ig
import pprint as pp
import re


def solve():

    data = open('data_inputs\day06_input.txt', 'r', encoding='utf-8').read().splitlines()[0]
    unique_instances = []

    for i in range(len(data)):
        # only care starting at 4th postion. If the set is len of 4 we know chars are unique

        # for part to change range of set from 4 to 14
        if i-3>=0 and len(set([data[i-j] for j in range(14)]))==14:
            unique_instances.append(i+1)

    print("Part 1 or 2", unique_instances[0])
    return


solve()
