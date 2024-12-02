import operator

from itertools import pairwise, starmap, filterfalse

def my_diff(report: list[int]) -> list[int]:
    return list(starmap(operator.sub, pairwise(report)))


num_safe = 0

with open("input2.txt") as f:
    for line in f:
        diffs = my_diff([int(x) for x in line.split()])
        if not list(filterfalse(lambda x: 0<x<4, diffs)):
            num_safe += 1
        if not list(filterfalse(lambda x: -4<x<0, diffs)):
            num_safe += 1


print(num_safe)