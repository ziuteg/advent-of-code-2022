def get_range(x):
    return list(map(int, x.split('-')))


def contains(a, b, x, y):
    return a <= x <= b and a <= y <= b


def overlaps(a, b, x, y):
    return a <= x <= b or a <= y <= b


def execute1(input):
    result = 0

    for line in input.splitlines():
        a, b = map(get_range, line.split(','))

        if contains(*a, *b) or contains(*b, *a):
            result += 1
        
    return result


def execute2(input):
    result = 0

    for line in input.splitlines():
        a, b = map(get_range, line.split(','))

        if overlaps(*a, *b) or overlaps(*b, *a):
            result += 1

    return result
