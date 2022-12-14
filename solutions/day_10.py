import collections as coll
import datetime as dt
import itertools as it
import math
from operator import itemgetter as ig
import pprint as pp
import re



def solve_1():

    data = open('data_inputs\day10_input.txt', 'r', encoding='utf-8').read().splitlines()

    x = 1
    op_count = 0

    total = 0
    cycles = [20, 60, 100, 140, 180, 220]

    for comm in data:
        command = comm.split(" ")

        if command[0] == "noop":
            op_count += 1

            if op_count in cycles:
                total += op_count * x
        
        elif command[0] == "addx":


            op_count += 1

            if op_count in cycles:
                total += op_count * (x)

            op_count += 1

            if op_count in cycles:
                total += op_count * (x)

            amt = int(command[1])
            x += amt
    
    print(total)

   
    return

def solve_2():

    data = open('data_inputs\day10_input.txt', 'r', encoding='utf-8').read().splitlines()

    current_x = 1
    op_count = 0
    screen = 0

    row = 0
    col = 0

    values_at_positions= [1] * 241

    # go through commands up get the values of X at each position
    for comm in data:
        command = comm.split(" ")

        if command[0] == "noop":
            op_count += 1
            values_at_positions[op_count] = current_x

        elif command[0] == "addx":
            amt = int(command[1])

            # at the end of the next cycle time
            values_at_positions[op_count + 1] = current_x
            current_x += amt

            # at the end of two operations from now
            # the value of x at position is going to be the new update x
            # from above
            op_count += 2
            values_at_positions[op_count] = current_x

    # Build out the view. First initialize
    #[1, 39] 6 high
    screen = [[None] * 40 for _ in range(6)]


    for row in range(6):
        for col in range(40):
            
            # 1 - 240
            cycle_time_drawn = row * 40 + col + 1
            # look at previous cycle time
            if abs(values_at_positions[cycle_time_drawn - 1] - (col)) <= 1:
                screen[row][col] = "#"
            else:
                screen[row][col] = " "
    # print(screen)

    for row in screen:
        print("".join(row))
    

# Part 1
# solve_1()

# Part 2
solve_2()
