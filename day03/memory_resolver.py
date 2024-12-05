import re

with open("./corrupted_memory.txt") as file:
    lines = file.read().splitlines()

ret = 0
for line in lines:
    matches = re.findall("mul\(\d+,\d+\)", line)
    for match in matches:
        numbers = re.findall("\d+", match)
        mul = int(numbers[0]) * int(numbers[1])
        ret += mul
print(ret)
