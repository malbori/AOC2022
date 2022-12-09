import collections as coll
import datetime as dt
import itertools as it
import math
from operator import itemgetter as ig
import pprint as pp
import re


def solve():

    curr_path = []
    sizes = coll.defaultdict(int)
    child_paths = coll.defaultdict(list)
    min_size = 100000
    total_size = 0
    
    # need to chunk out the instructions into sets of instructions
    data = open('data_inputs\day07_input.txt', 'r', encoding='utf-8').read().split("\n$ ")[1:]

    # iterate through instruction sets
    for instruction in data:
        steps = instruction.split("\n")

        action, result = steps[0], steps[1:]
        # print(action, result)

        action_steps = action.split(" ")
        command = action_steps[0]

        # handle scenarios for commands
        if command == "cd":
            if action_steps[1] == "..":
                # back out of path
                curr_path.pop()
            else:
                # add to to curr path
                appending = action_steps[1]
                print(appending)
                # curr_path.append[action_steps[1]]
            return
        
        path = "/".join[curr_path]

        # directory sizes in curr path
        dir_file_sizes = []

        for i in result:
            if i.startswith("dir"):
                dir_name = i.split(" ")[1]
                # build all the paths
                # need this 
                child_paths[path].append(f"{path}/{dir_name}")
            else:
                # add file sizes
                dir_file_sizes.append(int(i.split(" ")[0]))

        # leveraging default dict allows allocation if key DNE
        sizes[path] = sum(dir_file_sizes)
    # print(data)

    # now go through and get total size


    def dfs(x):
        size = sizes[x]
        for child in child_paths[x]:
            size += dfs(child)
        return size

    
    for path in sizes:
        if dfs(path) <= min_size:
            total_size += dfs(path)


    
    return



solve()