from random import randrange

"""
“methinks it is like a weasel”
Write 3 functions.

1. Generates a string that is 28 characters long by choosing random letters from the 26 letters in the alphabet plus
the space.

2. Scores each generated string by comparing the randomly generated string to the string.

3. Repeatedly calls generate and score, then if 100% of the letters are correct it is done. If the letters are not
correct then it will generate a whole new string.This  function should print out the best string generated so
far and its score every 1000 tries.
"""


def generate_string():
    alphabet = "abcdefghijklmnopqrstuvwxyz "
    count = 0
    output = ""
    while count != 28:
        output = output + alphabet[randrange(27)]
        count += 1
    return output


print(generate_string())

