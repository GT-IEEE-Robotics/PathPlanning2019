#returns object to prioritize based on input

def block_sort(blocks, attribute):
    #blocks is a list of tupes, properties are distance(0), color(1), shape(2)
    match = []
    if type(attribute) == int:
        index = 0
    elif attribute == 'red' or 'green' or 'red' or 'blue':
        index = 1
    elif attribute == 'cube' or 'sphere':
        index = 2
    else:
        print('attribute does not exist')
        return None
    for b in blocks:
        if b[index] == attribute:
            match.append(b)
    return match

class __main__:
    blocks_test = ((5, 'red', 'sphere'), (3, 'blue', 'cube'), (10, 'red', 'cube'))
    print(block_sort(blocks_test, 'red'))
