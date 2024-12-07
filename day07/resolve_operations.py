import sys 
from itertools import product

file_path = sys.argv[1]
operations = list()
with open(file_path) as file:
    lines = file.read().splitlines()
    for line in lines:
        target, numbers = line.split(":")
        target = int(target)
        numbers = list(map(int, numbers.split()))
        operations.append((target, numbers))

def resolve_left_to_right(numbers, operators):
    res = numbers[0]
    for i in range(len(operators)):
        if operators[i] == '*':
            res *= numbers[i + 1]
        elif operators[i] == '+':
            res += numbers[i + 1]
    return res

count = 0
for target, numbers in operations:
    repeat = len(numbers) - 1
    combinations = list(product(["+", "*"], repeat=repeat))
    for operators in combinations:
        res = resolve_left_to_right(numbers, operators)
        if res == target:
            count += res
            break
print(count)