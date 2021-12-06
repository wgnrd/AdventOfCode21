import sys
from typing import List

sys.path.append("../common")
import utils


class BingoInput:
  drawnNumbers: List[int] = []
  boards: List[int] = []
  markings: List[bool] = []

  def parse_input(self):
    content = utils.read_input_file()
    tmpSplit = content.split('\n\n')
    self.drawnNumbers = tmpSplit[0].split(',')

    del tmpSplit[0]

    for board in tmpSplit:
      tmpBoard: List[int] = []
      self.markings.append([[False] * 5] * 5)
      for line in board.split('\n'):
        bar = list(filter(None, line.split(' ')))
        tmpBoard.append(bar)

      self.boards.append(tmpBoard)

  def is_winning_board(self, markings: List[int]) -> bool:
    for i in range(len(markings)):
      if len(markings[i]) == len([t for t in markings[i] if t == True]):
        return True

    for i in range(len(markings[i])):
      col = []
      for j in range(len(markings)):
        col.append(markings[i][j])
      if len(col) == len([t for t in col if t == True]):
        return True

    return False

  def calculate_score(self, board: List[int], markings: List[int]) -> int:
    score = 0
    for i in range(len(board)):
      for j in range(len(board[i])):
        if not markings[i][j]:
          score += board[i][j]

    return score

  # performs the board markings for a drawn number
  def draw(self, drawnNumber) -> int:
    for idx, board in enumerate(self.boards):
      for i in range(len(board)):
        for j in range(len(board[i])):
          if board[i][j] == drawnNumber:
            # ERROR: markings affect whole column instead of cell
            print(idx, i, j, drawnNumber)
            self.markings[idx][i][j] = True
            print(self.markings[idx][i])
            print(self.markings[idx])

      if self.is_winning_board(self.markings[idx]):
        return self.calculate_score(self.boards[idx], self.markings[idx])

  # finds first winner and returns the score
  def find_first_winner(self) -> int:
    for drawnNumber in self.drawnNumbers:
      score = self.draw(drawnNumber)
      if score != None:
        return score


def main():
  utils.display_header_for_day(4)

  bi = BingoInput()
  bi.parse_input()
  # Star 1
  print(f'Result Star 1: {bi.find_first_winner()}')

  # Star 2
  # print(f'Result Star 2: {}')


main()
