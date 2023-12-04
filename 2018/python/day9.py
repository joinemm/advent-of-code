# Project: advent_of_code
# File: day_9
# Author: Joinemm
# Date created: 09/12/18
# Python Version: 3.6.6

from collections import deque

# input: 459 players; last marble is worth 71320 points
max_marble = 71320*100
playercount = 459

circle = deque([0])
marble_n = 1
scores = [0] * playercount
player = 1


def turn(n):
    if n % 23 == 0:
        scores[player-1] += n
        circle.rotate(7)
        scores[player-1] += circle.pop()
        circle.rotate(-1)
    else:
        circle.rotate(-1)
        circle.append(n)
    n += 1
    return n


while marble_n <= max_marble:
    marble_n = turn(marble_n)
    player += 1
    if player > playercount:
        player = 1

print(max(scores))
