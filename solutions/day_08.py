from operator import itemgetter as ig
import pprint as pp
import re


def solve_pt1():

    data = open('data_inputs\day08_input.txt', 'r', encoding='utf-8').read().splitlines()

    # 2D array
    grid = []
    total_trees = 0

    # parse data
    for row in data:
        # turn map object into list resulting in each row being broken up
        # into its individual cols
        res = list(map(int, row))
        grid.append(res)

    for row in range(len(grid)):
        for col in range(len(grid[row])):

            tree_height = grid[row][col]

            # visibility check initialized
            left_vis, right_vis, up_vis, down_vis = False, False, False, False

            # left tree visibility check
            if all(grid[row][left] < tree_height for left in range(col)):
                left_vis = True

            # right tree visibility check
            if all(grid[row][right] < tree_height for right in range(col + 1, len(grid[row]))):
                right_vis = True

            # up tree visibility check
            if all(grid[up][col] < tree_height for up in range(row)):
                up_vis = True

            # down tree visibility check
            if all(grid[down][col] < tree_height for down in range(row + 1, len(grid))):
                up_vis = True
            
            if up_vis or down_vis or left_vis or right_vis:
                total_trees += 1

    print(total_trees)
    
    return

def solve_pt2():

    data = open('data_inputs\day08_input.txt', 'r', encoding='utf-8').read().splitlines()

    # 2D array
    grid = []
    # keep track of line of sights
    totals = [0]

    # parse data
    for row in data:
        # turn map object into list resulting in each row being broken up
        # into its individual cols
        res = list(map(int, row))
        grid.append(res)

    for row in range(len(grid)):
        for col in range(len(grid[row])):

            tree_height = grid[row][col]

            # visibility check initialized
            left_vis, right_vis, up_vis, down_vis = 0, 0, 0, 0

            # left vis
            for left in range(col -1, -1, -1):
                left_vis += 1
                if grid[row][left] >= tree_height:
                    # stop counting
                    break
            # right vis
            for right in range(col + 1, len(grid[row])):
                right_vis +=1
                if grid[row][right] >= tree_height:
                    break
            # up vis
            for up in range(row -1, -1, -1):
                up_vis += 1
                if grid[up][col] >= tree_height:
                    break
            # down vis
            for down in range(row + 1, len(grid)):
                down_vis += 1
                if grid[down][col] >= tree_height:
                    break
            
            vis = up_vis * down_vis * left_vis * right_vis
            # print(vis)
            totals.append(vis)
    
    max_value = max(totals)
    print(max_value)
    return

solve_pt1()

solve_pt2()
