comparisonList = [8,9,4,5,0,1]
listLen = len(comparisonList)
r = [3, 7]
e1 = 0
e2 = 1

while True:
    sum = r[e1] + r[e2]
    if (sum >= 10):
        r.append(int(sum / 10))
        if r[-listLen:] == comparisonList:
            print(len(r) - listLen)
            break
        sum = sum % 10
    r.append(sum)
    if r[-listLen:] == comparisonList:
            print(len(r) - listLen)
            break
    e1 = (e1 + r[e1] + 1) % len(r)
    e2 = (e2 + r[e2] + 1) % len(r)