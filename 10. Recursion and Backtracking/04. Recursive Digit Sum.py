#!/bin/python3

import math
import os
import random
import re
import sys

def _digitSum(n):
    if len(n) == 1:
        return int(n)
    else:
        temp = str(sum([int(x) for x in n]))
        return _digitSum(temp)

# Complete the superDigit function below.
def superDigit(n, k):
    temp = str(k*sum([int(x) for x in n]))
    return _digitSum(temp)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = nk[0]

    k = int(nk[1])

    result = superDigit(n, k)

    fptr.write(str(result) + '\n')

    fptr.close()
