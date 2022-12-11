def parse_input(input):
    result = []
    gcd = 1

    for monkey_input in input.split('\n\n'):
        monkey_input = list(monkey_input.splitlines())

        items = list(map(int, monkey_input[1].split(': ')[1].split(',')))
        op = lambda old, expr=monkey_input[2].split('= ')[1] : eval(expr)
        test = int(monkey_input[3].split()[-1])
        if_true = int(monkey_input[4].split()[-1])
        if_false = int(monkey_input[5].split()[-1])

        # Using the assumption that all test values are co-prime
        gcd *= test

        result.append([items, op, test, if_true, if_false])

    return result, gcd


def solve(input, part):
    monkeys, gcd = parse_input(input)
    counts = [0 for i in range(len(monkeys))]
    turns = 20 if part == 1 else 10000

    for _ in range(turns):
        for monkey_index in range(len(monkeys)):
            items, op, test, if_true, if_false = monkeys[monkey_index]
            counts[monkey_index] += len(items)

            for item in items:
                item = op(item) // 3 if part == 1 else op(item) % gcd

                if item % test == 0:
                    monkeys[if_true][0].append(item)
                else:
                    monkeys[if_false][0].append(item)

            monkeys[monkey_index][0] = []

    
    counts.sort()

    return counts[-1] * counts[-2]


def execute1(input):
    return solve(input, 1)


def execute2(input):
    return solve(input, 2)