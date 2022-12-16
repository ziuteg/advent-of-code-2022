from collections import defaultdict
from collections import deque
import functools


graph = {}
flow_rates = {}


def read_input(input):
    flow_rates = {}
    connections = defaultdict(list)

    for line in input.splitlines():
        items = line.split()
        
        a = items[1]
        
        flow = items[4]
        flow = int(flow.split('=')[1][:-1])

        if flow > 0:
            flow_rates[a] = flow

        valves = items[9:]
        for valve in valves:
            valve = valve[:2]
            connections[a].append(valve)

    return flow_rates, connections


def simplify(graph, flow_rates):
    nodes = set(graph.keys())
    simple = defaultdict()

    for node in nodes:
        queue = deque([(node, 0)])
        visited = set()

        while len(queue) > 0:
            current, dist = queue.popleft()
            visited.add(current)

            for neighbour in graph[current]:
                if neighbour not in visited:
                    queue.append((neighbour, dist + 1))
                    if neighbour not in flow_rates:
                        continue
                    simple[node, neighbour] = dist + 1

    return simple


@functools.cache
def search(time, node, valves):
    result = 0

    for next in valves:
        delta = time - graph[node, next] - 1

        if delta <= 0:
            continue

        total = flow_rates[next] * delta
        result = max(result, total + search(delta, next, valves - {next}))
    
    return result


@functools.cache
def double_search(time, node, valves):
    result = 0

    for next in valves:
        delta = time - graph[node, next] - 1

        if delta <= 0:
            continue

        total = flow_rates[next] * delta
        result = max(
            result,
            total + double_search(delta, next, valves - {next}),
            total + search(26, 'AA', valves - {next})
        )
    
    return result


def execute1(input):    
    global flow_rates
    global graph

    flow_rates, connections = read_input(input)
    graph = simplify(connections, flow_rates)

    return search(30, 'AA', frozenset(flow_rates.keys()))


def execute2(input):
    global flow_rates
    global graph

    flow_rates, connections = read_input(input)
    graph = simplify(connections, flow_rates)

    return double_search(26, 'AA', frozenset(flow_rates.keys()))
