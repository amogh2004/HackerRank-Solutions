#!/bin/python3

import math
import os
import random
import re
import sys
from collections import deque

def is_safe(grid, x, y, distances):
    return x >= 0 and x < len(grid) and y >= 0 and y < len(grid) and distances[x][y] == -1 and grid[x][y] != 'X'

def get_safe_moves(grid, node, distances):
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    variants = []

    for di in directions:
        nunode = (node[0] + di[0], node[1] + di[1])
        while is_safe(grid, nunode[0], nunode[1], distances):
            variants.append(nunode)
            nunode = (nunode[0] + di[0], nunode[1] + di[1])

    return variants

# Complete the minimumMoves function below.
def minimumMoves(grid, startX, startY, goalX, goalY):
    next_to_visit = deque()
    node = (startX, startY)
    next_to_visit.appendleft(node)
    distances = [[-1]*len(grid) for _ in range(len(grid))]
    distances[startX][startY] = 0

    while next_to_visit:
        node = next_to_visit.pop()
        #print("point = ({}, {})".format(node[0], node[1]))
        #for row in distances:
        #    print(row)
        #print()
        height = distances[node[0]][node[1]]

        variants = get_safe_moves(grid, node, distances)

        for var in variants:
            if var == (goalX, goalY):
                return height + 1
            distances[var[0]][var[1]] = height + 1
            next_to_visit.appendleft(var)

    return -1

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    grid = []

    for _ in range(n):
        grid_item = input()
        grid.append(grid_item)

    startXStartY = input().split()

    startX = int(startXStartY[0])

    startY = int(startXStartY[1])

    goalX = int(startXStartY[2])

    goalY = int(startXStartY[3])

    result = minimumMoves(grid, startX, startY, goalX, goalY)

    fptr.write(str(result) + '\n')

    fptr.close()
