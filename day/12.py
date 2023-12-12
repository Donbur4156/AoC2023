from typing import List
from .util import *
import re
from itertools import combinations, repeat
from functools import cache

re_question = re.compile('\?')
re_hashtag = re.compile('#')

@cache
def check_combination(springs: tuple[str], groups: tuple[int]):
    return tuple(map(len, springs)) == groups

def calc_springs(springs: str, groups: str):
    groups = tuple(map(int, groups.split(",")))
    springs_amount = sum(groups)
    q_indices = re_question.finditer(springs)
    h_amount = len(list(re_hashtag.finditer(springs)))
    test_cases = combinations([i.span()[0] for i in q_indices], springs_amount-h_amount)
    counter = 0
    for tc in test_cases:
        s = list(springs)
        for c in tc:
            s[c] = "#"
        s = tuple("".join(s).replace("?", " ").replace(".", " ").split())
        if check_combination(s, groups):
            counter += 1
    return counter

def unfold(d: str):
    springs, groups = d.split()
    return (
        "?".join(repeat(springs, 5)),
        ",".join(repeat(groups, 5))
    )

def execute(data: List[str]):
    print_result(1, sum([calc_springs(*d.split()) for d in data]))
    print_result(2, sum([calc_springs(*unfold(d)) for d in data]))
