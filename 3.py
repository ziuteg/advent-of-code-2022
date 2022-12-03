
def calc_priority(i):
    if i.isupper():
        return ord(i) - ord('A') + 27
    return ord(i) - ord('a') + 1

def execute1(input):
    result = 0

    for line in input.splitlines():
        a, b = map(set, [line[:len(line)//2], line[len(line)//2:]])

        for i in a.intersection(b):
            result += calc_priority(i)

    return result


def execute2(input):
    result = 0

    input = list(input.splitlines())

    for i in range(0, len(input), 3):
        a, b, c = map(set, [input[i], input[i+1], input[i+2]])

        for i in a.intersection(b, c):
            result += calc_priority(i)
            
    return result
