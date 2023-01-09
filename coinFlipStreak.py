import random

numberOfStreaks = 0

for experimentNumber in range(10000):

    coinFlips = []
    for i in range(100):
        randonmNumber = random.randint(0, 1)
        if randonmNumber == 0:
            randomFlip = 'H'
        else:
            randomFlip = 'T'
        coinFlips.append(randomFlip)

    for x in range(len(coinFlips)-5):
        if coinFlips[x] == coinFlips[x + 1] and coinFlips[x] == coinFlips[x + 2] and coinFlips[x] == coinFlips[x + 3] and coinFlips[x] == coinFlips[x + 4] and coinFlips[x] == coinFlips[x + 5]:
            numberOfStreaks += 1

print(numberOfStreaks)