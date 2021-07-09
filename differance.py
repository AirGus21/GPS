f = open("coordsList.txt", "r")

latCoords = []

error = []

prevLine = 0

for l in f:
    l = l.split(',')
    error.append(float(l[0]) - float(prevLine))
    prevLine = l[0]
    latCoords.append(float(l[0]))
error.pop(0)

avgError = sum(error)/len(error)

print(max(latCoords))
print(min(latCoords))
print(str(sum(latCoords)/len(latCoords)))

count = 0
for lat in latCoords:
    if abs(lat - 4512.61522679) < 0.001:
        count += 1

print(count)


print("Minutes: " + str(avgError), "Feet: " + str(avgError * 6068), "Range(ft): " + str((max(error) - min(error)) * 6068))