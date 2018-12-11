serial = 3613
mX = 300
mY = 300
mS = 300 # set to 3 for part a

# thanks SO
def get_digit(number, n):
    return number // 10**n % 10

def GetPower(x, y):
    r = x + 10
    total = r*((r * y) + serial)
    d = 0
    if (total >= 100):
        d = get_digit(total, 2)
    return d - 5

ppts = {}
best = 0
bestPoint = (mX, mY)
bestSize = 0

# Store each point's power
for x in range(mX, 0, -1):
    for y in range(mY, 0, -1):
        p = GetPower(x, y)
        ppts[(x, y)] = p

# Get power for the region
for s in range(mS + 1):
    for x in range(1, mX + 1):
        for y in range(1, mY + 1):
            tp = 0
            for i in range(s):
                for j in range(s):
                    if (x + i) < mX and (y + j) < mY:
                        tp += ppts[(x + i, y + j)]
            # Better off checking debugger after a short while for these vals - suspect the size is way below 300
            if (tp > best):
                best = tp
                bestPoint = (x, y)     
                bestSize = s 

print(best)
print(bestPoint)
print(bestSize)