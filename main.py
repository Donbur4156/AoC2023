import sys
import datetime
from importlib import import_module
from day.util import get_day_data


if len(sys.argv) == 1:
    target_day = str(datetime.datetime.today().day)
else:
    target_day = sys.argv[1]

target_day = target_day.zfill(2)
day_data = get_day_data(target_day)
day_module = import_module(f'day.{target_day}')
day_module.execute(day_data)


