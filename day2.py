import operator

from itertools import pairwise, starmap, filterfalse

def my_diff(report: list[int]) -> list[int]:
    return list(starmap(operator.sub, pairwise(report)))



def check(differences):
    increasing = None
    for elem in differences:
        if increasing is None:
            if elem < 0:
                increasing = True
            elif elem > 0:
                increasing = False
            else:
                pass
        



num_safe = 0

with open("input2.txt") as f:
    for line in f:
        diffs = my_diff([int(x) for x in line.split()])

        filtered = [x for x in diffs if -4 < x < 4]

        print(line)
        print(diffs)
        print(filtered)


        # decreasing_elems = list(filterfalse(lambda x: 0<x<4, diffs))
        # if len(decreasing_elems) == 0 or len(decreasing_elems) == 1:
        #     if not [x for x in decreasing_elems if x < 4]:
        #         num_safe += 1
        #         print(line)
        #         print(diffs)
        # increasing_elems = list(filterfalse(lambda x: -4<x<0, diffs))
        # if len(increasing_elems) == 0 or len(increasing_elems) == 1:
        #     if not [x for x in increasing_elems if x < -4]:
        #         num_safe += 1
        #         print(line)
        #         print(diffs)


print(num_safe)