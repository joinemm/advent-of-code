# Project: advent_of_code
# File: day_7
# Author: Joinemm
# Date created: 07/12/18
# Python Version: 3.6.6

import string

instructions = []
with open("input_7.txt", "r") as input:
    for line in input:
        instructions.append(line.rstrip())

prerequisites = {}
step_state = {}
for x in string.ascii_uppercase:
    step_state[x] = False
    prerequisites[x] = []

for line in instructions:
    line = line.replace("Step ", "").replace(" must be finished before step", "").replace(" can begin.", "")
    prerequisite, step = line.split(" ")
    prerequisites[step].append(prerequisite)

worker = {"working_on": None, "time_remaining": 0}
workers = []
for i in range(5):
    workers.append(dict(worker))

result = ""
time = -1
while False in step_state.values() or None in step_state.values():
    can_do = []
    for worker in workers:
        if worker['working_on'] is not None:
            if worker['time_remaining'] == 1:
                result += worker['working_on']
                step_state[worker['working_on']] = True
                worker['working_on'] = None
                worker['time_remaining'] = 0
            else:
                worker['time_remaining'] -= 1

    for letter in prerequisites:
        if step_state[letter] == False:
            all_preqs = True
            if prerequisites[letter]:
                for step in prerequisites[letter]:
                    if step_state[step]:
                        continue
                    else:
                        all_preqs = False
                        break
            if all_preqs:
                can_do.append(letter)

    if can_do:
        for letter in sorted(can_do):
                for worker in workers:
                    if worker['working_on'] is None and step_state[letter] == False:
                        worker['working_on'] = letter
                        worker['time_remaining'] = 61 + string.ascii_uppercase.index(letter)
                        step_state[letter] = None
    time += 1

print(result)
print(time)
