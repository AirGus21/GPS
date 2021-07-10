# import serial
import time
import string
import math
import tkinter as tk


def dist(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2)

def ddmmToDecimal(coord):
    long = int(coord[0][0:3]) + (float(coord[0][3:])/60)
    lat = int(coord[1][0:2]) + (float(coord[1][2:])/60)
    return [long, lat]

def getData(type):
    while True:
        port = "/dev/ttyAMA0"
        ser = serial.Serial(port, baudrate=9600, timeout=0.5)
        newdata = ser.readline()
        newdata = newdata.split(",")
        if ("$"+type) == newdata[0]:
            return newdata

def avgLocation(size, type):
    longCoords = []
    latCoords = []

    for i in range(size):
        data = getData("GPRMC")
        longCoords.append(float(data[5]))
        latCoords.append(float(data[3]))

    avgLongCoord = sum(longCoords)/len(longCoords)
    avgLatCoord = sum(latCoords)/len(latCoords)

    return [avgLongCoord, avgLatCoord]

def setLockCoord():
    return avgLocation(10, "GPRMC")

def getAngle(currentCoord, lockCoord):
    if currentCoord[0] < lockCoord[0]:  # Checks long
        if currentCoord[1] > lockCoord[1]:
            print(1)
            angle = 270 - math.degrees(math.acos((abs(currentCoord[0] - lockCoord[0])/dist(currentCoord, lockCoord))))
        else:
            print(2)
            angle = 270 + math.degrees(math.acos((abs(currentCoord[0] - lockCoord[0])/dist(currentCoord, lockCoord))))
    else:
        if currentCoord[1] > lockCoord[1]:
            print(3)
            angle = 90 + math.degrees(math.acos((abs(currentCoord[0] - lockCoord[0])/dist(currentCoord, lockCoord))))
        else:
            print(4)
            angle = 90 - math.degrees(math.acos((abs(currentCoord[0] - lockCoord[0])/dist(currentCoord, lockCoord))))
    return round(angle)

print(getAngle([-4, -4], [0, 0]))


window = tk.Tk()
window.mainloop()

# collectionFreq = 10
# count = 0
# latCoord = []
# longCoord = []


# while True: #count < collectionFreq + 1:
#     port = "/dev/ttyAMA0"
#     ser = serial.Serial(port, baudrate=9600, timeout=0.5)
#     newdata = ser.readline()
#     newdata = newdata.split(",")

#     if newdata[0] == "$GPRMC"  and count < collectionFreq:
#         print(newdata[1], len(latCoord), count)
#         latCoord.append(float(newdata[3]))
#         longCoord.append(float(newdata[5]))
#         file = open("coordsList.txt", "a")
#         file.write(str(sum(latCoord)/len(latCoord)) + ", " + str(sum(longCoord)/len(longCoord)))
#         file.write("\n")
#         file.close()
#         count += 1
#     elif newdata[0] == "$GPRMC" and count >= collectionFreq:
        
        
#         if len(lockCoord) == 0:
#             lockCoord.append(sum(latCoord)/len(latCoord))
#             lockCoord.append(sum(longCoord)/len(longCoord))
#         else:
#             currentCoord.append(sum(latCoord)/len(latCoord))
#             currentCoord.append(sum(longCoord)/len(longCoord))
        
#         latCoord = []
#         longCoord = []
#         count = 0