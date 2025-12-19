banks = []
with open("../input.txt") as f:
  banks = [line.strip() for line in f.readlines()]

total = 0

for bank in banks:
  firstNum = []
  secondNum = 0

  for i in range(len(bank)-1):
    if len(firstNum) == 0 or int(bank[i]) > firstNum[1]:
      firstNum.clear()
      firstNum.append(i)
      firstNum.append(int(bank[i]))

  for j in range(firstNum[0]+1, len(bank)):
    if int(bank[j]) > secondNum:
      secondNum = int(bank[j])

  finalNum = int(str(firstNum[1]) + str(secondNum))
  total += finalNum

print(total)