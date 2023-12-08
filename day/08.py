from typing import List
import math
from .util import *


def execute(data: List[str]):
    def lr_conv(lr):
        if lr == "L":
            return 0
        return 1
    
    def calc_steps(node):
        steps = 0
        while True:
            operator = dirs[steps % len(dirs)]
            node = nodes_dict[node][operator]
            steps += 1
            if node.endswith("Z"):
                return steps

    dirs = list(map(lr_conv, list(data[0])))
    nodes_dict = {d[:3]: (d[7:10], d[12:15]) for d in data[2:]}
    steps = 0
    node = "AAA"
    while True:
        operator = dirs[steps % len(dirs)]
        node = nodes_dict[node][operator]
        steps += 1
        if node == "ZZZ":
            break
    print_result(1, steps)

    nodes = list(filter(lambda x: x.endswith("A"), nodes_dict.keys()))
    print_result(2, math.lcm(*list(map(calc_steps, nodes))))
