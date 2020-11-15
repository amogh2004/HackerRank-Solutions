#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countSwaps function below.
def countSwaps(arr, n):
    num_swaps = 0
    for i in range(n):
        for j in range(n-1):
            if arr[j] > a[j+1]:
                buff = arr[j+1]
                arr[j+1] = a[j]
                a[j] = buff
                num_swaps += 1
    print("Array is sorted in {} swaps.".format(num_swaps))
    print("First Element: {}".format(arr[0]))
    print("Last Element: {}".format(arr[-1]))

if __name__ == '__main__':
    n = int(input())

    a = list(map(int, input().rstrip().split()))

    countSwaps(a, n)
