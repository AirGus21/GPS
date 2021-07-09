import serial
import time
import string

while True: #count < collectionFreq + 1:
    port = "/dev/ttyAMA0"
    ser = serial.Serial(port, baudrate=9600, timeout=0.5)
    newdata = ser.readline()
    newdata = newdata.split(",")


    if newdata[0] == "$GPGGA":
		f = open("GPRMS.txt", "a")
		f.write(str(newdata))
		f.write("\n")
		f.close()