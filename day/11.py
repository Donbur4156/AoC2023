from typing import List
from itertools import combinations
import re
from .util import *

re_hashtag = re.compile('#')

def change_rows(data: List[str]):
    return list(map("".join, (zip(*data))))

def find_galaxies(data: List[str]):
    galaxies = []
    for r, row in enumerate(data):
        matches = re_hashtag.finditer(row)
        for m in matches:
            galaxies.append((r,m.span()[0]))
    return galaxies


def execute(data: List[str]):    
    def calc_distance(coords: tuple[tuple[int,int]], factor = 2):
        def rng_fix(a,b):
            return range(min(a,b), max(a,b))
        (ar, ac), (br, bc) = coords
        exp_amount = len(list(filter(lambda x: x in rng_fix(ar,br), exp_rows)))
        exp_amount += len(list(filter(lambda x: x in rng_fix(ac,bc), exp_cols)))
        return abs(ar-br) + abs(ac-bc) + exp_amount * (factor-1)
    
    exp_rows = [e for e, v in enumerate(data) if not "#" in v]
    exp_cols = [e for e, v in enumerate(change_rows(data)) if not "#" in v]
    galaxies = list(combinations(find_galaxies(data), 2))
    print_result(1, sum([calc_distance(gs) for gs in galaxies]))
    print_result(2, sum([calc_distance(gs, 1_000_000) for gs in galaxies]))
