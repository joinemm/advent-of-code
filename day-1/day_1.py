from timeit import default_timer as timer

start = timer()
# part 1
total = 0
for mass in open('input.txt', 'r'):
    total += (int(mass) // 3) - 2

print(f'{timer()-start:.4f}s', 'part 1:', total)


# part 2
def get_fuel(mass):
    fuel = (mass // 3) - 2
    if fuel > 0:
        fuel += get_fuel(fuel)
    elif fuel < 0:
        fuel = 0
    return fuel

total = 0
for mass in open('input.txt', 'r'):
    total += get_fuel(int(mass))

print(f'{timer()-start:.4f}s', 'part 2:', total)
