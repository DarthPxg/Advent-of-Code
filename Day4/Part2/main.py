map = []
with open("../input.txt") as f:
  map = [list(line.strip()) for line in f.readlines()]

total = 0

def removeAccessiblePapers(accessiblePapers):
  for pos in accessiblePapers:
    map[pos[0]][pos[1]] = "."

def getAccessiblePapers():
  accessiblePapers = 0
  accessiblePaperPositions = []

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
        accessiblePaperPositions.append([ri, cj])

  removeAccessiblePapers(accessiblePaperPositions)
  return accessiblePapers

accessiblePapers = getAccessiblePapers()
while accessiblePapers >= 1:
  total += accessiblePapers
  accessiblePapers = getAccessiblePapers()

print(total)