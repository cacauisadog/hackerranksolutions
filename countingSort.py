# https://www.hackerrank.com/challenges/one-month-preparation-kit-countingsort1/problem


def countingSort(arr):
    result = [0] * 100

    for i in arr:
        result[i] += 1

    return result


print(countingSort([1, 2, 10, 3]))
