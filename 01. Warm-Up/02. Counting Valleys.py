#!/bin/python3

import math
import os
import random
import re
import sys

def countingValleys(steps, path):
    # Write your code here
    res = 0
    in_valley = 0
    curr = 0

    for step in path:
        if step == 'U':
            curr += 1
        else:
            curr -= 1

        if curr < 0 and in_valley == 0:
            in_valley = 1
        if in_valley == 1 and curr == 0:
            in_valley = 0
            res += 1

    return res

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    steps = int(input().strip())

    path = input()

    result = countingValleys(steps, path)

    fptr.write(str(result) + '\n')

    fptr.close()
