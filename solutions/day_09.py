import collections as coll
import datetime as dt
import itertools as it
import math
from operator import itemgetter as ig
import pprint as pp
import re



def solve(length_of_rope):

    data = open('data_inputs\day09_input.txt', 'r', encoding='utf-8').read().splitlines()

    # Direction Mapping
    direction = {'L': (-1, 0), 'R': (1, 0), 'D': (0, -1), 'U': (0, 1)}

    # map the operations in data into direction , distance
    operations = []
    for row in data:
        # know the input starts with char and the rest is the int we want to pase
        dir, distance = row.split(" ")

        dir = direction[dir]
        distance = int(distance)
        
        operations.append((dir,distance))
    # print(operations)

    # initial position
    x_position = [0] * length_of_rope
    y_position = [0] * length_of_rope

    # going to build a dictionary of the visited positions
    visited_points = { (x_position[-1], y_position[-1]) }

    # iterate through the operations
    for (move_x, move_y), dist in operations:

        # iterate through the distance traveled
        for i in range(dist):
            # new x,y position in the grid
            x_position[0] += move_x
            y_position[0] += move_y

            for j in range(length_of_rope - 1):
                # distance created with the move
                distance_x = x_position[j + 1] - x_position[j] 
                distance_y = y_position[j + 1] - y_position[j]

                # diagonal. Use abs to get rid of those negative values 
                if abs(distance_x) == 2 or abs(distance_y) == 2: 
                    x_position[j + 1] = x_position[j] + int(distance_x / 2) 
                    y_position[j + 1] = y_position[j] + int(distance_y / 2)
            
            # log the visited spot
            visited_points.add((x_position[-1], y_position[-1]))
    # print(visited_points)
    print(len(visited_points))
    return

# Part 1
solve(2)

# Part 2
solve(10)
