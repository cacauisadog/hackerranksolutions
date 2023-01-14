# https://www.hackerrank.com/challenges/one-month-preparation-kit-the-birthday-bar/problem


def birthday(s, d, m):
    number_of_ways = 0

    for i in range(len(s)):
        segment = s[i : i + m]
        if len(segment) < m:
            break
        if sum(segment) == d:
            number_of_ways += 1

    return number_of_ways


print(birthday([1, 1, 1, 1, 1, 1], 3, 3))
