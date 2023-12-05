from typing import List
from .util import *

def create_mapping(data: List[str]):
    map_ = {}
    for d in data:
        d = [int(d) for d in d.split()]
        map_.update({
            range(d[1], d[1]+d[2]) : d[0]-d[1]
        })
    return map_

def calc_mapping(sources: List[int], mapping: dict[range, int]):
    def find_mapping(s: int):
        for k, v in mapping.items():
            if s in k:
                return s + v
        return s
    return [find_mapping(s_) for s_ in sources]


def execute(data: List[str]):
    def calc_seeds(seeds):
        soils = calc_mapping(seeds, create_mapping(data[3:40]))
        fert = calc_mapping(soils, create_mapping(data[42:52]))
        water = calc_mapping(fert, create_mapping(data[54:90]))
        lights = calc_mapping(water, create_mapping(data[92:138]))
        temps = calc_mapping(lights, create_mapping(data[140:168]))
        humis = calc_mapping(temps, create_mapping(data[170:210]))
        return calc_mapping(humis, create_mapping(data[212:254]))
    seeds_a = [int(s) for s in data[0].lstrip("seeds:").split()]
    #seeds_b = [range(a, a+b) for a, b in zip(seeds_a[0::2], seeds_a[1::2])]

    print_result(1, min(calc_seeds(seeds_a)))
    print_result(2, None)
