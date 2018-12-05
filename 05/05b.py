from string import ascii_lowercase
 
inputfile = "C:\\Users\\jkearns\\Documents\\GitHub\\advent-of-code-2018\\05\\input.txt"
with open(inputfile) as f:
    lines = f.readlines()

allChars = []
for line in lines:
    for c in line:
        allChars.append(c)



print(len(allChars))

bestCandidate = 'a'
bestLength = 11754

for c in ascii_lowercase:
    chars = [x for x in allChars if x != c and x != c.upper()]

    index = 0
    lastRead = '0'
    while index < len(chars) - 1:
        curr = chars[index]
        next = chars[index + 1]
        if (curr != next and curr.lower() == next.lower()):
            del chars[index]
            del chars[index]
            index -= 2
        index += 1
    
    if (len(chars) < bestLength):
        bestLength = len(chars)
        bestCandidate = c

print(bestLength)
print(c)