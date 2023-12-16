from typing import List
from .util import *
import sys
sys.setrecursionlimit(5000)
def energize_table(data: List[List[str]], start_coord, start_dir):
    def energize_next(coord: tuple[int, int], dir: str):
        def calc_next_coord():
            match dir:
                case "n": return (coord[0]-1, coord[1])
                case "e": return (coord[0], coord[1]+1)
                case "s": return (coord[0]+1, coord[1])
                case "w": return (coord[0], coord[1]-1)

        def check_coord():
            return (coord[0] in range(len(data[0])) and coord[1] in range(len(data)))

        if (coord, dir) in moving_table or not check_coord():
            return False
        moving_table.append((coord,dir))

        tile = data[coord[0]][coord[1]]

        match tile:
            case ".":
                dirs = [dir]
            case "|":
                if dir in ["n", "s"]:
                    dirs = [dir]
                else:
                    dirs = ["n", "s"]
            case "-":
                if dir in ["w", "e"]:
                    dirs = [dir]
                else:
                    dirs = ["e", "w"]
            case "/":
                match dir:
                    case "n": dirs = ["e"]
                    case "s": dirs = ["w"]
                    case "e": dirs = ["n"]
                    case "w": dirs = ["s"]
            case "\\":
                match dir:
                    case "n": dirs = ["w"]
                    case "s": dirs = ["e"]
                    case "e": dirs = ["s"]
                    case "w": dirs = ["n"]
        for dir in dirs:
            energize_next(calc_next_coord(), dir)
        
    
    moving_table = []
    energize_next(coord=start_coord, dir=start_dir)
    
    table = set(c[0] for c in moving_table)
    return len(table)

'''
for c in table:
    data[c[0]][c[1]] = "#"
return data
'''

def execute(data: List[str]):
    data = [list(d) for d in data]
    energize_map = [energize_table(data, (i, 0), "e") for i in range(len(data))]
    energize_map += [energize_table(data, (i, len(data)-1), "w") for i in range(len(data))]
    energize_map += [energize_table(data, (0, i), "s") for i in range(len(data))]
    energize_map += [energize_table(data, (len(data)-1, i), "n") for i in range(len(data))]
    print_result(1, energize_map[0])
    print_result(2, max(energize_map))
