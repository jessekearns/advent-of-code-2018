inputfile = "C:\\Users\\jkearns\\Documents\\GitHub\\advent-of-code-2018\\02\\input.txt"
with open(inputfile) as f:
    lines = f.readlines()

listSize = len(lines)
wordSize = len(lines[0])

for i in range(0, listSize):
        for j in range (i+1, listSize):
                word1 = lines[i]
                word2 = lines[j]
                difCount = 0
                for k in range(0, wordSize):
                        if (word1[k] != word2[k]):
                                difCount += 1
                        if (difCount > 1):
                                break
                if (difCount == 1):
                        print(word1)
                        print(word2)