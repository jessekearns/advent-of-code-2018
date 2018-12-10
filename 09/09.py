numPlayers = 465
lastMarble = 7194000

scores = {}
for i in range(numPlayers):
    scores[i] = 0

circle = [0]
currentIndex = 0
currentPlayer = 0

for curr in range(1, lastMarble+1):
    if(curr % 23 == 0 and curr != 0):
        scores[currentPlayer] += curr
        currentIndex -= 7
        currentIndex %= len(circle)
        scores[currentPlayer] += circle[currentIndex]
        circle.remove(circle[currentIndex])
    else:
        insertIndex = (currentIndex + 1) % (len(circle)) + 1
        circle.insert(insertIndex, curr)
        currentIndex = insertIndex

    # out = ''
    # for x in circle:
    #     out += str(x)
    #     out += ' '
    # print(out)
    # print(currentIndex)
    # print()

    currentPlayer += 1
    currentPlayer %= numPlayers

best = 0
for i in range(numPlayers):
    if (scores[i] > best):
        best = scores[i]

print(best)