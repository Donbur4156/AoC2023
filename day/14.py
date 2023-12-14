from typing import List
from .util import *
import re
import time
import numpy

re_O = re.compile("O")

test_data = [
    "O....#....",
    "O.OO#....#",
    ".....##...",
    "OO.#O....O",
    ".O.....O#.",
    "O.#..O.#.#",
    "..O..#O..O",
    ".......O..",
    "#....###..",
    "#OO..#....",
]

def tilt_north(data_: List[str]):
    for e, row in enumerate(data_):
        matches = re_O.finditer("".join(row))
        for m in matches:
            ind = m.span()[0]
            data_[e][ind] = "."
            row_ind = e
            while True:
                if row_ind == 0 or data_[row_ind-1][ind] in ["#", "O"]:
                    break
                row_ind -= 1
            data_[row_ind][ind] = "O"
    return data_

def calc_load(data_: List[str]):
    load = 0
    data_.reverse()
    for ind, row in enumerate(data_, start=1):
        load += ind * row.count("O")
    return load


def execute(data: List[str]):
    data = test_data
    data = [list(d) for d in data]
    data_c = data.copy()
    cycles = 1000000000
    for i in range(cycles*4):
        data: numpy.ndarray = numpy.rot90(m=tilt_north(data),k=-1, axes=(0, 1))
        if i % 10000 == 0:
            print(i)
    data = data.tolist()

    print_result(1, calc_load(tilt_north(data_c)))
    print_result(2, calc_load(data))
