# Project: advent_of_code
# File: day_3
# Author: Joinemm
# Date created: 04/12/18
# Python Version: 3.6.6

claims = []
with open("input_3.txt", "r") as input:
    for line in input:
        claim = line.rstrip()
        claims.append(claim)

size = 1100
world = [[0]*size for i in range(size)]

claims_two = []
for claim in claims:
    claim_id = claim.split("@")[0].rstrip()
    position_data = claim.split("@")[1].split(":")
    coords = position_data[0].rstrip().split(",")
    x_pos = int(coords[0])
    y_pos = int(coords[1])
    dimensions = position_data[1].rstrip().split("x")
    width = int(dimensions[0])
    height = int(dimensions[1])
    claims_two.append([x_pos, y_pos, width, height, claim_id])

    for y in range(height):
        for x in range(width):
            world[y_pos+y][x_pos+x] += 1

for claim in claims_two:
    failed = False
    for y in range(claim[3]):
        for x in range(claim[2]):
            if world[claim[1]+y][claim[0]+x] > 1:
                failed = True
    if not failed:
        print(claim[4])

claimed = 0
for y in range(size):
    for x in range(size):
        if world[y][x] > 1:
            claimed += 1

print(claimed)
