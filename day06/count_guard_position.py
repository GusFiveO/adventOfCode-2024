import sys
from enum import Enum

directions = {"<": (0, -1), ">": (0, 1), "v": (1, 0), "^": (-1, 0)}
rotation = {"<": "^", "^": ">", ">": "v", "v": "<"}


class State(Enum):
    FREE = 1
    BLOCKED = 2
    OUT = 3


class Guard:
    def __init__(self, direction_symbol, position, map):
        self.direction = directions[direction_symbol]
        self.position = position
        self.map = map
        self.state = State.FREE

    def __str__(self):
        return f"direction: {self.direction}, position: {self.position}"

    def find_initial_position(map):
        for row_idx, row in enumerate(map):
            for col_idx, elem in enumerate(row):
                if elem in directions.keys:
                    return (directions[elem], (row_idx, col_idx))

    def turn_right(self):
        direction_symbol = rotation[self.direction]
        self.direction = directions[direction_symbol]

    def is_out(self, position):
        map_width = len(self.map[0])
        map_height = len(self.map)
        if (
            position[0] > map_height
            or position[0] < 0
            or position[1] > map_width
            or position[1] < 0
        ):
            return True
        return False

    def is_blocked(self, position):
        if self.map[position[0]][position[1]] == "#":
            return True
        return False

    def mark_visited_position(self, position):
        print(self.map[position[0]][position[1]])
        row = list(self.map[position[0]])
        row[position[1]] = "X"
        self.map[position[0]] = "".join(row)

    def move_forward(self):
        (y_step, x_step) = self.direction
        initial_position = self.position
        new_position = (self.position[0] + y_step, self.position[1] + x_step)
        if self.is_out(new_position):
            self.mark_visited_position(initial_position)
            self.state = State.OUT
        elif self.is_blocked(new_position):
            self.state = State.BLOCKED
        else:
            self.mark_visited_position(initial_position)
            self.state = State.FREE


guard_map_path = sys.argv[1]
with open(guard_map_path) as file:
    lines = file.read().splitlines()
    guard_map = lines
guard = Guard(">", (0, 0), guard_map)
guard.move_forward()
print(guard)
print(guard_map)
