import collections as coll
import datetime as dt
import itertools as it
import math
from operator import itemgetter as ig
import pprint as pp
import re



def solve():

    data = open('data_inputs\day09_input.txt', 'r', encoding='utf-8').read().splitlines()
    length_of_rope = 2

    # Direction Mapping
    direction = {'L': (-1,0), 'R':(1,0),'D':(0,-1),'U':(0,1)}

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
    visited_points = {x_position[-1], y_position[-1]}

    # iterate through the operations
    for (move_x, move_y), dist in operations:

        # iterate through the distance traveled
        for i in range(dist):
            # new x,y position in the grid
            x_position[0] += move_x
            y_position[0] += move_y

            for j in range (length_of_rope -1):
                # track the distance and handle directional movement
                x_distance = x_position[j + 1] - x_position[j]
                y_distance = y_position[j +1] - y_position[j]

                # handle directional movement
                if abs(x_distance) == 2 or abs(y_distance) == 2:
                    x_position[j + 1] = x_position[j] + int(x_distance / 2)
                    y_position[j + 1] = x_position[j] + int(y_distance / 2)
            
            # log the visited spot
            visited_points.add((x_position[-1], y_position[-1]))
    print(len(visited_points))
    return

solve()
