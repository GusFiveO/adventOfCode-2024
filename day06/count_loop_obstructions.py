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

    def mark_visited_position(self, position):
        row = list(self.map[position[0]])
        if row[position[1]] in directions.keys():
            return
        if self.state == State.BLOCKED:
            row[position[1]] = "+"
        elif self.direction == ">" or self.direction == "<":
            if row[position[1]] == "|":
                row[position[1]] = "+"
            else:
                row[position[1]] = "-"
        else:
            if row[position[1]] == "-":
                row[position[1]] = "+"
            else:
                row[position[1]] = "|"
        self.map[position[0]] = "".join(row)

    def move_forward(self):
        # print(self.position)
        (y_step, x_step) = directions[self.direction]
        initial_position = self.position
        new_position = (self.position[0] + y_step, self.position[1] + x_step)
        if self.is_out(new_position):
            self.mark_visited_position(initial_position)
            self.state = State.OUT
            return
        elif self.is_blocked(new_position):
            self.state = State.BLOCKED
            self.mark_visited_position(initial_position)
            self.turn_right()
            self.move_forward()
            return
        else:
            self.mark_visited_position(initial_position)
            self.state = State.FREE
        self.position = new_position

    def patrol(self):
        while self.state is not State.OUT:
            # while self.state is State.FREE:
            self.move_forward()

    def check_history(self, history, direction, position):
        if position in history[direction]:
            # print(position, history[direction], direction)
            return True
        return False

    def add_obstacle_forward(self):
        tmp_map = copy.deepcopy(self.map)
        position = (
            self.position[0] + directions[self.direction][0],
            self.position[1] + directions[self.direction][1],
        )
        row = list(tmp_map[position[0]])
        row[position[1]] = "#"
        tmp_map[position[0]] = "".join(row)
        return tmp_map

    def is_in_a_loop(self, map):
        history = {"<": [], "^": [], ">": [], "v": []}
        initial_map = copy.deepcopy(self.map)
        (initial_postion, initial_direction) = self.position, self.direction
        self.map = map
        while self.state is not State.OUT:
            if self.check_history(history, self.direction, self.position) is True:
                print("LOOP")
                self.state = State.FREE
                self.map = initial_map
                self.position = initial_postion
                self.direction = initial_direction
                return True
            else:
                history[self.direction].append(self.position)
            self.move_forward()
        self.state = State.FREE
        self.map = initial_map
        self.position = initial_postion
        self.direction = initial_direction
        return False

    def find_obstacles(self, count):
        (self.direction, self.position) = self.find_initial_position(self.map)
        # print(self.direction, self.position)
        self.state = State.FREE
        obstacle = []
        try:

            while self.state is not State.OUT:
                tmp_map = self.add_obstacle_forward()
                if self.is_in_a_loop(tmp_map):
                    position = (
                        self.position[0] + directions[self.direction][0],
                        self.position[1] + directions[self.direction][1],
                    )
                    obstacle.append(position)
                # for row in tmp_map:
                #     print(row)
                self.move_forward()
                # self.print_map()
        except Exception:
            pass
        return obstacle

    def print_map(self):
        for row in self.map:
            print(row)


guard_map_path = sys.argv[1]
with open(guard_map_path) as file:
    lines = file.read().splitlines()
    guard_map = lines
guard = Guard(guard_map)
visited_position = guard.patrol()
guard.print_map()
obstacles = guard.find_obstacles(0)
print(obstacles)
obstacles = list(dict.fromkeys(obstacles))
length = len(obstacles)
print(length)
print(f"The guard visited {visited_position} positions !")
