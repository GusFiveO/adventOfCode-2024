import re

with open("./corrupted_memory.txt") as file:
    lines = file.read().splitlines()

ret = 0
do = True
for line in lines:
    matches = re.findall("mul\(\d+,\d+\)|do\(\)|don't\(\)", line)
    for match in matches:
        if match == "do()":
            do = True
            continue
        elif match == "don't()":
            do = False
            continue
        if do is True:
            numbers = re.findall("\d+", match)
            mul = int(numbers[0]) * int(numbers[1])
            ret += mul
print(ret)
