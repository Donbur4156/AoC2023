from typing import List
from itertools import pairwise
from .util import *

def allzeros(seq):
    return all(v==0 for v in seq)

def pairwise_difs(seq):
    return [s[1]-s[0] for s in pairwise(seq)]

def calc_next(sequence: List[int]):
    return 0 if allzeros(sequence) else sequence[-1] + calc_next(pairwise_difs(sequence))

def calc_prev(sequence: List[int]):
    return 0 if allzeros(sequence) else sequence[0] - calc_prev(pairwise_difs(sequence))

def execute(data: List[str]):
    data = [list(map(int, d.split())) for d in data]
    print_result(1, sum([calc_next(d) for d in data]))
    print_result(2, sum([calc_prev(d) for d in data]))
