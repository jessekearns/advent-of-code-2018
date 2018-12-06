import operator
inputfile = "C:\\Users\\jkearns\\Documents\\GitHub\\advent-of-code-2018\\06\\input.txt"
with open(inputfile) as f:
    lines = f.readlines()

distanceMax = 10000
coords = {}
maxX = 0
maxY = 0
minX = 999
minY = 999
winners = 0

for line in lines:
    sp = line.split(', ')
    x = int(sp[0])
    y = int(sp[1])
    coords[(x, y)] = 0
    if x > maxX:
        maxX = x
    if x < minX:
        minX = x
    if y > maxY:
        maxY = y
    if y < minY:
        minY = y

for x in range(minX, maxX):
    for y in range(minY, maxY):
        totalDist = 0
        for c in coords:
            xDif = abs(x - c[0])
            yDif = abs(y - c[1])
            dist = yDif + xDif
            totalDist += dist
        if (totalDist < distanceMax):
            winners += 1

print (winners)