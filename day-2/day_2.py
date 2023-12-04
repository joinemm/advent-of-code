from timeit import default_timer as timer

start = timer()
# setup
with open('input.txt', 'r') as f:
    intcode = [int(x) for x in f.read().split(',')]


def run(memory, noun, verb):
    memory[1] = noun
    memory[2] = verb
    i = 0
    while True:
        opcode, pos_1, pos_2, target_pos = memory[i:i+4]
        if opcode == 1:
            memory[target_pos] = memory[pos_1] + memory[pos_2]
        elif opcode == 2:
            memory[target_pos] = memory[pos_1] * memory[pos_2]
        elif opcode == 99:
            break
        else:
            print('something went wrong: opcode', opcode)
            break
        
        i += 4
    return memory[0] 


# part 1
print(f'{timer()-start:.4f}s', 'part 1:', run(intcode.copy(), 12, 2))


# part 2
for noun in range(100):
    for verb in range(100):
        result = run(intcode.copy(), noun, verb)
        if result == 19690720:
            print(f'{timer()-start:.4f}s', 'part 2:', (100 * noun + verb))
            quit()
