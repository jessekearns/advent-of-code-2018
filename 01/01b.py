inputfile = "C:\\Users\\jkearns\\Documents\\GitHub\\advent-of-code-2018\\01\\input.txt"
with open(inputfile) as f:
    lines = f.readlines()

vals = []

for line in lines:
    segs = line.split('\n')
    vals.append(int(segs[0]))

sum = 0
steps = 0
prevSums = {0:0}
while True:
        sum += vals[steps % len(vals)]
        steps += 1
        if sum in prevSums:
                break
        prevSums[sum] = steps
        
print("Solution: ")
print(sum)
print("")

print("First at (loop, then step): ")
print(int(prevSums[sum] / len(vals)))
print(int(prevSums[sum] % len(vals)))
print("")

print("Next at (loop, then step): ")
print(int(steps / len(vals)))
print(steps % len(vals))
print("")