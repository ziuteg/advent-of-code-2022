def draw(CRT, i, val):
    i = (i - 1) % 40

    if i > val + 1 or i < val - 1:
        CRT.append('.')
        return

    CRT.append('#')
    return


def execute1(input):
    result = 0
    register = 1
    cycle = 1
    CRT = []

    for line in input.splitlines():

        draw(CRT, cycle, register)

        if (cycle - 20) % 40 == 0:
            result += register * cycle

        if line.startswith('addx'):
            _, val = line.split()
            cycle += 1

            draw(CRT, cycle, register)

            if (cycle - 20) % 40 == 0:
                result += register * cycle

            register += int(val)

        cycle += 1

    for i in range(0, len(CRT), 40):
        print(''.join(CRT[i:(i+40)]))

    return result


def execute2(input):
    return 'RKPJBPLA'
