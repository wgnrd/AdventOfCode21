import sys
from typing import List

sys.path.append("../common")
import utils

clouds: List[int] = []
field: List[List[int]] = []


def get_report():
  content = utils.read_input_file()
  content = content.splitlines()

  for line in content:
    clouds.append([l.strip() for l in line.split('->')])


def get_dim() -> int:
  m = 0
  for cloud in clouds:
    for point in cloud:
      for val in point.split(','):
        x = int(val)
        if x > m:
          m = x

  return m


def get_height() -> int:
  return int(max([point.split(',')[0] for cloud in clouds for point in cloud]))


def is_diagonal(cloud: List[int]) -> bool:
  endp = cloud[1].split(',')
  startp = cloud[0].split(',')
  return not (startp[0] == endp[0] or startp[1] == endp[1])


def add_cloud(cloud: List[int]):
  endp = [int(x) for x in cloud[1].split(',')]
  startp = [int(x) for x in cloud[0].split(',')]
  if endp[0] != startp[0]:
    for x in range(min(endp[0], startp[0]), max(endp[0], startp[0]) + 1):
      field[startp[1]][x] += 1
  elif endp[1] != startp[1]:
    for y in range(min(endp[1], startp[1]), max(endp[1], startp[1]) + 1):
      field[y][startp[0]] += 1


def print_field():
  print('\n'.join(
      [''.join(['{:3}'.format(item) for item in row]) for row in field]))


def set_field():
  dim = get_dim()
  for i in range(dim + 1):
    field.append([0] * (dim + 1))


def nondiagonal_dangers() -> int:
  set_field()

  for cloud in clouds:
    if (not is_diagonal(cloud)):
      add_cloud(cloud)

  sum = 0
  for x in range(len(field)):
    for y in range(len(field[x])):
      if field[x][y] >= 2:
        sum += 1

  return sum


def main():
  utils.display_header_for_day(5)
  get_report()

  # # Star 1
  print(f'Result Star 1: {nondiagonal_dangers()}')

  # # Star 2
  # print(f'Result Star 2: {calculate_life_support_rating(reportList)}')


main()
