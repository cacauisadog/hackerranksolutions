#!/bin/python3

import os 


# https://www.hackerrank.com/challenges/one-month-preparation-kit-time-conversion/problem
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    splits = s.split(":")
    hh = splits[0]
    mm = splits[1]
    ss = splits[2][:2]
    period = s[-2:]

    if period == "AM":
        if hh == "12":
            return f"00:{mm}:{ss}"
        return s[:-2]

    if period == "PM" and hh == "12":
        return s[:-2]

    return f"{int(hh)+12}:{mm}:{ss}"



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()

