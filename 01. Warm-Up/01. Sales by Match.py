#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    socks = {}
    res = 0

    for el in ar:
        if el not in socks.keys():
            socks[el] = 1
        else:
            socks[el] += 1

    for key in socks.keys():
        res += socks[key]//2

    return res

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
