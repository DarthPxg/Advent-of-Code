lines = [int(line.strip().replace("L", "-").replace("R", "")) for line in open("input.txt")]

dialNumber = 50
zeroCount = 0

for line in lines:
  if line < 0:
    div, mod = divmod(line, -100)
    zeroCount += div

    if dialNumber != 0 and dialNumber + mod <= 0:
      zeroCount += 1
  else:
    div, mod = divmod(line, 100)
    zeroCount += div
    if dialNumber + mod >= 100:
      zeroCount += 1

  dialNumber = (dialNumber + line) % 100

print(f"----- {zeroCount} -----")