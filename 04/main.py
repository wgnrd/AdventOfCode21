import sys
from typing import List

sys.path.append("../common")
import utils


class BingoInput:
  drawnNumbers: List[int] = []
  boards: List[int] = []

  def parse_input(self):
    content = utils.read_input_file()
    foo = content.split('\n\n')
    self.drawnNumbers = foo[0].split(',')

    del foo[0]

    for board in foo:
      tmpBoard: List[int] = []
      for line in board.split('\n'):
        bar = list(filter(None, line.split(' ')))
        tmpBoard.extend(bar)

      self.boards.append(tmpBoard)


def main():
  utils.display_header_for_day(4)

  bi = BingoInput()
  bi.parse_input()
  print(bi.drawnNumbers)
  # Star 1
  print(f'Result Star 1: {0}')

  # Star 2
  # print(f'Result Star 2: {}')


main()
