from typing import List


def execute(data: List[str]):
    f1 = [''.join(filter(str.isdigit, d)) for d in data]
    f1 = [int(x[0] + x[-1]) for x in f1]
    print(f'part 1: {sum(f1)}')

    # account for number overlap
    repl_map = {
        'one': 'o1e',
        'two': 't2o',
        'three': 't3e',
        'four': 'f4r',
        'five': 'f5e',
        'six': 's6x',
        'seven': 's7n',
        'eight': 'e8t',
        'nine': 'n9e'
    }

    def repl(_x: str) -> str:
        for key, val in repl_map.items():
            _x = _x.replace(key, val)
        return _x

    f2 = [''.join(filter(str.isdigit, repl(d))) for d in data]
    f2 = [int(x[0] + x[-1]) for x in f2]
    print(f'part 2: {sum(f2)}')
