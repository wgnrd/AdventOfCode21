from typing import List
import sys

sys.path.append("../common")
import utils


def get_input() -> List[List[int]]:
  content = utils.read_input_file()
  return [list(map(int, list(line))) for line in content.splitlines()]


def get_neighbours(x, y, heightmap):
  if (x, y) == (0, 0):
    return [heightmap[x + 1][y], heightmap[x][y + 1]]
  elif (x, y) == (len(heightmap) - 1, len(heightmap[0]) - 1):
    return [heightmap[x - 1][y], heightmap[x - 1][y - 1]]
  elif (x, y) == (0, len(heightmap[0]) - 1):
    return [heightmap[x][y - 1], heightmap[x + 1][y]]
  elif y == len(heightmap[0]) - 1:
    return [heightmap[x - 1][y], heightmap[x][y - 1], heightmap[x + 1][y]]
  elif (x, y) == (len(heightmap) - 1, 0):
    return [heightmap[x - 1][y], heightmap[x][y + 1]]
  elif y == 0:
    return [heightmap[x - 1][y], heightmap[x + 1][y], heightmap[x][y + 1]]
  elif x == 0:
    return [heightmap[x][y - 1], heightmap[x + 1][y], heightmap[x][y + 1]]
  elif x == len(heightmap) - 1:
    return [heightmap[x - 1][y], heightmap[x][y - 1], heightmap[x][y + 1]]

  return [
      heightmap[x - 1][y], heightmap[x][y - 1], heightmap[x + 1][y],
      heightmap[x][y + 1]
  ]


def sum_of_low_points() -> int:
  heightmap = get_input()
  sum = 0
  for i in range(0, len(heightmap)):
    for j in range(0, len(heightmap[0])):
      h = heightmap[i][j]
      neighbours = get_neighbours(i, j, heightmap)
      if min(neighbours) > h:
        sum += h + 1
  return sum


def main():
  utils.display_header_for_day(9)

  # Star 1)
  print(f'Result Star 1: {sum_of_low_points()}')


main()