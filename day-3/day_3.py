from timeit import default_timer as timer

start = timer()
with open('input.txt', 'r') as f:
    A, B = [x.split(',') for x in f.read().splitlines()]

operations = {
    'R': (1, 0),
    'L': (-1, 0),
    'U': (0, 1),
    'D': (0, -1)
}

def get_coords(wire):
    head = (0, 0)
    coords = []
    for instruction in wire:
        delta = operations[instruction[0]]
        n = int(instruction[1:])
        for _ in range(n):
            head = (head[0] + delta[0], head[1] + delta[1])
            coords.append(head)
    
    return coords

A = get_coords(A)
B = get_coords(B)

collisions = set(A).intersection(B)

distances = set()
lowest = len(A)
for location in collisions:
    distances.add(abs(0 - location[0]) + abs(0 - location[1]))
    try:
        steps_1 = A[:lowest].index(location)
        steps_2 = B[:lowest].index(location)
        lowest = steps_1 + steps_2 + 2
    except ValueError:
        continue


print(f'{timer()-start:.4f}s', 'part 1:', min(distances))
print(f'{timer()-start:.4f}s', 'part 2:', lowest)
