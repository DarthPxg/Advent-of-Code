banks = []
with open("../input.txt") as f:
  banks = [line.strip() for line in f.readlines()]

total = 0

for bank in banks:
  removals = len(bank) - 12
  stack = []

  for digit in bank:
      while stack and removals > 0 and stack[-1] < digit:
          stack.pop()
          removals -= 1
      stack.append(digit)

  while removals > 0:
      stack.pop()
      removals -= 1

  result = ''.join(stack)
  total += int(result)

print(total)