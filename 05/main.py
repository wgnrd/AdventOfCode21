import sys
from typing import List

sys.path.append("../common")
import utils

field: List[int] = []


def get_report():
  content = utils.read_input_file()
  content = content.splitlines()

  for line in content:
    field.append([l.strip() for l in line.split('->')])

  print(field)


def main():
  utils.display_header_for_day(3)
  reportList = get_report()

  # # Star 1
  # print(f'Result Star 1: {calculate_power_consumption(reportList)}')

  # # Star 2
  # print(f'Result Star 2: {calculate_life_support_rating(reportList)}')


main()
