from typing import List
from .util import *

test_data = ["rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7"]

def calc_hash(step: str):
    value = 0
    for c in list(step):
        value = ((value + ord(c)) * 17) % 256
    return value

def execute(data: List[str]):
    # data = test_data
    steps = data[0].split(",")
    print_result(1, sum([calc_hash(s) for s in steps]))

    boxes = {nr: {} for nr in range(256)}
    for step in steps:
        if step.endswith("-"):
            label = step[:-1]
            box = boxes.get(calc_hash(label))
            box.pop(label, None)
        else:
            label, foc_len = step.split("=")
            box = boxes.get(calc_hash(label))
            box[label] = int(foc_len)

    power = 0
    for box_nr, box in boxes.items():
        for slot_nr, foc_len in enumerate(box.values(), 1):
            power += (box_nr+1) * slot_nr * foc_len
    print_result(2, power)
