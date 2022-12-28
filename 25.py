MAPPING = {
    '=': -2,
    '-': -1,
    '0': 0,
    '1': 1,
    '2': 2,
}


def snafu_to_dec(snafu):
    result = 0
    for i, item in enumerate(reversed(snafu)):
        result += MAPPING[item] * 5 ** i
    return result


def dec_to_snafu(dec):
    result = ''

    while dec != 0:
        rest = dec % 5
        if rest == 3:
            dec += 2
            result += '='
        elif rest == 4:
            dec += 1
            result += '-'
        else:
            result += str(rest)
        dec //= 5

    return ''.join(reversed(result))


def execute1(input):
    result = 0

    for line in input.splitlines():
        result += snafu_to_dec(line)

    return dec_to_snafu(result)