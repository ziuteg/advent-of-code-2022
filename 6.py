def execute1(input):

    for i in range(len(input)):
        if len(set(input[i:i+4])) == 4:
            return i+4

    return None


def execute2(input):

    for i in range(len(input)):
        if len(set(input[i:i+14])) == 14:
            return i+14
            
    return None
