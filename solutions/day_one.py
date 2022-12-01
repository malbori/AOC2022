import collections as coll
import datetime as dt
import itertools as it
import math
from operator import itemgetter as ig
import pprint as pp
import re

from utility.helper import ints

def solve():

    data = open('data_inputs\day01_input.txt', 'r', encoding='utf-8').read()
    print(data)

    # convert string to array of nums with helper function
    nums = ints(data)
    print(nums)

    # multiple lines of nums
    # nums = [[ints(l)] for l in d.split("\n")]

    return

print(solve())
