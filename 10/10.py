class Point:
    def __init__(self, x, y, dX, dY):
        self.x = x
        self.y = y
        self.dX = dX
        self.dY = dY

    def GetPositionAtTime(self, time):
        currX = self.x + (time*self.dX)
        currY = self.y + (time*self.dY)
        return (currX, currY)

    def GetChar(self):
        return '#'

inputfile = "C:\\Users\\jkearns\\Documents\\GitHub\\advent-of-code-2018\\10\\inputModified.txt"
with open(inputfile) as f:
    lines = f.readlines()

# Create list of all points
points = []
for line in lines:
    seg = line.split(', ')
    p = Point(int(seg[0]), int(seg[1]), int(seg[2]), int(seg[3]))
    points.append(p)

step = 10343 # Start at 0 - slower but checks the whole space

minX = 999999
maxX = -999999
minY = 999999
maxY = -999999
bxd = 999999
byd = 999999
bestStep = step

improving = True
while improving:
    bminX = 999999
    bmaxX = -999999
    bminY = 999999
    bmaxY = -999999

    # Get bounds at time
    for p in points:
        c = p.GetPositionAtTime(step)
        if (c[0] < bminX):
            bminX = c[0]
        if (c[0] > bmaxX):
            bmaxX = c[0]
        if (c[1] < bminY):
            bminY = c[1]
        if (c[1] > bmaxY):
            bmaxY = c[1]

    xd = bmaxX - bminX
    yd = bmaxY - bminY
    td = xd + yd
    if (td < (bxd + byd)):
        minX = bminX
        maxX = bmaxX
        minY = bminY
        maxY = bmaxY
        bxd = xd
        byd = yd
        bestStep = step
        step += 1
    else:
        improving = False

grid = {}
# populate empty grid
for i in range(minX, maxX + 1):
    grid[i] = {}
    for j in range(minY, maxY + 1):
        grid[i][j] = '.'

# add points to grid
for p in points:
    c = p.GetPositionAtTime(bestStep)
    grid[c[0]][c[1]] = p.GetChar()

#print grid
for j in range(minY, maxY + 1):
    row = ''
    for i in range(minX, maxX + 1):
        row += grid[i][j]
    print(row)

print(bestStep)