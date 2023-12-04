from timeit import default_timer as timer

start = timer()
with open('input.txt', 'r') as f:
    intcode = [int(x) for x in f.read().split(',')]

def get_values(memory, i, modes, param_amount):
    params = memory[i+1:i+param_amount+1]
    values = [param if mode == 1 else memory[param] for param, mode in zip(params, modes)]
    return params, values

# part 1
memory = intcode.copy()
input_value = 1
i = 0
while True:
    instruction = str(memory[i]).zfill(5)
    opcode = int(instruction[-2:])
    modes = [int(x) for x in reversed(instruction[:3])]
    if opcode == 1:
        params = memory[i+1:i+4]
        values = [param if mode == 1 else memory[param] for param, mode in zip(params, modes)]
        memory[params[2]] = values[0] + values[1]
    elif opcode == 2:
        params = memory[i+1:i+4]
        values = [param if mode == 1 else memory[param] for param, mode in zip(params, modes)]
        memory[params[2]] = values[0] * values[1]
    elif opcode == 3:
        # takes a single integer as input and saves it to the position given by its only parameter
        params = memory[i+1:i+2]
        memory[params[0]] = input_value
    elif opcode == 4:
        # outputs the value of its only parameter
        params = memory[i+1:i+2]
        values = [param if mode == 1 else memory[param] for param, mode in zip(params, modes)]
        if values[0] != 0:
            # dont print debug zeros
            print(f'{timer()-start:.4f}s', 'part 1:', values[0])
    elif opcode == 99:
        break
    else:
        print('something went wrong: opcode', opcode, instruction)
        break

    i += len(params) + 1


# part 2
memory = intcode.copy()
input_value = 5
i = 0
while True:
    instruction = str(memory[i]).zfill(5)
    opcode = int(instruction[-2:])
    modes = [int(x) for x in reversed(instruction[:3])]
    if opcode == 1:
        params, values = get_values(memory, i, modes, 3)
        memory[params[2]] = values[0] + values[1]
    
    elif opcode == 2:
        params, values = get_values(memory, i, modes, 3)
        memory[params[2]] = values[0] * values[1]

    elif opcode == 3:
        params = memory[i+1:i+2]
        memory[params[0]] = input_value

    elif opcode == 4:
        params, values = get_values(memory, i, modes, 1)
        if values[0] != 0:
            # dont print debug zeros
            print(f'{timer()-start:.4f}s', 'part 2:', values[0])
    
    elif opcode == 5:
        params, values = get_values(memory, i, modes, 2)
        if values[0] != 0:
            i = values[1]
            continue

    elif opcode == 6:
        params, values = get_values(memory, i, modes, 2)
        if values[0] == 0:
            i = values[1]
            continue
    
    elif opcode == 7:
        params, values = get_values(memory, i, modes, 3)
        if values[0] < values[1]:
            memory[params[2]] = 1
        else:
            memory[params[2]] = 0

    elif opcode == 8:
        params, values = get_values(memory, i, modes, 3)
        if values[0] == values[1]:
            memory[params[2]] = 1
        else:
            memory[params[2]] = 0

    elif opcode == 99:
        break
    
    else:
        print('something went wrong: opcode', opcode, instruction)
        break
    
    i += len(params) + 1
