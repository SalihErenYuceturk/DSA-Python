from random import randrange

"""
“methinks it is like a weasel”
Write 3 functions.

1. Generates a string that is 28 characters long by choosing random letters from the 26 letters in the alphabet plus
the space.

2. Scores each generated string by comparing the randomly generated string to the goal string.

3. Repeatedly calls the first and second methods, then if 100% of the letters are correct it is done. If the letters 
are not correct then it will generate a whole new string. This function should print out the best string generated so
far and its score every 1000 tries.
"""


# Returns a random 28 character long string made of letters and space.
def generate_string():
    alphabet = "abcdefghijklmnopqrstuvwxyz "
    count = 0
    output = ""
    while count != 28:
        output = output + alphabet[randrange(27)]
        count += 1
    return output


# Returns ratio of similarity between string_in and goal_string.
def compare_string(string_in):
    goal_string = "methinks it is like a weasel"
    index = 0
    correct_characters = 0
    while index != 28:
        if string_in[index] == goal_string[index]:
            correct_characters += 1
        index += 1
    return correct_characters/28


def main():
    best_random_string = generate_string()
    counter = 0
    while True:
        random_string = generate_string()
        if compare_string(random_string) > compare_string(best_random_string):
            best_random_string = random_string
        if counter % 1000 == 0:
            print(best_random_string, " Similarity Index: ", compare_string(best_random_string), " Iteration: ",
                  counter)
        if compare_string(best_random_string) == 1:
            print(best_random_string, " Similarity Index: ", compare_string(best_random_string), " Iteration: ",
                  counter)
            break
        counter += 1


main()



