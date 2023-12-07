from typing import List
from math import prod
from .util import *

test_data = [
    "32T3K 765",
    "T55J5 684",
    "KK677 28",
    "KTJJT 220",
    "QQQJA 483",
]


'''
types:
0: high card
1: one pair
2: two pair
3: three a kind
4: full house
5: four a kind
6: five a kind
'''
card_strengths = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
card_strengths_new = ['J', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'Q', 'K', 'A']

def comp_cards(a:str):
    a = a[0]
    def card_type():
        a_r = {}
        for a_ in list(a):
            if a_ in a_r.keys():
                a_r[a_] += 1
            else:
                a_r[a_] = 1
        a_v = list(a_r.values())
        if 5 in a_v:
            return 6
        if 4 in a_v:
            return 5
        if 3 in a_v:
            if 2 in a_v:
                return 4
            return 3
        return a_v.count(2)
    return int("".join([str(card_type()), *[str(card_strengths.index(v)).zfill(2) for v in list(a)]]))
        
def comp_cards_new(a:str):
    a = a[0]
    def card_type():
        a_r = {}
        for a_ in list(a):
            if a_ in a_r.keys():
                a_r[a_] += 1
            else:
                a_r[a_] = 1
        a_v = list(a_r.values())
        a_j = a_r.get('J', 0)
        if 5 in a_v:
            return 6
        if 4 in a_v:
            if a_j >= 1:
                return 6
            return 5
        if 3 in a_v:
            if a_j == 3:
                if 2 in a_v:
                    return 6
                return 5
            if a_j == 2:
                return 6
            if a_j == 1:
                return 5
            if 2 in a_v:
                return 4
            return 3
        if 2 in a_v:
            a_v_c = a_v.count(2)
            if a_v_c == 1:
                if a_j >= 1:
                    return 3
                return 1
            if a_v_c == 2:
                if a_j == 2:
                    return 5
                if a_j == 1:
                    return 4
                return 2
        if a_j == 1:
            return 1
        return 0
    return int("".join([str(card_type()), *[str(card_strengths_new.index(v)).zfill(2) for v in list(a)]]))


def execute(data: List[str]):
    # data = test_data
    hands = [tuple(d.split()) for d in data]
    hands.sort(key=comp_cards)
    print_result(1, sum([prod([r, int(b[1])]) for r, b in enumerate(hands, 1)]))
    hands.sort(key=comp_cards_new)
    print_result(2, sum([prod([r, int(b[1])]) for r, b in enumerate(hands, 1)]))
