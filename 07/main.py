from typing import List
import sys

sys.path.append("../common")
import utils

positions: List[int] = []


def get_input() -> List[int]:
  content = utils.read_input_file()
  return [int(p) for p in content.split(',')]


def calculate_fuel() -> int:
  positions = get_input()

  # get median
  positions.sort()
  median = positions[int(len(positions) / 2)]

  # sum the abolute differences between the blastpoint each crab
  return sum([abs(p - median) for p in positions])


def calculate_crab_fuel() -> int:
  positions = get_input()
  m = int(sum(positions) / len(positions))

  absoluteFuel = 0
  for position in positions:
    diff = abs(position - m)
    diff = int(diff * (diff + 1) / 2)
    absoluteFuel += diff

  return absoluteFuel


def main():
  utils.display_header_for_day(7)

  # # Star 1)
  print(f'Result Star 1: {calculate_fuel()}')

  # # Star 2
  print(f'Result Star 2: {calculate_crab_fuel()}')


main()
