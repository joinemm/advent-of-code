from math import ceil, floor, sqrt

# d = x(t - x)
# 0 = x(t - x) - d
# 0 = xt - x^2 - d
# 0 = -x^2 + tx - d
# solve with quadratic formula
# (-b +- sqrt(b^2 - 4ac))/2a
# where a = -1, b = -t, c = d


def quadratic_formula(a: int, b: int, c: int) -> tuple[int, int]:
    return [(-b - sqrt(b**2 - 4 * a * c) * i) / (2 * a) for i in [1, -1]]


def part1(input: str):
    times, distances = [
        [int(x) for x in line.split(":", 1)[1].split()] for line in input.split("\n")
    ]

    total = 1
    for time, distance in zip(times, distances):
        x1, x2 = quadratic_formula(1, time, distance)
        total *= ceil(x2) - floor(x1 + 1)

    return total


def part2(input: str):
    time, distance = [
        int("".join(line.split(":", 1)[1].split())) for line in input.split("\n")
    ]

    x1, x2 = quadratic_formula(1, time, distance)
    return ceil(x2) - floor(x1 + 1)
