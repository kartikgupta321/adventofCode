import re
def calculate(data):
  """sums up all uncorrupted multiplications""" 
  result = 0

  pattern = r"mul\((\d+),(\d+)\)"

  matches = re.findall(pattern, data)
  for a, b in matches:
    result += int(a) * int(b)

  return result



with open('day3.txt', 'r') as file:
  result = 0
  data = file.read()
  print(calculate(data))

  

# print(result)