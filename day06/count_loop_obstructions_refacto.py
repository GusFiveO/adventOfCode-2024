import sys
from enum import Enum
import copy

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

    def move_forward(self):
        (y_step, x_step) = directions[self.direction]
        new_position = (self.position[0] + y_step, self.position[1] + x_step)
        if self.is_out(new_position):
            self.state = State.OUT
            return
        elif self.is_blocked(new_position):
            self.turn_right()
            return
        # else:
        #     self.state = State.FREE
        self.position = new_position

    def add_obstacle_forward(self, position):
        map_width = len(self.map[0])
        map_height = len(self.map)
        # position = (
        #     self.position[0] + directions[self.direction][0],
        #     self.position[1] + directions[self.direction][1],
        # )
        if (
            position[0] >= map_height
            or position[0] < 0
            or position[1] >= map_width
            or position[1] < 0
            or self.map[position[0]][position[1]] != "."
        ):
            return False
        row = list(self.map[position[0]])
        row[position[1]] = "#"
        self.map[position[0]] = "".join(row)
        return True

    def find_obstacles(self):
        obstacles = set()
        i = 0
        while self.state is not State.OUT:
            tmp_guard = copy.deepcopy(self)
            # if tmp_guard.add_obstacle_forward() and is_in_a_loop(
            if is_in_a_loop(tmp_guard, self.position, self.direction):
                # print("LOOP")
                position = (
                    self.position[0] + directions[self.direction][0],
                    self.position[1] + directions[self.direction][1],
                )
                obstacles.add(position)
            # else:
            # print("PAS LOOP")
            i += 1
            self.move_forward()
        return obstacles


def print_map(map):
    for row in map:
        print(row)


def check_history(history, direction, position):
    if position in history[direction]:
        return True
    return False


def is_in_a_loop(guard: Guard):
    history = {"<": [], "^": [], ">": [], "v": []}
    # print_map(guard.map)
    while guard.state is not State.OUT:
        if check_history(history, guard.direction, guard.position):
            print("loop", guard)
            return True
        else:
            history[guard.direction].append(guard.position)
        guard.move_forward()
    return False


guard_map_path = sys.argv[1]
with open(guard_map_path) as file:
    lines = file.read().splitlines()
    guard_map = lines
# guard = Guard(guard_map)
# print_map(guard.map)
# obstacles = guard.find_obstacles()
# length = len(obstacles)
# print(length)
guard2 = Guard(guard_map.copy())
count = 0
for j, row in enumerate(range(len(guard_map))):
    for i, col in enumerate(range(len(guard_map[0]))):
        # guard2 = Guard(guard_map.copy())
        guard2.map = guard_map.copy()
        guard2.state = State.FREE
        (guard2.direction, guard2.position) = guard2.find_initial_position(guard2.map)

        if guard2.add_obstacle_forward((row, col)):
            # print_map(guard2.map)
            # if i == 60 and j == 64:
            if is_in_a_loop(guard2) is True:
                count += 1
            # if i == 60 and j == 64:
            #     print_map(guard2.map)
            #     print("==================================")
            #     if is_in_a_loop(guard2):
            #         print("loop")
            #         count += 1
            #         continue
            #     exit()
print(count)
