from string import ascii_lowercase

def updateAvailable(dependencies, next):
    # update available work

    for key in dependencies:
        if next in dependencies[key]:
            dependencies[key].remove(next)

def getNext(dependencies, inProgress, completed):
    # new work - find the next available
    next = chr(ord('Z') + 1)
    for key in dependencies:
        if key in inProgress or key in completed:
            continue
        if len(dependencies[key]) == 0 and key < next:
            next = key
    if (next > 'Z'):
        return ''
    return next

inputfile = "C:\\Users\\jkearns\\Documents\\GitHub\\advent-of-code-2018\\07\\inputModified.txt"
with open(inputfile) as f:
    lines = f.readlines()



dependencies = {}

for c in ascii_lowercase:
    dependencies[c.upper()] = []

for line in lines:
    seg = line.split(', ')
    dependencies[seg[1][0]].append(seg[0][0])

workers = 5
baseSeconds = 60

seconds = -1
workerSeconds = {}
for i in range(0, workers):
    workerSeconds[i] = 0

workerTasks = {}
for i in range(0, workers):
    workerTasks[i] = ''

completed = ''
inProgress = []

while len(completed) < 26:
    seconds += 1
    # decrement all counters
    for i in range(0, workers):
        workerSeconds[i] -= 1

    # Completed work - Update available tasks and workers
    for i in range(0, workers):
        if (workerSeconds[i] <= 0 and workerTasks[i] != ''):
            updateAvailable(dependencies, workerTasks[i])
            inProgress.remove(workerTasks[i])
            completed += workerTasks[i]
            workerTasks[i] = '' 

    # Assign out new work
    for i in range(0, workers):
        if (workerSeconds[i] <= 0):
            next = getNext(dependencies, inProgress, completed)
            if (next != ''):
                inProgress.append(next)
                workerTasks[i] = next
                workerSeconds[i] = ord(next) - ord('A') + 1 + baseSeconds

    output = ''
    if seconds < 10:
        output += '00' + str(seconds) + ' | '
    elif seconds < 100:
        output += '0' + str(seconds) + ' | '
    else:
        output += str(seconds) + ' | '

    for i in range(0, workers):
        if (workerTasks[i] == ''):
            output += '. | '
        else:
            output += workerTasks[i] + ' | '
    output += completed
    print (output)



print(seconds)

