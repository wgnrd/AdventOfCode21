import sys
from typing import List

sys.path.append("../common")
import utils


def get_report():
  content = utils.read_input_file()
  contentList = content.splitlines()
  return contentList


def find_major_bit(reportList: List[str], index: int) -> str:
  ones = 0
  for line in reportList:
    if line[index] == '1':
      ones += 1

  return '1' if ones > len(reportList) / 2 else '0'


def generate_epsilon(gamma: str) -> str:
  epsilon = gamma.replace('1', '2')
  epsilon = epsilon.replace('0', '1')
  return epsilon.replace('2', '0')


def handle_report(reportList: List[str]) -> int:
  gamma = ''.join([
      find_major_bit(reportList, index) for index in range(len(reportList[0]))
  ])
  return int(gamma, 2) * int(generate_epsilon(gamma), 2)


def main():
  utils.display_header_for_day(3)
  # Star 1
  reportList = get_report()
  print(f'Result Star 1: {handle_report(reportList)}')

  # Star 2


main()
