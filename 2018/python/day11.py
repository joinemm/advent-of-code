# Project: advent_of_code
# File: day_11
# Author: Joinemm
# Date created: 17/12/18
# Python Version: 3.6.6

serial = 3031


def power_level(x, y):
    x += 1
    y += 1
    rack_id = x + 10
    level = rack_id * y
    level += serial
    level *= rack_id
    try:
        level = int(str(level)[-3])
    except IndexError:
        level = 0
    level -= 5
    return level


grid = []
for y in range(300):
    grid_row = []
    for x in range(300):
        grid_row.append(power_level(x, y))
    grid.append(grid_row)

# part 1
largest = (None, 0, 0)
for y in range(298):
    for x in range(298):
        largest_size = (0, 0)
        level = 0
        for i in range(3):
            level += sum(grid[y+i][x:x+3])
        if level > largest_size[1]:
            largest_size = (3, level)

        if largest_size[1] > largest[2]:
            largest = ((x + 1, y + 1), largest_size[0], largest_size[1])

print(f"{largest[0][0]},{largest[0][1]}")

# part 2
largest = (None, 0, 0)
for y in range(300):
    for x in range(300):
        space = min([300-y, 300-x])
        if space > 20:
            # randomly chosen cutoff
            space = 20

        largest_size = (0, 0)
        for size in range(1, space):
            size_level = 0
            for i in range(size):
                size_level += sum(grid[y+i][x:x+size])
            if size_level > largest_size[1]:
                largest_size = (size, size_level)

        if largest_size[1] > largest[2]:
            largest = ((x + 1, y + 1), largest_size[0], largest_size[1])

print(f"{largest[0][0]},{largest[0][1]},{largest[1]}")

