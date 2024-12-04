import re

pat = r"mul\((\d{1,3}),(\d{1,3})\)"

total = 0

with open("input3.txt") as f:
    for line in f:
        for match in re.finditer(pat, line):
            total += int(match.group(1)) * int(match.group(2))

print(total)