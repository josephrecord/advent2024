from collections import Counter

left, right = [], []

with open("input1.txt") as f:
    for line in f:
        l, r = (int(x) for x in line.split())
        left.append(l)
        right.append(r)

total = 0
for pair in zip(sorted(left), sorted(right)):
    diff = abs(pair[0] - pair[1])
    total += diff


rc = Counter(right)
score = 0
for elem in left:
    score += rc[elem] * elem
