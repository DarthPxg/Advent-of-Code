lines = [int(line.strip().replace("L", "-").replace("R", "")) for line in open("../input.txt")]

dialNumber = 50
zeroCount = 0

for line in lines:
  dialNumber = (dialNumber + line) % 100
  if dialNumber == 0:
    zeroCount += 1

print(f"----- {zeroCount} -----")