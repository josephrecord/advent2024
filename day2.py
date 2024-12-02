import operator

from itertools import pairwise, starmap, filterfalse

def my_diff(report: list[int]) -> list[int]:
    return starmap(operator.sub, pairwise(report))


num_safe = 0

with open("input2.txt") as f:
    for line in f:
        l = [int(x) for x in line.split()]
        diff = list(my_diff(l))
        print("list")
        print(l)
        print(list(my_diff(l)))

        if not list(filterfalse(lambda x: 0<x<4, diff)):
            print("decreasing")
            num_safe += 1

        if not list(filterfalse(lambda x: -4<x<0, diff)):
            print("increasing")
            num_safe += 1


print(num_safe)