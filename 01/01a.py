inputfile = "C:\\Users\\jkearns\\Documents\\GitHub\\advent-of-code-2018\\01\\input.txt"
with open(inputfile) as f:
    lines = f.readlines()

vals = []

for line in lines:
    segs = line.split('\n')
    vals.append(int(segs[0]))



print(sum(vals))


