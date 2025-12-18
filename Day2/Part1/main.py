ids = open("../input.txt").readline().strip().split(",")
invalidIds = []

for id in ids:
  bounds = id.split("-")
  for n in range(int(bounds[0]), int(bounds[1])+1):
    n = str(n)
    l = len(n)

    if l % 2 != 0:
      continue

    if n[:l//2] == n[l//2:]:
      invalidIds.append(int(n))

print(sum(invalidIds))