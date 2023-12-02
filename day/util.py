import pathlib
from typing import List

import httpx
import json
from colorama import Fore, Style

__all__ = ['print_result', 'get_config', 'get_day_data']


def print_result(part: int, result):
    if result is None:
        print(f'Part {part}: {Fore.YELLOW}Unsolved')
    else:
        print(f'Part {part}: {Style.BRIGHT}{Fore.GREEN}{result}')


def get_config() -> dict:
    with open('config.json') as _f:
        return json.load(_f)


def get_day_data(day: str) -> List[str]:
    path = pathlib.Path(f'day_data/{day}.txt')

    if path.exists():
        with open(path.absolute()) as _f:
            return _f.readlines()

    cfg = get_config()

    headers = {
        'cookie': f'session={cfg["session_token"]}'
        #'user-agent': f'{cfg["repo"]} by {cfg["email_adress"]}'
    }
    r = httpx.get(f'https://adventofcode.com/2023/day/{int(day)}/input', headers=headers)
    text = r.text.splitlines()
    with open(path.absolute(), 'w') as _f:
        _f.writelines('\n'.join(text))
    return text
