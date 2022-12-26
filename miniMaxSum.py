#!/bin/python3


# https://www.hackerrank.com/challenges/one-month-preparation-kit-mini-max-sum/problem
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    sorted_array = sorted(arr)
    minimum_sum = sum(sorted_array[:4])
    maximum_sum = sum(sorted_array[-4:])

    print(f"{minimum_sum} {maximum_sum}")

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)

