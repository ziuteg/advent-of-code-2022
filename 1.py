def calc_totals(input):
    return [sum(map(int, list.splitlines())) for list in input.split('\n\n')]


def execute1(input):
    return max(calc_totals(input))


def execute2(input):
    return sum(sorted(calc_totals(input))[-3:])
