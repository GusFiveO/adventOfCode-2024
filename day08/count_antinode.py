import sys

def print_map(map):
    for row in map:
        print(row)

def compute_difference(point1, point2):
    y = point1[0] - point2[0]
    x = point1[1] - point2[1]
    return (y, x)

def find_next_antenna(antenna, map):
    antenna_y, antenna_x = antenna
    target = map[antenna_y][antenna_x]
    # print("target", target)
    # print_map(map[antenna_y:])
    for y, row in enumerate(map[antenna_y:]):
        for x, elem in enumerate(row):
            if x == antenna_x and y + antenna_y == antenna_y:
                continue
            elif elem == target:
                print(y, x)
                return y + antenna_y, x

    return None

def store_antinodes(antenna_1, antenna_2, map):
    difference = compute_difference(antenna_1, antenna_2)
    print("difference", difference, antenna_1, antenna_2)
    print(map[antenna_1[0] + difference[0]][antenna_1[1] + difference[1]])
    # map[antenna_1[0] + difference[0]][antenna_1[1] + difference[1]] = '#'
    row = map[antenna_1[0] + difference[0]]
    row = row[:antenna_1[1] + difference[1]] + "#" + row[antenna_1[1] + difference[1] + 1:]
    map[antenna_1[0] + difference[0]] = row
    row2 = map[antenna_2[0] - difference[0]]
    row2 = row2[:antenna_2[1] - difference[1]] + "#" + row2[antenna_2[1] - difference[1] + 1:]
    map[antenna_2[0] - difference[0]] = row2



file_path = sys.argv[1]
with open(file_path) as file:
    antennas_map = file.read().splitlines()
    print_map(antennas_map)

for y, row in enumerate(antennas_map):
    for x, elem in enumerate(row):
        print(elem)
        if elem != '.' and elem != '#':
            print((y,x), elem)
            next_antenna = find_next_antenna((y,x), antennas_map)
            if next_antenna is None:
                continue
            else:
                store_antinodes((y, x), next_antenna, antennas_map)
                print_map(antennas_map)
                exit()

# next_antenna = find_next_antenna((5,6), antennas_map)
# print(next_antenna)
