# https://www.hackerrank.com/challenges/one-month-preparation-kit-caesar-cipher-1/problem

from collections import deque
from string import ascii_lowercase, ascii_uppercase


def caesarCipher(s, k):
    cipher_lowercase_alphabet = deque(ascii_lowercase)
    cipher_uppercase_alphabet = deque(ascii_uppercase)
    cipher_lowercase_alphabet.rotate(-k)
    cipher_uppercase_alphabet.rotate(-k)
    encrypted_string = ""

    for letter in s:
        if letter.islower() and letter in ascii_lowercase:
            letter_index = ascii_lowercase.index(letter)
            encrypted_letter = cipher_lowercase_alphabet[letter_index]
        elif letter in ascii_uppercase:
            letter_index = ascii_uppercase.index(letter)
            encrypted_letter = cipher_uppercase_alphabet[letter_index]
        else:
            encrypted_letter = letter

        encrypted_string += encrypted_letter

    return encrypted_string


print(caesarCipher("middle-Outz", 2))
