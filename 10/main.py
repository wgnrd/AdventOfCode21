from typing import List
import sys

sys.path.append('../common')
import utils

openSymbol = ['{', '[', '(', '<']
closeSymbol = ['}', ']', ')', '>']


def get_lines() -> List[str]:
  content = utils.read_input_file()
  return content.splitlines()


def rec_check(c, i):
  # abbort
  if len(c) < i:
    return ('', 0)

  char = c[i]
  charIdx = i
  error = ''
  while i < len(c):
    nextChar = ''
    if char in openSymbol:
      # if its an open Symbol we need to go deeper in the recursion
      nextChar, currentIndex = rec_check(c, i + 1)
      # if we are at the beginning of a line
      if currentIndex == 0:
        if char == '{':
          nextChar += '}'
        elif char == '<':
          nextChar += '>'
        elif char == '(':
          nextChar += ')'
        elif char == '[':
          nextChar += ']'
        return (nextChar, 0)
    elif char in closeSymbol:
      # if its a closing symbol we can go back in the recursion
      return (char, i)
    if (nextChar == '.'):
      i = currentIndex
      continue
    # error checking
    if char == '{' and nextChar != '}':
      error = 'Expected } but found ' + nextChar
    elif char == '<' and nextChar != '>':
      error = f'Expected > but found {nextChar}'
    elif char == '(' and nextChar != ')':
      error = f'Expected ) but found {nextChar}'
    elif char == '[' and nextChar != ']':
      error = f'Expected ] but found {nextChar}'
    if error:
      raise Exception(error, nextChar)
    # if its open and closing right next to it
    if charIdx == 0 and i < len(c):
      return rec_check(c, i + 2)
    return ('.', i + 1)


def check_lines() -> int:
  lines = get_lines()
  sum = 0
  done = []
  errors = []
  for line in lines:
    try:
      l = rec_check(line, 0)
      done.append(line + " " + l[0])
    except Exception as error:
      if "Expected" in error.args[0]:
        errors.append(error.args[1])

  for error in errors:
    if error == ')':
      sum += 3
    elif error == ']':
      sum += 57
    elif error == '}':
      sum += 1197
    elif error == '>':
      sum += 25137

  return sum


def main():
  utils.display_header_for_day(10)

  # # Star 1)
  print(f'Result Star 1: {check_lines()}')

  # # Star 2
  # print(f'Result Star 2: {calculate_crab_fuel()}')


main()
