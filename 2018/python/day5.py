# Project: advent_of_code
# File: day_5
# Author: Joinemm
# Date created: 05/12/18
# Python Version: 3.6.6

import string

with open("input_5.txt", "r") as input:
    polymer_input = input.read().rstrip()

lowest = len(polymer_input)
for letter in list(string.ascii_lowercase):
    polymer = polymer_input.replace(letter, "").replace(letter.upper(), "")
    skip = 0
    finished = False
    while not finished:
        match = False
        for x in range(len(polymer)-skip-1):
            i = x + skip
            if polymer[i].lower() == polymer[i+1].lower():
                if not polymer[i].istitle() == polymer[i+1].istitle():
                    match = True
                else:
                    continue
            else:
                continue
            if i > 0:
                skip = i-1
            polymer = polymer[:i] + polymer[i+2:]
            break
        if not match:
            finished = True

    if len(polymer) < lowest:
        lowest = len(polymer)

print(lowest)
