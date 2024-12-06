import sys
from enum import Enum

directions = {"<": (0, -1), ">": (0, 1), "v": (1, 0), "^": (-1, 0)}
rotation = {"<": "^", "^": ">", ">": "v", "v": "<"}


class State(Enum):
    FREE = 1
    BLOCKED = 2
    OUT = 3


class Guard:
    def __init__(self, map):
        (self.direction, self.position) = self.find_initial_position(map)
        self.visited_postions = 0
        self.map = map
        self.state = State.FREE

    def __str__(self):
        return f"direction: {self.direction}, position: {self.position}"

    def find_initial_position(self, map):
        for row_idx, row in enumerate(map):
            for col_idx, elem in enumerate(row):
                if elem in directions.keys():
                    return elem, (row_idx, col_idx)
        return None, None

    def turn_right(self):
        self.direction = rotation[self.direction]
        self.state = State.FREE

    def is_out(self, position):
        map_width = len(self.map[0])
        map_height = len(self.map)
        if (
            position[0] >= map_height
            or position[0] < 0
            or position[1] >= map_width
            or position[1] < 0
        ):
            return True
        return False

    def is_blocked(self, position):
        if self.map[position[0]][position[1]] == "#":
            return True
        return False

    def mark_visited_position(self, position):
        if self.map[position[0]][position[1]] != "X":
            self.visited_postions += 1
        row = list(self.map[position[0]])
        row[position[1]] = "X"
        self.map[position[0]] = "".join(row)

    def move_forward(self):
        (y_step, x_step) = directions[self.direction]
        initial_position = self.position
        new_position = (self.position[0] + y_step, self.position[1] + x_step)
        if self.is_out(new_position):
            self.mark_visited_position(initial_position)
            self.state = State.OUT
            return
        elif self.is_blocked(new_position):
            self.state = State.BLOCKED
            return
        else:
            self.mark_visited_position(initial_position)
            self.state = State.FREE
        self.position = new_position

    def patrol(self):
        history = {"<": [], "^": [], ">": [], "v": []}
        while self.state is not State.OUT:
            if check_history(history, self.direction, self.position):
                return self.visited_postions
            else:
                history[guard.direction].append(guard.position)
            while self.state is State.FREE:
                self.move_forward()
            if self.state is State.BLOCKED:
                self.turn_right()
        return self.visited_postions

    def print_map(self):
        for row in self.map:
            print(row)


def check_history(history, direction, position):
    if position in history[direction]:
        return True
    return False


guard_map_path = sys.argv[1]
with open(guard_map_path) as file:
    lines = file.read().splitlines()
    guard_map = lines
guard = Guard(guard_map)
visited_position = guard.patrol()
guard.print_map()
print(f"The guard visited {visited_position} positions!")
