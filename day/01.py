from typing import List

def part_one(data: List[str]):
    return sum([calc_two_digit_nr_p1(line) for line in data])

def calc_two_digit_nr_p1(line: str):
    line_list = list(line)
    first = None
    last = None
    for a in line_list:
        if a.isnumeric():
            first = a
            break
    line_list.reverse()
    for a in line_list:
        if a.isnumeric():
            last = a
            break
    return int(f"{first}{last}")

def part_two(data: List[str]):
    return sum([calc_line(line.strip()) for line in data])

def calc_line(line: str):
    line_list = list(line)
    first = None
    last = None
    for a in range(len(line_list)):
        if nr := check_str_for_nr(line_list[a::]):
            first = nr
            break

    for a in range(len(line_list)):
        if nr := check_str_for_nr(line_list[-a-1::]):
            last = nr
            break
    return int(f"{first}{last}")

def check_str_for_nr(text: str):
    if text[0].isnumeric():
        return text[0]
    text = "".join([str(item) for item in text])
    if text.startswith(tuple(numbers.keys())):
        for k, v in numbers.items():
            if text.startswith(k):
                return v
    

numbers = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9
}

def execute(data: List[str]):
    print(f'part 1: {part_one(data)}')
    print(f'part 2: {part_two(data)}')
