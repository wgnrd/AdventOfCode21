def display_header_for_day(day):
  print("--------------------")
  print(f"Day {day}")
  print("AdventOfCode 2021")
  print("Done by wgnrd")
  print("--------------------")


def read_input_file():
  file = open(".\input.txt", "r")
  content = file.read()
  file.close()
  return content