import sys
import datetime
from importlib import import_module
from pathlib import Path
from time import perf_counter
from day.util import get_day_data
import shutil
from colorama import init as colorama_init, Fore


colorama_init(autoreset=True)
today = datetime.datetime.today()

if len(sys.argv) == 1:
    if today.year != 2023 or today.month != 12:
        print(f'{Fore.RED}Error: Can\'t run without specific day outside of competition time')
        exit(1)
    target_day = str(datetime.datetime.today().day)
else:
    target_day = sys.argv[1]

if target_day == "gen":
    target_day = str(today.day).zfill(2)
    if Path(f"day/{target_day}.py").exists():
        print(f'{Fore.RED}Error: Can\'t generate, current day already exists.')
        exit(1)
    shutil.copyfile('template/day.py', f'day/{target_day}.py')
    print(f'{Fore.GREEN}Generated template for day {target_day}.')
else:
    if int(target_day) > datetime.datetime.today().day:
        print(f'{Fore.RED}Error: Can\'t run future day')
        exit(1)
    target_day = target_day.zfill(2)
    day_data = get_day_data(target_day)
    day_module = import_module(f'day.{target_day}')
    start_time = perf_counter()
    day_module.execute(day_data)
    end_time = perf_counter() - start_time
    print(f'{Fore.LIGHTBLACK_EX}Perf: Took {end_time:.3f} seconds')
