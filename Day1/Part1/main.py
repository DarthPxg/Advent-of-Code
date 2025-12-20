with open("../input.txt") as f:
  lines = [int(line.strip().replace("L", "-").replace("R", "")) for line in f]

dialNumber = 50
zeroCount = 0

for line in lines:
  dialNumber = (dialNumber + line) % 100
  if dialNumber == 0:
    zeroCount += 1

print(f"----- {zeroCount} -----")