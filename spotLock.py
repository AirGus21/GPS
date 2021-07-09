import serial
import time
import string


def getData(type):
    port = "/dev/ttyAMA0"
    ser = serial.Serial(port, baudrate=9600, timeout=0.5)
    newdata = ser.readline()
    newdata = newdata.split(",")
    if ("$"+type) == newdata[0]:
        return newdata



def setLockCoord():
    print(getData("GPRMC"))

    lockLat = 0
    lockLong = 0

    return [lockLong, lockLat]


setLockCoord()



# lockCoord = []
# currentCoord = []


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