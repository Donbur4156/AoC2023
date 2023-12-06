from typing import List
from .util import *
from math import prod


def execute(data: List[str]):
    def calc_ways(time, dist):
        return len([ht for ht in range(time) if prod([time-ht, ht]) > dist])
    times, distances = (d.split()[1:] for d in data)

    
    print_result(1, prod([calc_ways(int(l[0]), int(l[1])) for l in zip(times, distances)]))
    print_result(2, calc_ways(int("".join(times)), int("".join(distances))))
