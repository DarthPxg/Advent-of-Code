ids = ""
with open("../input.txt") as f:
  ids = f.readline().strip().split(",")

invalidIds = []

for id_range in ids:
  bounds = id_range.split("-")
  for id in range(int(bounds[0]), int(bounds[1])+1):
    id = str(id)
    l = len(id)

    pattern = ""
    for i in range(len(id)//2):
      pattern += id[i]
      if len(id) % len(pattern) == 0:
        if pattern * (len(id) // len(pattern)) == id:
          invalidIds.append(int(id))
          break

print(sum(invalidIds))