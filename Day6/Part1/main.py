import math

with open("../input.txt") as f:
  numbers = [line.strip().split() for line in f.readlines()]

total = 0

operations = numbers[-1]
numbers.pop(-1)

for j in range(len(operations)):
  numsToAdd = []
  for i in range(len(numbers)):
    if 0 <= j < len(numbers[i]):
      numsToAdd.append(int(numbers[i][j]))

  if operations[j] == "*":
    total += math.prod(numsToAdd)
  else:
    total += sum(numsToAdd)

print(total)