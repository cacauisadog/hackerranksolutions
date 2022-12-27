#!/bin/python3

import math
import os
import random
import re
import sys

# https://www.hackerrank.com/challenges/one-month-preparation-kit-flipping-bits/problem
# Complete the 'flippingBits' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts LONG_INTEGER n as parameter.
#

def flippingBits(n):
    bits = f"{n:032b}"
    flipped = ''.join('0' if c == '1' else '1' for c in bits)
    return int(flipped, 2)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        n = int(input().strip())

        result = flippingBits(n)

        fptr.write(str(result) + '\n')

    fptr.close()

