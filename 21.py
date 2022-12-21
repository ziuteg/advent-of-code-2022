def dfs(ops, values, node):
    if node in values:
        return values[node]

    op = ops[node][1]
    lhs = dfs(ops, values, ops[node][0])
    rhs = dfs(ops, values, ops[node][2])

    if lhs == None or rhs == None:
        return None

    if op == '+':
        return lhs + rhs
    elif op == '-':
        return lhs - rhs
    elif op == '/':
        return lhs // rhs
    elif op == '*':
        return lhs * rhs
    else:
        raise Exception('Unknown op: ' + op)


def find(ops, values, node, val=None):
    if node == 'humn':
        return val

    if node == 'root':
        return find(ops, values, ops[node][0], dfs(ops, values, ops[node][2]))

    op = ops[node][1]
    lhs = dfs(ops, values, ops[node][0])
    rhs = dfs(ops, values, ops[node][2])

    assert lhs == None or rhs == None
    assert lhs != None or rhs != None

    if op == '+':
        if lhs != None:
            return find(ops, values, ops[node][2], val - lhs)
        return find(ops, values, ops[node][0], val - rhs)
    elif op == '-':
        if lhs != None:
            return find(ops, values, ops[node][2], lhs - val)
        return find(ops, values, ops[node][0], val + rhs)
    elif op == '/':
        if lhs != None:
            return find(ops, values, ops[node][2], lhs // val)
        return find(ops, values, ops[node][0], val * rhs)
    elif op == '*':
        if lhs != None:
            return find(ops, values, ops[node][2], val // lhs)
        return find(ops, values, ops[node][0], val // rhs)
    else:
        raise Exception('Unknown op: ' + op)


def read_input(input):
    values = {}
    ops = {}

    for line in input.splitlines():
        items = line.split()

        if len(items) == 2:
            values[items[0][:-1]] = int(items[1])
        else:
            ops[items[0][:-1]] = items[1:]

    return ops, values


def execute1(input):
    ops, values = read_input(input)
    return dfs(ops, values, 'root')


def execute2(input):
    ops, values = read_input(input)
    values['humn'] = None
    return find(ops, values, 'root')
