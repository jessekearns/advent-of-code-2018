inputfile = "C:\\Users\\jkearns\\Documents\\GitHub\\advent-of-code-2018\\05\\input.txt"
with open(inputfile) as f:
    lines = f.readlines()

chars = []
for line in lines:
    for c in line:
        chars.append(c)

index = 0
lastRead = '0'

print(len(chars))

while index < len(chars) - 1:
    curr = chars[index]
    next = chars[index + 1]
    if (curr != next and curr.lower() == next.lower()):
        del chars[index]
        del chars[index]
        index -= 2
    index += 1


print(len(chars))