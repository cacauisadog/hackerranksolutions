# https://www.hackerrank.com/challenges/one-month-preparation-kit-pangrams/problem
from string import ascii_lowercase


def pangrams(s):
    s = s.lower()
    alphabet = list(ascii_lowercase)

    for letter in alphabet:
        if letter not in s:
            return "not pangram"

    return "pangram"


print(pangrams("We promptly judged antique ivory buckles for the next prize"))
