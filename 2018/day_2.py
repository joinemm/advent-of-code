# Project: advent_of_code
# File: day_2
# Author: Joinemm
# Date created: 04/12/18
# Python Version: 3.6.6

from collections import Counter
import string

ids = []
with open("input_2.txt", "r") as input:
    for line in input:
        box_id = line.rstrip()
        ids.append(box_id)

alphabets = list(string.ascii_lowercase)

twos = 0
threes = 0

for item in ids:
    two = False
    three = False
    counter = Counter(item)
    for char in alphabets:
        count = counter[char]
        if count == 3:
            three = True
        elif count == 2:
            two = True
        if two and three:
            break
    if two:
        twos += 1
    if three:
        threes += 1

print(twos * threes)

for item in ids:
    for x in ids:
        if x == item:
            break
        correct = True
        difference = 0
        sames = ""
        for i in range(len(item)):
            char = item[i]
            char2 = x[i]
            i += 1
            if char == char2:
                sames += char
            else:
                difference += 1
            if difference > 1:
                correct = False
                break
        if correct:
            print(sames)
