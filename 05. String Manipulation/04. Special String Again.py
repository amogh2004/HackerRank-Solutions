import math
import os
import random
import re
import sys

# Complete the substrCount function below.
def substrCount(n, s):

    class Repeater(object):
        def __init__(self, char, count):
            self.char = char
            self.count = count

    # 1st round, build repeaters
    curr, count = None, 0
    repeaters = []
    for i in s:
        if i == curr:
            count += 1
        else:
            if curr is not None:
                repeaters.append(Repeater(curr, count))
            curr, count = i, 1
    repeaters.append(Repeater(curr, count))  # append the last case

    # 2nd round, calculate one repeater one time
    answer = 0
    for repeater in repeaters:
        # the formula: 3 => 3*4//2 = 6, 4 => 4*5//2 = 10
        answer += (repeater.count * (repeater.count+1)) // 2
    #print("2#answer=", answer)

    # 3rd round, caculate 3 repeaters joining together
    for i in range(2, len(repeaters)):
        first, second, third = repeaters[i-2:i+1]
        if second.count == 1 and first.char == third.char: # palindrome only allows one diff letter in the middle.
            answer += min(first.count, third.count)
    #print("3#answer=", answer)

    return answer


def substrCount_failed_timeout(n, s):
    def is_palindrome(string):
        first = string[0]
        for i in range(len(string) // 2):
            # test indexes: 3=left:0, right:2
            # test indexes: 4=left:0, right:3
            if first != string[i] or first != string[len(string)-1-i]:
                return False
        return True

    def is_mid_diff(string):
        if len(string) == 1:
            return False
        return (len(string) % 2 == 1) and (string[0] != string[len(string)//2])

    count = 0
    for i in range(n):
        has_diff = False
        for j in range(i, n):
            curr = s[i:j+1]
            if is_palindrome(curr):
                #print(s[i:j+1])
                count += 1
                if is_mid_diff(curr):
                    has_diff = True
            else:
                if has_diff:
                    break # jump out this break
    return count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = substrCount(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
