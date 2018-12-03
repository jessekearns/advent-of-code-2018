inputfile = "C:\\Users\\jkearns\\Documents\\GitHub\\advent-of-code-2018\\02\\input.txt"
with open(inputfile) as f:
    lines = f.readlines()

twos = 0
threes = 0

for line in lines:
    twofer = False
    threefer = False
    for c in line:
        ccount = line.count(c)
        if (ccount == 2):
            twofer = True
        if (ccount == 3):
            threefer = True
    if (twofer):
        twos += 1
    if (threefer):
        threes += 1

checksum = twos * threes

print(checksum)