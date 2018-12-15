def ReadingOrder(unit):
    return (1000 * unit.y) + unit.x

def GridReadingOrder(pair):
    return (1000 * pair[1]) + pair[0]

def GetNeighbors(p):
    neighbors = []
    neighbors.append((p[0]+1, p[1]))
    neighbors.append((p[0]-1, p[1]))
    neighbors.append((p[0], p[1]+1))
    neighbors.append((p[0], p[1]-1))
    return neighbors

def GetDistanceOld(x1, x2, y1, y2, availableGrid, checkedTiles):
    if (x1 == x2 and y1 == y2):
        checkedTiles[(x1, y1)] = 0
        return 0, checkedTiles
    if (x1, y1) in checkedTiles:
        return checkedTiles[(x1, y1)], checkedTiles
    # Illegal tile
    if (x1 < 0 or y1 < 0 or x1 > len(availableGrid) or y1 > len(availableGrid[0]) or availableGrid[x1][y1] == False):
        checkedTiles[(x1, y1)] = 9999
        return 9999, checkedTiles
    
    # Check all 4 neighbors
    updatedDict = checkedTiles
    curr, updatedDict = GetDistance(x1-1, x2, y1, y2, availableGrid, updatedDict)
    best = curr

    curr, updatedDict = GetDistance(x1+1, x2, y1, y2, availableGrid, updatedDict)
    if (curr < best):
        best = curr

    curr, updatedDict = GetDistance(x1, x2, y1-1, y2, availableGrid, updatedDict)
    if (curr < best):
        best = curr

    curr, updatedDict = GetDistance(x1-1, x2, y1+1, y2, availableGrid, updatedDict)
    if (curr < best):
        best = curr

    return best, updatedDict

def GetDistance(x1, x2, y1, y2, availableGrid, checkedTiles):
    # Init state, all distances max, neighbors in queue
    distances = {}
    for i in range(-1, len(availableGrid)+1):
        for j in range(-1, len(availableGrid[0])+1):
            distances[(i, j)] = 9999
    queue = []
    queue.append((x2, y2))

    queueIndex = 0
    while queueIndex < len(queue):
        c = queue[queueIndex]
        queueIndex += 1
        # Illegal tile - carry on with this tile having the max distance
        if (c[0] < 0 or c[1] < 0 or c[0] >= len(availableGrid) or c[1] >= len(availableGrid[0])):
            continue
          
        if(c[0] == x2 and c[1] == y2):
            distances[c] = 0

        # Border or occupied space - carry on
        elif(availableGrid[c[0]][c[1]] == False):
            continue

        neighbors = GetNeighbors(c)
        for n in neighbors:
            if n not in queue and n in distances:
                queue.append(n)

        bestDistance = 9999
        for n in neighbors:
            if(n in distances and distances[n] < bestDistance):
                bestDistance = distances[n]
        distances[c] = bestDistance + 1

        # if (x1 == c[0] and y1 == c[1]):
        #     return distances[c]   

    # why are we still here? Just to suffer?
    return distances[(x1, y1)]
        


class Unit:
    def __init__(self, t, x, y):
        self.type = t # goblin or elf
        self.x = x
        self.y = y
        self.attack = 3
        self.hp = 200
    
    def IsAlive(self):
        return self.hp > 0

    def Attack(self, target):
        if self.type == target.type:
            print("That seems wrong!")
        target.hp = target.hp - self.attack

    def GetAdjacent(self, grid):
        adjacentSpots = []
        if grid[self.x+1][self.y]:
            adjacentSpots.append((self.x+1, self.y))
        if grid[self.x][self.y+1]:
            adjacentSpots.append((self.x, self.y+1))
        if grid[self.x-1][self.y]:
            adjacentSpots.append((self.x-1, self.y))
        if grid[self.x][self.y-1]:
            adjacentSpots.append((self.x, self.y-1))
        return adjacentSpots
    
    def IsAdjacent(self, target):
        if self.x == target.x:
            return self.y == target.y - 1 or self.y == target.y + 1
        if self.y == target.y:
            return self.x == target.x - 1 or self.x == target.x + 1
        return False

    def FindDestination(self, targets, allies, grid):
        bestDist = 99
        best = (self.x, self.y)

        availableGrid = grid
        for t in targets:
            if t.IsAlive:
                availableGrid[t.x][t.y] = False
        for a in allies:
            if a != self and a.IsAlive:
                availableGrid[a.x][a.y] = False

        for t in targets:
            adjacentTiles = t.GetAdjacent(availableGrid)
            adjacentTiles.sort(key=GridReadingOrder)
            for adjacency in adjacentTiles:
                d = GetDistance(self.x, adjacency[0], self.y, adjacency[1], availableGrid, {})
                if d < bestDist:
                    bestDist = d
                    best = adjacency

        # best is where we want to be - pick the best direction to get there
        if best[0] == self.x and best[1] == self.y:
            return best

        moves = self.GetAdjacent(availableGrid)
        bestMove = (self.x, self.y)
        # bestDist is distance from current
        for m in moves:
            d = GetDistance(m[0], best[0], m[1], best[1], availableGrid, {})
            if d < bestDist:
                bestDist = d
                bestMove = m

        return bestMove


    def TakeTurn(self, targets, allies, grid):
        if not self.IsAlive:
            return

        # Move
        print((self.x, self.y))
        destination = self.FindDestination(targets, allies, grid)
        if(self.x == destination[0] and self.y == destination[1]):
            print('Staying put')
            print()
        else:
            self.x = destination[0]
            self.y = destination[1]
            print((self.x, self.y))
            print()
        

        # Attack if available
        targets.sort(key=ReadingOrder)
        for t in targets:
            if t.IsAlive:
                if (self.IsAdjacent(t)):
                    self.Attack(t)
                    print("Attack!")
                    print((t.x, t.y))
                    print()
                    return

        return




inputfile = "C:\\Users\\jkearns\\Documents\\GitHub\\advent-of-code-2018\\15\\inputDemo.txt"
with open(inputfile) as f:
    lines = f.readlines()

mX = len(lines[0]) - 1 # Minus one for the \n
mY = len(lines)

grid = []
elves = []
goblins = []

for j in range(mY):
    grid.append([])

for i in range(mX):
    for j in range(mY):
        c = lines[j][i]
        if (c == '#'):
            grid[i].append(False)
        elif (c == 'E'):
            elves.append(Unit('e', i, j))
            grid[i].append(True)
        elif (c == 'G'):
            goblins.append(Unit('g', i, j))
            grid[i].append(True)
        elif (c == '.'):
            grid[i].append(True)
        else:
            print('Bad char')

step = 0
while True:
    allUnits = (goblins + elves)
    allUnits.sort(key=ReadingOrder)
    numLivingElves = 0
    numLivingGoblins = 0
    for u in allUnits:
        if (u.IsAlive):
            if u.type == 'e':
                u.TakeTurn(goblins, elves, grid)
                numLivingElves += 1
            elif u.type == 'g':
                u.TakeTurn(elves, goblins, grid)
                numLivingGoblins += 1
    if (numLivingElves == 0 or numLivingGoblins == 0):
        print('Done!')
        break
    else:
        step += 1