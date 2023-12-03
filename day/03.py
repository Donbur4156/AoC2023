from typing import List
import re
from .util import *

re_specials = re.compile('[@_!#$%^&*()<>?/\|}{~:=+-]')
re_digits = re.compile('[0-9][0-9][0-9]|[0-9][0-9]|[0-9]')

def check_for_special(data, row, pos_b, pos_e):
    rows_to_check = data[max(row-1,0):row+2]
    chars_to_check: List[str] = [row[max(pos_b-1,0):pos_e+1] for row in rows_to_check]
    for chars in chars_to_check:
        if re_specials.search(chars):
            return True
    return False

def check_for_engine(data, row, pos_b, pos_e):
    rows_to_check = data[max(row-1,0):row+2]
    chars_to_check: List[str] = [row[max(pos_b-1,0):pos_e+1] for row in rows_to_check]
    for r_, chars in enumerate(chars_to_check, max(row-1,0)):
        pos = chars.find("*")
        if pos >= 0:
            p = max(pos_b-1,0) + pos
            return r_, p
    return False

def find_digits(data: List[str]):
    numbers = []
    for e, row in enumerate(data):
        matches = re_digits.finditer(row)
        for m in matches:
            if check_for_special(data, e, *m.span()):
                numbers.append(int(m.group(0)))
    return sum(numbers)

def find_engines(data: List[str]):
    def add_adjacent(adjacent, part):
        if parts := adjacents.get(adjacent, None):
            parts.append(part)
        else:
            adjacents[adjacent] = [part]
            
    adjacents: dict[tuple, list[int]] = {}
    for e, row in enumerate(data):
        matches = re_digits.finditer(row)
        for m in matches:
            if adj_pos := check_for_engine(data, e, *m.span()):
                add_adjacent(adj_pos, int(m.group(0)))

    return sum([v[0]*v[1] for v in adjacents.values() if len(v) == 2])


def execute(data: List[str]):
    print_result(1, find_digits(data))
    print_result(2, find_engines(data))
