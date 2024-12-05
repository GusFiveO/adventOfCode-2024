with open("./reports.csv") as file:
    lines = file.read().splitlines()
reports = [list(map(int, line.split())) for line in lines]


def is_safe(report):
    direction = 0
    for idx, level in enumerate(report):
        if idx != 0:
            difference = report[idx - 1] - level
            if direction == 0:
                direction = difference
            elif difference * direction < 0:
                return False
            distance = abs(difference)
            if distance < 1 or distance > 3:
                return False

            if idx == len(report) - 1:
                return True


def is_safe_with_problem_dampener(report):
    if is_safe(report):
        return True
    for i in range(len(report)):
        tmp_report = report[:i] + report[i + 1 :]
        if is_safe(tmp_report):
            return True
    return False


count = 0
for report in reports:
    if is_safe_with_problem_dampener(report):
        count += 1

print("Safe record total count:", count)
