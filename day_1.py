# Project: advent_of_code
# File: day_1
# Author: Joinemm
# Date created: 04/12/18
# Python Version: 3.6.6

changes = []
with open("input_1.txt", "r") as input:
    for line in input:
        change = int(line.rstrip())
        changes.append(change)

results = [0]
found = False
while not found:
    for x in changes:
        result = results[-1]
        result += x
        if result in results:
            print(result)
            found = True
            break
        else:
            results.append(result)
