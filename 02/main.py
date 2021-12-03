import sys
from enum import Enum

sys.path.append("../common")
import utils


class Direction(Enum):
  forward = 1
  up = 2
  down = 3


class Position:
  dx = 0
  dy = 0
  aim = 0


def get_instructions():
  content = utils.read_input_file()
  return content.splitlines()


def move(direction: Direction, distance: int, p: Position):
  if direction == Direction.down:
    p.dy += distance
  elif direction == Direction.up:
    p.dy = max(p.dy - distance, 0)
  elif direction == Direction.forward:
    p.dx += distance


def move_aim(direction: Direction, distance: int, p: Position):
  if direction == Direction.down:
    p.aim += distance
  elif direction == Direction.up:
    p.aim = max(p.aim - distance, 0)
  elif direction == Direction.forward:
    p.dx += distance
    p.dy += p.aim * distance


def handle_instruction(instruction: str, postition: Position):
  inst_pair = instruction.split()
  move(Direction[inst_pair[0]], int(inst_pair[1]), postition)


def handle_aim_instructions(instruction: str, position: Position):
  inst_pair = instruction.split()
  move_aim(Direction[inst_pair[0]], int(inst_pair[1]), position)


def calculate_position(instructions: str) -> int:
  position = Position()
  list(
      map(lambda instruction: handle_instruction(instruction, position),
          instructions))
  return position.dx * position.dy


def calculate_aim(instructions: str) -> int:
  position = Position()
  list(
      map(lambda instruction: handle_aim_instructions(instruction, position),
          instructions))
  return position.dx * position.dy


def main():
  utils.display_header_for_day(2)

  # Star 1
  instructions = get_instructions()
  print(f'result Star 1: {calculate_position(instructions)}')

  # Star 2
  instructions = get_instructions()
  print(f'result Star 1: {calculate_aim(instructions)}')


main()
