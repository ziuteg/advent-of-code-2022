class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

    def shift_right(self):
        a = self.prev
        b = self.next
        a.next = b
        b.prev = a

        self.next = b.next
        self.prev = b
        b.next.prev = self
        b.next = self

    def shift_left(self):
        a = self.prev
        b = self.next
        a.next = b
        b.prev = a

        self.next = a
        self.prev = a.prev
        a.prev.next = self
        a.prev = self

    def shift(self, steps):
        if steps > 0:
            for _ in range(steps):
                self.shift_right()
        elif steps < 0:
            for _ in range(-steps):
                self.shift_left()


class CircularList:
    def __init__(self, vals):
        self.head = Node(vals[0])
        self.head.next = self.head
        self.head.prev = self.head
        self.tail = self.head
        self.length = 1
        for val in vals[1:]:
            self.append(val)

    def append(self, val):
        node = Node(val)
        node.prev = self.tail
        node.next = self.head
        self.tail.next = node
        self.tail = node
        self.head.prev = node
        self.length += 1

    def __str__(self):
        node = self.head
        s = ''
        while node.next != self.head:
            s += str(node.val) + ' '
            node = node.next
        s += str(node.val)
        return s


def read_input(input, key=1):
    nums = []
    for line in input.splitlines():
        nums.append(int(line) * key)

    cycle = CircularList(nums)

    nodes = []
    node = cycle.head
    start = None
    while node not in nodes:
        nodes.append(node)
        node = node.next
        if node.val == 0:
            start = node

    return start, nodes


def mix(nodes):
    start = None
    for node in nodes:
        if node.val == 0:
            start = node
            continue

        offset = node.val
        if node.val < 0:
            offset = -(abs(offset) % (len(nodes)-1))
        else:
            offset = node.val % (len(nodes)-1)

        node.shift(offset)
    return start


def execute1(input):
    start, nodes = read_input(input)

    mix(nodes)

    result = 0
    for i in range(3001):
        if i % 1000 == 0:
            result += start.val
        start = start.next
    return result


def execute2(input):
    start, nodes = read_input(input, 811589153)

    for _ in range(10):
        mix(nodes)

    result = 0
    for i in range(3001):
        if i % 1000 == 0:
            result += start.val
        start = start.next
    return result