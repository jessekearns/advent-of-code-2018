def StringifyState(state):
    output = ''
    for p in state:
        if (p):
            output += '#'
        else:
            output += '.'
    return output

def UpdateState(state, rules):
    newState = []
    for i in range(len(state)):
        firstNeighbor = i - 2
        lastNeighbor = i + 2
        key = ''
        # Handle neighbors outside of out boundaries - always false
        if firstNeighbor == -2:
            key = '..' + StringifyState(state[0:lastNeighbor + 1])
        elif firstNeighbor == -1:
            key = '.' + StringifyState(state[0:lastNeighbor + 1])
        elif lastNeighbor == len(state):
            key = StringifyState(state[firstNeighbor:len(state)]) + '.'
        elif lastNeighbor == len(state) + 1:
            key = StringifyState(state[firstNeighbor:len(state)]) + '..'
        else:
            key = StringifyState(state[firstNeighbor:lastNeighbor + 1])
        
        newState.append(rules[key])
    return newState

def GetIndexSumForState(state, firstPotIndex):
    total = 0
    for i in range(len(state)):
        if(state[i]):
            total += (firstPotIndex + i)
    return total

statefile = "C:\\Users\\jkearns\\Documents\\GitHub\\advent-of-code-2018\\12\\state0.txt"
rulesfile = "C:\\Users\\jkearns\\Documents\\GitHub\\advent-of-code-2018\\12\\rules.txt"
with open(statefile) as f:
    stateLines = f.readlines()

with open(rulesfile) as f:
    rulesLines = f.readlines()

step = 0
firstPotIndex = -3

state = []
for c in stateLines[0]:
    state.append(c == '#')

rules = {}
for line in rulesLines:
    r = line.split(' => ')
    rules[r[0]] = (r[1] == '#' or r[1] == '#\n')

while step < 20:
    state = UpdateState(state, rules)
    step += 1

print(GetIndexSumForState(state, firstPotIndex))