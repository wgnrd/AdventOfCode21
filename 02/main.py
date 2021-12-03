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
aim = 0


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


def move_aim(direction: Direction, distance: int):
  global dy, dx, aim

  if direction == Direction.down:
    aim += distance
  elif direction == Direction.up:
    aim = max(aim - distance, 0)
  elif direction == Direction.forward:
    dx += distance
    dy += aim * distance


def handle_instruction(instruction):
  inst_pair = instruction.split()
  move(Direction[inst_pair[0]], int(inst_pair[1]))


def handle_aim_instructions(instruction):
  inst_pair = instruction.split()
  move_aim(Direction[inst_pair[0]], int(inst_pair[1]))


def calculate_position(instructions) -> int:
  reset_position()
  list(map(handle_instruction, instructions))
  return dx * dy


def calculate_aim(instructions) -> int:
  reset_position()
  list(map(handle_aim_instructions, instructions))
  return dx * dy


def reset_position():
  global dy, dx, aim
  dx = 0
  dy = 0
  aim = 0


def main():
  utils.display_header_for_day(2)

  # Star 1
  instructions = get_instructions()
  print(f'result Star 1: {calculate_position(instructions)}')

  # Star 2
  instructions = get_instructions()
  print(f'result Star 1: {calculate_aim(instructions)}')


main()
