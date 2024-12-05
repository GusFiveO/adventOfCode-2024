with open("./word_grid.txt") as file:
    lines = file.read().splitlines()
letter_matrix = lines

middle_letter = "A"

width = len(letter_matrix[0])
height = len(letter_matrix)

directions = [(1, 1), (-1, 1)]
neighbours = ["S", "M"]


def is_valid(y, x):
    return y >= 0 and y < height and x >= 0 and x < width


def get_opposite_neighbour(current_neighbour):
    index = neighbours.index(current_neighbour)
    opposite_neighbour = neighbours[1 - index]
    return opposite_neighbour


def check_neighbours(letter_matrix, y, x):
    for direction in directions:
        (y_step, x_step) = direction
        tmp_y = y
        tmp_x = x
        tmp_y += y_step
        tmp_x += x_step
        if is_valid(y, x) is not True:
            return False
        else:
            try:
                current_neighbour = letter_matrix[tmp_y][tmp_x]
                opposite_neighbour = get_opposite_neighbour(current_neighbour)
                tmp_y = y - y_step
                tmp_x = x - x_step
                if letter_matrix[tmp_y][tmp_x] != opposite_neighbour:
                    return False
            except Exception:
                return False
    return True


def find_word(letter_matrix, y, x):
    count = 0
    if check_neighbours(letter_matrix, y, x) is True:
        count += 1
    return count


count = 0
for y in range(height):
    for x in range(width):
        if letter_matrix[y][x] == middle_letter:
            count += find_word(letter_matrix, y, x)

print("X-MAS have been found", count, "times")
