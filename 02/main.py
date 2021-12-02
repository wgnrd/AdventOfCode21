import sys
from enum import Enum

sys.path.append("../common")
import utils


class Direction(Enum):
  forward = 1
  up = 2
  down = 3


dx = 0
dy = 0


def get_instructions():
  content = utils.read_input_file()
  return content.splitlines()


def move(direction: Direction, distance: int):
  global dy, dx

  if direction == Direction.down:
    dy += distance
  elif direction == Direction.up:
    dy = max(dy - distance, 0)
  elif direction == Direction.forward:
    dx += distance


def handle_instruction(instruction):
  inst_pair = instruction.split()
  move(Direction[inst_pair[0]], int(inst_pair[1]))


def calculate_position(instructions) -> int:
  list(map(handle_instruction, instructions))
  return dx * dy


def main():
  utils.display_header_for_day(2)

  # Star 1
  instructions = get_instructions()
  print(f'result Star 1: {calculate_position(instructions)}')


main()
