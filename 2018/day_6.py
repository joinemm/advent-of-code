# Project: advent_of_code
# File: day_6
# Author: Joinemm
# Date created: 06/12/18
# Python Version: 3.6.6

coordinates = {}
with open("input_6.txt", "r") as input:
    for line in input:
        line_coords = line.rstrip().split(", ")
        x = int(line_coords[0])
        y = int(line_coords[1])
        coords = (x, y)
        coordinates[coords] = 0

region_area = 0
orig_coordinates = dict(coordinates)
size = 400
for y in range(size):
    for x in range(size):
        two_coords = False
        distances = []
        for coord in orig_coordinates:
            d = abs(coord[0]-x) + abs(coord[1]-y)
            distances.append((d, coord))

        total_distance = 0
        for tup in distances:
            total_distance += tup[0]
        if total_distance < 10000:
            region_area += 1

        if sorted(distances)[0][0] == sorted(distances)[1][0]:
            two_coords = True

        if not two_coords and distances:
            closest = sorted(distances)[0][1]
            if y == 0 or y == size-1 or x == 0 or x == size-1:
                if closest in coordinates:
                    del(coordinates[closest])
            elif closest in coordinates:
                coordinates[closest] += 1

print(sorted(coordinates.values())[-1])
print(region_area)
