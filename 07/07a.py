from string import ascii_lowercase
inputfile = "C:\\Users\\jkearns\\Documents\\GitHub\\advent-of-code-2018\\07\\inputModified.txt"
with open(inputfile) as f:
    lines = f.readlines()

dependencies = {}

for c in ascii_lowercase:
    dependencies[c.upper()] = []

for line in lines:
    seg = line.split(', ')
    dependencies[seg[1][0]].append(seg[0][0])

output = ''

while len(dependencies) > 0:
    next = 'Z'
    for key in dependencies:
        if len(dependencies[key]) == 0 and key < next:
            next = key
    
    output += next
    del dependencies[next]
    for key in dependencies:
        if next in dependencies[key]:
            dependencies[key].remove(next)
    


print(output)