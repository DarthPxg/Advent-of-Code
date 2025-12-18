f = open("input.txt")

lines = f.readlines()

dialNumber = 50
zeroCount = 0

for line in lines:
  if len(line) < 2:
    continue
  number = int(line[1:])

  if line[0] == "R":
    dialNumber += number
  else:
    dialNumber -= number

  dialNumber %= 100

  if dialNumber == 0:
    zeroCount += 1

print(f"-----{zeroCount}-----")