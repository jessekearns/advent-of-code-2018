inputfile = "C:\\Users\\jkearns\\Documents\\GitHub\\advent-of-code-2018\\03\\input-modified.txt"
with open(inputfile) as f:
    lines = f.readlines()

xForId = {}
yForId = {}
widthForId = {}
heightForId = {}

numIds = 1311
gridWidth = 0
gridHeight = 0

for line in lines:
    ints = line.split(',')
    id = int(ints[0])
    xForId[id] =  int(ints[1])
    yForId[id] = int(ints[2])
    widthForId[id] = int(ints[3])
    heightForId[id] = int(ints[4])
    if (xForId[id] + widthForId[id] > gridWidth):
        gridWidth = xForId[id] + widthForId[id]
    if (yForId[id] + heightForId[id] > gridHeight):
        gridHeight = yForId[id] + heightForId[id]

# Initialize 2d array of zeros
grid = [ [0] * gridHeight for _ in range(gridWidth)]
    
for id in range(1, numIds + 1):
    x = xForId[id]
    y = yForId[id]
    w = widthForId[id]
    h = heightForId[id]
    for i in range(x, x+w):
        for j in range(y, y+h):
            grid[i][j] += 1

for id in range(1, numIds + 1):
    x = xForId[id]
    y = yForId[id]
    w = widthForId[id]
    h = heightForId[id]
    claimIsValid = True
    for i in range(x, x+w):
        for j in range(y, y+h):
            if (grid[i][j] > 1):
                    claimIsValid = False
    if (claimIsValid == True):
        print(id)
