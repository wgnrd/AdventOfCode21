import sys
from typing import List

sys.path.append("../common")
import utils


def get_report():
  content = utils.read_input_file()
  contentList = content.splitlines()
  return contentList


def find_major_bit(reportList: List[str], index: int) -> str:
  threshold = len(reportList) / 2
  ones = 0
  for line in reportList:
    if line[index] == '1':
      ones += 1

  return '2' if ones == threshold else '1' if ones > threshold else '0'


def generate_epsilon(gamma: str) -> str:
  epsilon = gamma.replace('1', '2')
  epsilon = epsilon.replace('0', '1')
  return epsilon.replace('2', '0')


def calculate_power_consumption(reportList: List[str]) -> int:
  gamma = ''.join([
      find_major_bit(reportList, index) for index in range(len(reportList[0]))
  ])
  return int(gamma, 2) * int(generate_epsilon(gamma), 2)


def oxygen_rating(reportList: List[str]) -> int:
  oxyList = reportList
  for i in range(len(reportList[0])):
    oxyList = [
        line for line in oxyList
        if line[i] == ('0' if find_major_bit(oxyList, i) == '0' else '1')
    ]
    if len(oxyList) == 1:
      break

  return int(oxyList[0], 2)


def co2_rating(reportList: List[str]) -> int:
  co2List = reportList
  for i in range(len(reportList[0])):
    co2List = [
        line for line in co2List
        if line[i] == ('1' if find_major_bit(co2List, i) == '0' else '0')
    ]
    if len(co2List) == 1:
      break

  return int(co2List[0], 2)


def calculate_life_support_rating(reportList: List[str]) -> int:
  return co2_rating(reportList) * oxygen_rating(reportList)


def main():
  utils.display_header_for_day(3)
  reportList = get_report()

  # Star 1
  print(f'Result Star 1: {calculate_power_consumption(reportList)}')

  # Star 2
  print(f'Result Star 2: {calculate_life_support_rating(reportList)}')


main()
