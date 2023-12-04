# Project: advent_of_code
# File: day_12
# Author: Joinemm
# Date created: 17/12/18
# Python Version: 3.6.6

from collections import deque

initial_state = "##...#......##......#.####.##.#..#..####.#.######.##..#.####...##....#.#.####.####.#..#.######.##..."

instructions = []
with open('input_12.txt', 'r') as input:
    for line in input:
        row = []
        for char in line:
            if char == "#":
                row.append(1)
            elif char == ".":
                row.append(0)
            else:
                continue

        instructions.append((row[:5], row[-1]))

print(instructions)
