def parse_input(input):
    input, ops = input.split('\n\n')
    input = input.splitlines()
    input.pop()

    stacks = [[] for _ in range(len(input)+1)]

    for line in input:
        for i in range(0, len(line), 4):
            if line[i+1] != ' ':
                stacks[i//4].append(line[i+1])

    for stack in stacks:
        stack.reverse()

    ops = ops.replace('move ', '')
    ops = ops.replace(' from ', ',')
    ops = ops.replace(' to ', ',').splitlines()
    ops = [list(map(int, list(op.split(',')))) for op in ops]

    return stacks, ops


def execute1(input):
    result = ''
    stacks, ops = parse_input(input)

    for n, a, b in ops:
        for _ in range(n):
            stacks[b-1].append(stacks[a-1].pop())

    for stack in stacks:
        result += stack[-1]

    return result


def execute2(input):
    result = ''
    stacks, ops = parse_input(input)

    for n, a, b in ops:
        arr = []
        for _ in range(n):
            arr.append(stacks[a-1].pop())
        stacks[b-1] += reversed(arr)

    for stack in stacks:
        result += stack[-1]

    return result
