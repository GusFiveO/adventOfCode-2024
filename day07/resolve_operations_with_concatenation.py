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

def resolve_left_to_right(target, numbers, operators):
    res = numbers[0]
    for i in range(len(operators)):
            if numbers[0] > target:
                return numbers
            if operators[i] == '*':
                numbers[i + 1] = numbers[i] * numbers[i + 1]
                return resolve_left_to_right(target, numbers[i + 1:], operators[i + 1:])
            elif operators[i] == '+':
                numbers[i + 1] = numbers[i] + numbers[i + 1]
                return resolve_left_to_right(target, numbers[i + 1:], operators[i + 1:])
            elif operators[i] == '||':
                numbers[i + 1] = int(f"{numbers[i]}{numbers[i + 1]}")
                return resolve_left_to_right(target, numbers[i + 1:], operators[i + 1:])
    return numbers

count = 0
for target, numbers in operations:
    repeat = len(numbers) - 1
    combinations = list(product(["+", "*", "||"], repeat=repeat))
    for operators in combinations:
        operators = list(operators)
        res = resolve_left_to_right(target, numbers.copy(), operators)
        if res[0] == target:
            count += res[0]
            break
print(count)