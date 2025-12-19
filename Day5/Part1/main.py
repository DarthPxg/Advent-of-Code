with open("../input.txt") as f:
    content = f.read()

parts = content.split('\n\n')
ranges = [line for line in parts[0].split('\n')]
numbers = [line for line in parts[1].split('\n')]

freshIds = 0

for n in numbers:
  for r in ranges:
    bounds = [int(line) for line in r.split("-")]
    if bounds[0] <= int(n) <= bounds[1]:
       freshIds += 1
       break

print(freshIds)