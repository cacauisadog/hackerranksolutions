# https://www.hackerrank.com/challenges/one-month-preparation-kit-sock-merchant/problem

from collections import Counter


def sockMerchant(n, ar):
    counter = Counter(ar)
    pairs = 0

    for item in counter:
        pairs += counter[item] // 2

    return pairs


print(sockMerchant(9, [10, 20, 20, 10, 10, 30, 50, 10, 20]))
