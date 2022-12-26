#!/bin/python3


# https://www.hackerrank.com/challenges/one-month-preparation-kit-plus-minus/problem
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    arrlen = len(arr)
    positives, negatives, zeroes = 0, 0, 0

    for num in arr:
        if num > 0:
            positives += 1
        elif num < 0:
            negatives += 1
        else:
            zeroes += 1

    positive_ratio = positives / arrlen
    negative_ratio = negatives / arrlen
    zero_ratio = zeroes / arrlen

    print(f"{positive_ratio:.6f}\n{negative_ratio:.6f}\n{zero_ratio:.6f}\n")

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)

