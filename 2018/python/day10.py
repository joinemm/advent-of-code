# Project: advent_of_code
# File: day_10
# Author: Joinemm
# Date created: 17/12/18
# Python Version: 3.6.6

import re

stars = []
with open("input_10.txt", "r") as input:
    for line in input:
        finds = re.findall('<(.*?)>', line)
        initial = [int(finds[0].split(",")[0]), int(finds[0].split(",")[1])]
        velocity = [int(finds[1].split(",")[0]), int(finds[1].split(",")[1])]
        stars.append(initial + velocity)


def pass_time():
    min_x = None
    min_y = None
    max_x = 0
    max_y = 0
    for star in stars:
        star[0] += star[2]
        star[1] += star[3]

        if min_x is None:
            min_x = star[0]
        elif star[0] < min_x:
            min_x = star[0]

        if min_y is None:
            min_y = star[1]
        elif star[1] < min_y:
            min_y = star[1]

        if star[0] > max_x:
            max_x = star[0]
        if star[1] > max_y:
            max_y = star[1]

    if min_x < 0:
        dx = abs(min_x)
    else:
        dx = -min_x
    if min_y < 0:
        dy = abs(min_y)
    else:
        dy = -min_y

    if dy+max_y < 11:
        grid = [["."] * (dx+max_x+1) for i in range(dy+max_y+1)]
        for star in stars:
            grid[star[1] + dy][star[0] + dx] = "#"

        for row in grid:
            for char in row:
                print(char, end="")
            print("\n", end="")
        return False
    else:
        return True


go = True
time = 0
while go:
    go = pass_time()
    time += 1

print(time)
