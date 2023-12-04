from typing import List
from .util import *

def parse_data(card_infos: str):
    return {
        "card_nr": int(card_infos[5:8]),
        "wins": set(card_infos[10:39].split()),
        "nums": set(card_infos[42:].split()),
        "instances": 1
    }

def calc_matches(d):
    return len(list(d["wins"] & d["nums"]))

def execute(data: List[str]):
    card_list = [parse_data(c) for c in data]
    combines = [calc_matches(d) for d in card_list]
    print_result(1, sum([2**(c-1) for c in filter(lambda num: num != 0, combines)]))

    for card in card_list:
        matches = calc_matches(card)
        card_nr = card["card_nr"]
        for c in card_list[card_nr:card_nr+matches]:
            c["instances"] += card["instances"]
    print_result(2, sum([c["instances"] for c in card_list]))
