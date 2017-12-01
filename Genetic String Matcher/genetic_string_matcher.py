"""
- Sharad Bhat
- 3rd November, 2017
"""

import string
import random
import time

string_to_be_matched = input("Enter string to be matched\n")

possible_characters = string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation + ' '

n = len(string_to_be_matched)

generation = 0

temporary = ''.join(random.choices(possible_characters, k=n))

while True:
    generation += 1
    print("Generation " + str(generation) + " : ", end='')
    print(temporary)
    if temporary == string_to_be_matched:
        break
    next_temporary = ''
    for i in range(len(temporary)):
        if string_to_be_matched[i] == temporary[i]:
            next_temporary += temporary[i]
        else:
            next_temporary += random.choice(possible_characters)
    temporary = next_temporary
    time.sleep(0.01)

print("It took {} generations to match the input string".format(generation))
