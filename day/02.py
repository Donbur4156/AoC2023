from typing import List
from .util import *
#12 red cubes, 13 green cubes, and 14 blue cubes
game_ref = {
    "red": 12,
    "green": 13,
    "blue": 14
}

def calc_id_sum(data: List[str]):
    games = [parse_game(game) for game in data]
    filtered_games = list(filter(check_game, games))
    return sum([game["id"] for game in filtered_games])

def parse_game(game_line: str):
    game_line = game_line.removeprefix("Game ").rstrip("\n")
    index_colon = game_line.find(":")
    return {
        "id": int(game_line[0:index_colon]),
        "sets": game_line[index_colon+2:].split(sep="; ")
    }

def check_game(game: dict[str, str]):
    game_sets = game["sets"]
    for set in game_sets:
        for cube in set.split(","):
            cube = cube.rstrip().lstrip()
            amount, color = cube.split()
            if int(amount) > game_ref[color]:
                return False
    return True

def calc_few_game(game: dict[str, str]):
    game_sets = game["sets"]
    r = g = b = 0
    for set in game_sets:
        for cube in set.split(","):
            cube = cube.rstrip().lstrip()
            amount, color = cube.split()
            match color:
                case "red": r = max(r, int(amount))
                case "green": g = max(g, int(amount))
                case "blue": b = max(b, int(amount))
    return r * g * b

def calc_few_games(data: List[str]):
    games = [parse_game(game) for game in data]
    return sum([calc_few_game(game) for game in games])


def execute(data: List[str]):
    print_result(1, calc_id_sum(data))
    print_result(2, calc_few_games(data))
