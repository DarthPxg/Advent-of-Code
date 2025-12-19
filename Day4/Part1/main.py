map = []
with open("../input.txt") as f:
  map = [list(line.strip()) for line in f.readlines()]

accessiblePapers = 0

for ri in range(len(map)): # ri = row index
  for cj in range(len(map[ri])): # cj = character index
    if map[ri][cj] == ".":
      continue

    paperCount = 0

    for i in range(-1, 2):
      for j in range(-1, 2):
        if i == 0 and j == 0:
          continue
        if 0 <= ri + i < len(map) and 0 <= cj + j < len(map[ri + i]):
          if map[ri + i][cj + j] == "@":
            paperCount += 1

    if paperCount < 4:
      accessiblePapers += 1

print(accessiblePapers)