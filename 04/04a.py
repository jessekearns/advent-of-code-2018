inputfile = "C:\\Users\\jkearns\\Documents\\GitHub\\advent-of-code-2018\\04\\inputModified.txt"
with open(inputfile) as f:
    lines = f.readlines()

minutesInADay = 24 * 60

# status vars
currentId = 0
sleptAtMinute = 0

# current totals
sleptMinutesById = {}
timeSleptThroughMinuteById = {}

for line in lines:
    seg = line.split(',')
    #month = int(seg[0])
    #day = int(seg[1])
    minute = (int(seg[2]) * 60) + int(seg[3]) # express time in total minutes to handle sleep > 1 hour
    status = seg[4]
    if (seg[4] == 'w\n' or seg[4] == 'w'):
        # Wake up - update dictionary of slept minutes
        minutesAsleep = (minute - sleptAtMinute) % minutesInADay
        sleptMinutesById[currentId] += minutesAsleep
        # Update most likely minutes
        for i in range(sleptAtMinute, sleptAtMinute + minutesAsleep):
            properMinuteValue = i % minutesInADay
            if (properMinuteValue not in timeSleptThroughMinuteById[currentId]):
                timeSleptThroughMinuteById[currentId][properMinuteValue] = 0
            timeSleptThroughMinuteById[currentId][properMinuteValue] += 1
        # reset status
        sleptAtMinute = 0
    elif (seg[4] == 's\n' or seg[4] == 's'):
        # sleeping
        sleptAtMinute = minute
    else: # New guard clocks in
        # Update status, add guard to dictionaries if it's not present
        currentId = int(seg[4])
        if (currentId not in sleptMinutesById):
            sleptMinutesById[currentId] = 0
        if (currentId not in timeSleptThroughMinuteById):
            timeSleptThroughMinuteById[currentId] = {}

# values stored: get the best
currentBest = 0
currentBestId = 0
for key in sleptMinutesById:
    if sleptMinutesById[key] > currentBest:
        currentBest = sleptMinutesById[key]
        currentBestId = key

print("Guard who slept the most minutes:")
print(currentBestId)
print('')

currentBestTimes = 0
currentBestMinute = 0
gMinutes = timeSleptThroughMinuteById[currentBestId]
for minute in gMinutes:
    if (gMinutes[minute] > currentBestTimes):
        currentBestTimes = gMinutes[minute]
        currentBestMinute = minute

print("Minute slept the most:")
print(currentBestMinute)
print('')

print(currentBestMinute * currentBestId)