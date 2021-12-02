import sys

sys.path.append("../common")
import utils


def get_depths():
  content = utils.read_input_file()
  contentList = content.splitlines()
  return list(map(int, contentList))


def count_increase(depthList):
  return len([(i, j)
              for i, j in enumerate(depthList)
              if (i > 0) and (depthList[i] > depthList[i - 1])])


def split_windows(depthList):
  return [(depthList[i] + depthList[i + 1] + depthList[i + 2])
          for i, j in enumerate(depthList)
          if (i + 2) < len(depthList)]


def main():
  utils.display_header_for_day(1)
  # Star 1
  depthList = get_depths()
  print(f'Result Star 1: {count_increase(depthList)}')

  # Star 2
  windowList = split_windows(depthList)
  print(f'Result Star 2: {count_increase(windowList)}')


main()
