from math import gcd


def lcm(elems):
    a = elems[0]
    rest = elems[1:]
    if len(rest) == 1:
        b = rest[0]
        return a * b // gcd(a, b)
    else:
        return lcm([a, lcm(rest)])


def part1(input: str):
    nodes = {}
    instructions, rest = input.split("\n\n", 1)
    instructions = list(instructions)
    for line in rest.split("\n"):
        starting, data = line.split(" = ")
        left, right = data.strip("()").split(", ")
        nodes[starting] = (left, right)

    current_node = nodes["AAA"]
    n = 0
    while current_node != nodes["ZZZ"]:
        direction = 0 if instructions[n % len(instructions)] == "L" else 1
        current_node = nodes[current_node[direction]]
        n += 1

    return n


def part2(input: str):
    nodes = {}
    instructions, rest = input.split("\n\n", 1)
    instructions = list(instructions)
    positions = []
    for line in rest.split("\n"):
        starting, data = line.split(" = ")
        left, right = data.strip("()").split(", ")
        nodes[starting] = (left, right)
        if starting.endswith("A"):
            positions.append(nodes[starting])

    loops = []
    for position in positions:
        n = 0
        while True:
            direction = 0 if instructions[n % len(instructions)] == "L" else 1
            next = position[direction]
            if next.endswith("Z"):
                break
            position = nodes[next]
            n += 1
        loops.append(n + 1)

    return lcm(loops)
