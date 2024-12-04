import re

pat = r"(mul)\((\d{1,3}),(\d{1,3})\)|(do\(\))|((don't)\(\))"

matches = []

total = 0

with open("input3.txt") as f:
    lines = f.readlines()

# lines = ["xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"]

for line in lines:
    for match in re.finditer(pat, line):
        matches.append(match)


do = True

for match in matches:
    if match.group(1) == "mul":
        if do:
            print(f"Adding product {match}")
            total += int(match.group(2)) * int(match.group(3))
        else:
            print(f"Not adding product {match}")
    elif match.group(4) == "do()":
        print(f"Do {match}")
        do = True
    elif match.group(5) == "don't()":
        print(f"Dont {match}")
        do = False
    else:
        pass
        
