from typing import List
import sys

sys.path.append("../common")
import utils

digits: List[str] = []
signals: List[str] = []


def get_digits() -> List[str]:
  content = utils.read_input_file()
  content = content.splitlines()
  content = [
      x[1].strip().split(' ') for x in (line.split('|') for line in content)
  ]
  return [item for sublist in content for item in sublist]


def number_of_unique_digits() -> int:
  digits = get_digits()
  sum = 0
  for digit in digits:
    if len(digit) == 2 or len(digit) == 3 or len(digit) == 4 or len(digit) == 7:
      sum += 1

  return sum


def main():
  utils.display_header_for_day(8)

  # # Star 1)
  print(f'Result Star 1: {number_of_unique_digits()}')

  # # Star 2
  # print(f'Result Star 2: {calculate_crab_fuel()}')


main()
