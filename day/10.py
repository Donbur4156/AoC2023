from typing import List
from .util import *

pipe_map: dict[str, tuple[str,str]] = {
    ".": ("", ""),
    "|": ("north", "south"),
    "-": ("east", "west"),
    "L": ("north", "east"),
    "J": ("north", "west"),
    "7": ("south", "west"),
    "F": ("south", "east"),
    "S": ("east", "west")
}

def calc_dir(direction):
    match direction:
        case "north": return ((-1, 0), "south")
        case "south": return ((1, 0), "north")
        case "west": return ((0, -1), "east")
        case "east": return ((0, 1), "west")


def execute(data: List[str]):
    def get_pipe(coord):
        return data[coord[0]][coord[1]]
    
    def get_next_dir(pipe, prev_dir):
        mapping = pipe_map[pipe]
        return mapping[1 - mapping.index(prev_dir)]

    for e, d in enumerate(data):
        if "S" in d:
            start = (e, list(d).index("S"))
    dir = "east"
    loop = [start]
    tile_coord = start
    while True:
        next_coord, prev_dir = calc_dir(dir)
        tile_coord = tuple(map(sum, zip(tile_coord, next_coord)))
        loop.append(tile_coord)
        pipe = get_pipe(tile_coord)
        if pipe == "S":
            break
        dir = get_next_dir(pipe, prev_dir)
    print_result(1, int(len(loop)/2))
    print_result(2, None)
