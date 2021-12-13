import sys
from typing import List

sys.path.append("../common")
import utils


def get_report() -> List[int]:
  content = utils.read_input_file()
  return [int(age) for age in content.split(',')]


def calculate_fish(days: int) -> int:
  fishes = get_report()

  # fishes = [f - 1 if f > 0 else 6 for f in fishes]
  for day in range(days):
    for i, fish in enumerate(fishes):
      new_age = fish - 1
      if new_age < 0:
        new_age = 6
        fishes.append(9)
      fishes[i] = new_age
    print(day)

  return len(fishes)


def main():
  utils.display_header_for_day(3)
  get_report()

  # # Star 1
  print(f'Result Star 1: {calculate_fish(80)}')

  # # Star 2


main()
