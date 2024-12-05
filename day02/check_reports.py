with open("./reports.csv") as file:
    lines = file.read().splitlines()

reports = [list(map(int, line.split())) for line in lines]

count = 0
for report in reports:
    direction = 0
    for idx, level in enumerate(report):
        if idx != 0:
            difference = report[idx - 1] - level
            if direction == 0:
                direction = difference
            elif difference * direction < 0:
                print(
                    report,
                    "=> [Not the same direction]:",
                    f"[{report[idx -1]}, {level}]",
                )
                break
            distance = abs(difference)
            if distance < 1 or distance > 3:
                print(
                    report,
                    f"=> [Bad distance: {distance}]:",
                    f"[{report[idx -1]}, {level}]",
                )
                break

            if idx == len(report) - 1:
                count += 1
print("Safe record total count:", count)
