class Recipe:
    def __init__(self, previous, next, parent1, parent2, value):
        self.prev = previous
        self.next = next
        self.p1 = parent1
        self.p2 = parent2
        self.score = value
    
    def InsertAfter(self, newRecipe):
        temp = self.next
        self.next = newRecipe
        newRecipe.prev = self
        newRecipe.next = temp

class Elf:
    def __init__(self, recipe):
        self.recipe = recipe

    def Advance(self):
        moves = 1 + self.recipe.score
        for i in range(moves):
            self.recipe = self.recipe.next

# Create new recipes and insert to the list
# Return the new tail and the number of items added
def Mix(r1, r2, tail):
    currentTail = tail
    sum = r1.score + r2.score
    newScores = []
    if (sum == 0):
        newScores = [0]
    while sum > 0:
        newScores.append(sum % 10)
        sum = int(sum / 10)
    newRecipeCount = len(newScores)
    while len(newScores) > 0:
        s = newScores.pop()
        newRecipe = Recipe(None, None, r1, r2, s)
        currentTail.InsertAfter(newRecipe)
        currentTail = newRecipe
    return (currentTail, newRecipeCount)

def GetLength(head, tail):
    curr = head
    count = 1
    while curr != tail:
        count += 1
        curr = curr.next
    return count

def CheckMatch(sequence, tail):
    digit = sequence % 10
    if tail.score == digit:
        if sequence < 10:
            return True
        else:
            remainder = int(sequence / 10)
            return CheckMatch(remainder, tail.prev)
    return False

input = 894501

head = Recipe(None, None, None, None, 3)
tail = Recipe(head, head, None, None, 7)
head.prev = tail
head.next = tail
e1 = Elf(head)
e2 = Elf(tail)
currentLength = 2
while currentLength < input + 10:
    newTail, newItems = Mix(e1.recipe, e2.recipe, tail)
    tail = newTail
    currentLength = currentLength + newItems
    e1.Advance()
    e2.Advance()

backItem = tail
outputString = ''
for i in range(10):
    outputString = str(backItem.score) + outputString
    backItem = backItem.prev  

print(outputString)