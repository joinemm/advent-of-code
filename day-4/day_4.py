from timeit import default_timer as timer
import math

start = timer()

# puzzle input
# 231832-767346
begin = 231832
end = 767346

passwords_1 = set()
passwords_2 = set()

n = begin
while n <= end:
    adjacent = {}
    breakpoint = None
    multiplier = 1
    prev = int(str(n)[0])
    for i, d in enumerate([int(x) for x in str(n)[1:]]):
        if d < prev:
            breakpoint = 4 - i
            multiplier = prev - d
            break
        elif d == prev:
            if str(d) in adjacent:
                adjacent[str(d)] += 1
            else:
                adjacent[str(d)] = 2
            
        prev = d
   
    if breakpoint is None:
        breakpoint = 0
        if adjacent.values():
            passwords_1.add(n)
        if 2 in adjacent.values():
            passwords_2.add(n)

    addition = int(math.pow(10, breakpoint))*multiplier
    if breakpoint != 0:
        addition -= int(str(n)[-breakpoint:])
        addition += int(str(prev)*breakpoint)

    n += addition

print(f'{timer()-start:.4f}', 'part 1:', len(passwords_1))
print(f'{timer()-start:.4f}', 'part 2:', len(passwords_2))
