from enum import Enum
class Direction(Enum):
    UP = 0
    RIGHT = 1
    DOWN = 2
    LEFT = 3

class TurnDirection(Enum):
    STRAIGHT = 0
    RIGHT = 1
    BACKWARDS = 2
    LEFT = 3

class Cart:
    def __init__(self, x, y, direction):
        self.x = x
        self.y = y
        self.direction = direction
        self.TurnDirection = TurnDirection.LEFT
        self.Collided = False

    def Advance(self, trackChar):
        if (self.Collided):
            return

        if (trackChar == '+'):
            dir = (self.direction.value + self.TurnDirection.value) % 4
            self.direction = Direction(dir)            
            if (self.TurnDirection == TurnDirection.LEFT):
                self.TurnDirection = TurnDirection.STRAIGHT
            elif (self.TurnDirection == TurnDirection.STRAIGHT):
                self.TurnDirection = TurnDirection.RIGHT
            elif (self.TurnDirection == TurnDirection.RIGHT):
                self.TurnDirection = TurnDirection.LEFT
        
        if (trackChar == '/'):
            if(self.direction == Direction.RIGHT):
                self.direction = Direction.UP
            elif(self.direction == Direction.UP):
                self.direction = Direction.RIGHT
            elif(self.direction == Direction.DOWN):
                self.direction = Direction.LEFT
            elif(self.direction == Direction.LEFT):
                self.direction = Direction.DOWN

        if (trackChar == '\\'):
            if(self.direction == Direction.RIGHT):
                self.direction = Direction.DOWN
            elif(self.direction == Direction.DOWN):
                self.direction = Direction.RIGHT
            elif(self.direction == Direction.UP):
                self.direction = Direction.LEFT
            elif(self.direction == Direction.LEFT):
                self.direction = Direction.UP

        if (self.direction == Direction.LEFT):
            self.x -= 1
        if (self.direction == Direction.UP):
            self.y -= 1
        if (self.direction == Direction.RIGHT):
            self.x += 1
        if (self.direction == Direction.DOWN):
            self.y += 1

def CompareCarts(cart):
    return (cart.y * 1000) + cart.x

def CartsCollided(carts):
    for i in range(len(carts)):
        firstCart = carts[i]
        for j in range(i+1, len(carts)):
            secondCart = carts[j]
            if firstCart.x == secondCart.x and firstCart.y == secondCart.y and not firstCart.Collided and not secondCart.Collided:
                firstCart.Collided = True
                secondCart.Collided = True
                return (True, firstCart.x, firstCart.y)

    return (False, 0, 0)

def RemainingCarts(carts):
    returnVal = 0
    lastCart = (0,0)
    for i in range(len(carts)):
        if (not carts[i].Collided):
            returnVal += 1
            lastCart = (carts[i].x, carts[i].y)

    return (returnVal, lastCart[0], lastCart[1])

inputfile = "C:\\Users\\jkearns\\Documents\\GitHub\\advent-of-code-2018\\13\\input.txt"
with open(inputfile) as f:
    rows = f.readlines()

carts = []
for i in range(len(rows[0]) - 1):
    for j in range(len(rows)):
        if (rows[j][i] == 'v' or rows[j][i] == 'V'):
            carts.append(Cart(i, j, Direction.DOWN))
        if (rows[j][i] == '>'):
            carts.append(Cart(i, j, Direction.RIGHT))
        if (rows[j][i] == '^'):
            carts.append(Cart(i, j, Direction.UP))
        if (rows[j][i] == '<'):
            carts.append(Cart(i, j, Direction.LEFT))

lastCart = False
collisions = 0
steps = 0
while not lastCart:
    steps += 1
    carts.sort(key=CompareCarts)
    i = 0
    lastCartIndex = len(carts)
    while i < lastCartIndex:
        cart = carts[i]
        cart.Advance(rows[cart.y][cart.x])
        check = CartsCollided(carts)
        if (check[0]):
            collisions += 1
            message = str(collisions) + ': Collision found on step ' + str(steps) + '\n(' + str(check[1]) + ',' + str(check[2]) + ')\n'
            print(message)
        
        i += 1
    check2 = RemainingCarts(carts)
    if check2[0] <= 1:
        message = 'Last cart found on step ' + str(steps) + '\n(' + str(check2[1]) + ',' + str(check2[2]) + ')\n'
        print(message)
        lastCart = True
        break