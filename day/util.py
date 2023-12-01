import pathlib
from typing import List

import httpx
import json


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
        'cookie': f'session={cfg["session_token"]}',
        'user-agent': f'{cfg["repo"]} by {cfg["email_adress"]}'
    }
    r = httpx.get(f'https://adventofcode.com/2023/day/{int(day)}/input', headers=headers)
    text = r.text.splitlines()
    with open(path.absolute(), 'w') as _f:
        _f.writelines('\n'.join(text))
    return text
