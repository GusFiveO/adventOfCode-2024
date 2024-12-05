with open("./word_grid.txt") as file:
    lines = file.read().splitlines()
letter_matrix = lines

word = "XMAS"

width = len(letter_matrix[0])
height = len(letter_matrix)

directions = [(1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]


def is_valid(y, x):
    return y >= 0 and y < height and x >= 0 and x < width


def check_direction(letter_matrix, y, x, direction):
    (y_step, x_step) = direction
    for i in range(len(word)):
        if is_valid(y, x) is not True or word[i] != letter_matrix[y][x]:
            return False
        y += y_step
        x += x_step
    return True


def find_word(letter_matrix, y, x):
    count = 0
    for direction in directions:
        if check_direction(letter_matrix, y, x, direction) is True:
            count += 1
    return count


count = 0
for y in range(height):
    for x in range(width):
        if letter_matrix[y][x] == word[0]:
            count += find_word(letter_matrix, y, x)

print(f"Word: ({word}) have been found", count, "times")
