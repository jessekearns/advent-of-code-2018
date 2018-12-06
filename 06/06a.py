import operator
inputfile = "C:\\Users\\jkearns\\Documents\\GitHub\\advent-of-code-2018\\06\\input.txt"
with open(inputfile) as f:
    lines = f.readlines()

coords = {}
maxX = 0
maxY = 0

minX = 999
minY = 999
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

for x in range(minX - 1, maxX + 1):
    for y in range(minY - 1, maxY + 1):
        bDist = 99999
        bCoord = (0, 0)
        tied = False
        for c in coords:
            xDif = abs(x - c[0])
            yDif = abs(y - c[1])
            dist = yDif + xDif
            if (bDist > dist):
                bDist = dist
                bCoord = c
                tied = False
            elif (bDist == dist):
                bDist = dist
                bCoord = c
                tied = True
        if (x < minX or x > maxX or y < minY or y > maxY):
            if (not tied):
                coords[bCoord] -= 9999
        elif (not tied):
            coords[bCoord] += 1

bestC = (0,0)
bestD = 0

for c in coords:
    if (coords[c] > bestD):
        bestD = coords[c]
        bestC = c

print (bestC)
print (bestD)