ids = open("../input.txt").readline().strip().split(",")
invalidIds = []

for id_range in ids:
  bounds = id_range.split("-")
  for id in range(int(bounds[0]), int(bounds[1])+1):
    id = str(id)
    l = len(id)

    if l % 2 != 0:
      continue

    if id[:l//2] == id[l//2:]:
      invalidIds.append(int(id))

print(sum(invalidIds))