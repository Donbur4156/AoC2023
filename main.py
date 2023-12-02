import sys
import datetime
from importlib import import_module
from day.util import get_day_data
import shutil


if len(sys.argv) == 1:
    today = datetime.datetime.today()
    if today.year != 2023 or today.month != 12:
        print('Error: can\'t run without specific day outside of competition time')
        exit(1)
    target_day = str(datetime.datetime.today().day)
else:
    target_day = sys.argv[1]

if int(target_day) > datetime.datetime.today().day:
    print('Error: Can\'t run future day')
    exit(1)

target_day = target_day.zfill(2)
day_data = get_day_data(target_day)
try:
    day_module = import_module(f'day.{target_day}')
except ModuleNotFoundError:
    shutil.copyfile('template/day.py', f'day/{target_day}.py')
else:
    day_module.execute(day_data)
