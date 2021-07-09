readFile = open("coordsList.txt", "r")
writeFile = open("Path.txt", "w")

for line in readFile:
    line = line.replace(" ", "")
    line = line.split(',')
    lat = int(line[0][0:2]) + (float(line[0][2:])/60)
    long = int(line[1][0:2]) + (float(line[1][2:])/60)
    writeFile.write(str(lat) + ",-" + str(long))
    writeFile.write("\n")
writeFile.close()