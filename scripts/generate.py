# -*- coding: utf-8 -*-
# Script to generate the dict data file
import json


# format
buffer = """# -*- coding: utf-8 -*-


class HolidayDataset(object):
    \"\""Dataset as dict.""\"

    # holidays jp dataset
    HOLIDAYS = """

# read the dataset
holiday_dict = {}
with open('dataset/holidays_detailed.yml') as file:
  lines = file.readlines()
  for i in range(0, len(lines)):
    line = lines[i]
    if 'date' in line:
      date_str = line.replace('date: ', '').strip()
      holiday_dict[date_str] = {}
    elif 'week:' in line:
      holiday_dict[date_str]['week'] = line.replace('week: ', '').strip()
    elif 'week_en:' in line:
      holiday_dict[date_str]['week_en'] = line.replace('week_en: ', '').strip()
    elif 'name:' in line:
      holiday_dict[date_str]['name'] = line.replace('name: ', '').strip()
    elif 'name_en:' in line:
      holiday_dict[date_str]['name_en'] = line.replace('name_en: ', '').strip()

# send to the file
with open('holiday_jp/holidays.py', 'w', encoding='utf8') as file:
  file.write(buffer + json.dumps(holiday_dict, ensure_ascii=False, indent=4, sort_keys=True))
