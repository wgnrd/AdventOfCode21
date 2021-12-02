import sys

sys.path.append("../common")
import utils


def read_input_file():
  file = open(".\input.txt", "r")
  content = file.read()
  contentList = content.splitlines()
  file.close()
  return list(map(int, contentList))


def count_increase(depthList):
  count = 0
  for i, j in enumerate(depthList):
    if (i > 0 and (depthList[i] > depthList[i - 1])):
      count += 1

  return count


def split_windows(depthList):
  windowList = []

  for i, j in enumerate(depthList):
    if ((i + 2) < len(depthList)):
      windowList.append(depthList[i] + depthList[i + 1] + depthList[i + 2])

  return windowList


def main():
  utils.displayHeaderForDay(1)
  # Star 1
  depthList = read_input_file()
  print(f'Result Star 1: {count_increase(depthList)}')

  # Star 2
  windowList = split_windows(depthList)
  print(f'Result Star 2: {count_increase(windowList)}')


main()
