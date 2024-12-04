import operator

from itertools import pairwise, starmap, filterfalse

def my_diff(report: list[int]) -> list[int]:
    return list(starmap(operator.sub, pairwise(report)))



def check_inc(diffs):
    if not list(filterfalse(lambda x: -4<x<0, diffs)):
        return True
    return False

def check_dec(diffs):
    if not list(filterfalse(lambda x: 0<x<4, diffs)):
        return True
    return False     


def r(report):
    for i in range(len(report)):
        yield report[:i] + report[i+1:]


def checkp1(report):
    diffs = my_diff(report)
    if check_inc(diffs):
        return True
    elif check_dec(diffs):
        return True
    else:
        return False
    
num_safe = 0

with open("input2.txt") as f:
    for line in f:
        report = [int(x) for x in line.split()]
        if checkp1(report):
            num_safe += 1
        else:
            for report_variant in r(report):
                if checkp1(report_variant):
                    num_safe += 1
                    break



print(num_safe)