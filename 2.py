from collections import defaultdict

SCORES = defaultdict(int, {
    'AX': 3,
    'BY': 3,
    'CZ': 3,
    'AY': 6,
    'BZ': 6,
    'CX': 6,
})


def execute1(input):
    result = 0

    for line in input.splitlines():
        a, b = line.split()
        result += ord(b) - ord('X') + 1
        result += SCORES[a + b]

    return result


MAPPINGS = {
    'AX': 'Z',
    'BX': 'X',
    'CX': 'Y',
    'AY': 'X',
    'BY': 'Y',
    'CY': 'Z',
    'AZ': 'Y',
    'BZ': 'Z',
    'CZ': 'X',
}


def execute2(input):
    result = 0

    for line in input.splitlines():
        a, b = line.split()
        b = MAPPINGS[a + b]
        result += ord(b) - ord('X') + 1
        result += SCORES[a + b]

    return result
