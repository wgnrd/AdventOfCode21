def read_input_file():
  file = open(".\input.txt", "r")
  content = file.read()
  content_list = content.splitlines()
  file.close()
  return content_list


def count_increase(depth_list):
  count = 0
  for i, j in enumerate(depth_list):
    if (i > 0 and (depth_list[i] > depth_list[i - 1])):
      count += 1

  return count


def main():
  depth_list = read_input_file()
  print(count_increase(depth_list))


main()
