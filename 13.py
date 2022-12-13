from functools import cmp_to_key


def parse_input(input):
    input = '[' + input.replace('\n\n', ',').replace('\n', ',') + ']'
    return eval(input)


def compare(a, b):
    if isinstance(a, int) and isinstance(b, int):
        return 1 if a < b else 0 if a == b else -1
    if isinstance(a, int):
        return compare([a], b)
    if isinstance(b, int):
        return compare(a, [b])
    for i in range(len(a)):
        if i >= len(b):
            return -1
        val = compare(a[i], b[i])
        if val != 0:
            return val
    if len(a) < len(b):
        return 1
    return 0


def execute1(input):
    input = parse_input(input)

    result = 0
    
    for i in range(0, len(input), 2):
        a = input[i]
        b = input[i+1]

        if compare(a, b) == 1:
            print('right', a, b, i//2+1)
            result += i//2+1

    return result


def execute2(input):
    input = parse_input(input)

    input.append([[2]])
    input.append([[6]])

    sorted_data = list(reversed(sorted(input, key=cmp_to_key(compare))))

    result = 1

    for i in range(len(sorted_data)):
        if sorted_data[i] == [[2]] or sorted_data[i] == [[6]]:
            result *= i+1

    return result
