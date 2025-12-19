with open("../input.txt") as f:
    content = f.read()

parts = content.split('\n\n')
ranges = [line for line in parts[0].split('\n')]

ranges.sort(key=lambda x: int(x.split("-")[0]))

def mergeRanges():
  i = 0

  while i < len(ranges) - 1:
    bounds = ranges[i].split("-")
    nextBounds = ranges[i+1].split("-")
    if int(nextBounds[0]) <= int(bounds[1]):
      if int(nextBounds[1]) > int(bounds[1]):
        ranges[i] = ranges[i].replace(f"-{bounds[1]}", f"-{nextBounds[1]}")
      ranges.pop(i+1)
    else:
      i += 1

  return True

def calculateAllPossibleIds():
  freshIds = 0
  for r in ranges:
    bounds = [int(line) for line in r.split("-")]
    freshIds += (bounds[1] - bounds[0]) + 1

  return freshIds

ok = mergeRanges()
freshIds = calculateAllPossibleIds()

print(freshIds)