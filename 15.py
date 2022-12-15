def read_input(input):
    x_min = 99999999
    x_max = -99999999
    beacons = set()
    sensors = set()
    dist = {}
    dmax = 0

    for line in input.splitlines():
        item = line.split()

        sensor = tuple(map(int, (item[2][2:-1], item[3][2:-1])))
        sensors.add(sensor)

        beacon = tuple(map(int, (item[8][2:-1], item[9][2:])))
        beacons.add((beacon))
        
        x_min = min(x_min, beacon[0])
        x_max = max(x_max, beacon[0])

        dist[sensor] = abs(sensor[0]-beacon[0]) + abs(sensor[1]-beacon[1])
        dmax = max(dmax, dist[sensor])
    
    return sensors, beacons, dist, x_min-dmax, x_max+dmax


def execute1(input):
    sensors, beacons, dist, x_min, x_max = read_input(input)
    
    result = 0
    y = 2000000

    for x in range(x_min, x_max+1):
        for sensor in sensors:
            if dist[sensor] >= abs(sensor[0]-x) + abs(sensor[1]-y):
                if (x, y) in beacons:
                    continue
                if (x, y) in sensors:
                    continue
                result += 1
                break

    return result


def tuning_frequency(x, y):
    return 4000000 * x + y


def execute2(input):
    sensors, _, dist, _, _ = read_input(input)

    limit = 4000000

    for y in range(0, limit+1):
        starts = []
        ends = []
        for sensor in sensors:
            dy = dist[sensor]-abs(sensor[1]-y)
            if dy < 0:
                continue
            starts.append(sensor[0]-dy)
            ends.append(sensor[0]+dy+1)

        starts.sort()
        ends.sort()

        if starts[0] > 0:
            return tuning_frequency(starts[0], y)
        if ends[-1] < limit:
            return tuning_frequency(ends[-1], y)

        coverage = 0
        start_index = 0
        end_index = 0
        while start_index < len(starts) and end_index < len(ends):
            if starts[start_index] <= ends[end_index]:
                coverage += 1
                start_index += 1
            else:
                coverage -= 1
                end_index += 1
            if coverage == 0:
                return tuning_frequency(starts[start_index]-1, y)

    return None
