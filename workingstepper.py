import serial
import time

ser = serial.Serial('/dev/cu.usbmodem14101', 9600)
ser.timeout = 1

#while True:
    #i = input("Enter Message: ")
    #ser.write(i.encode())
    #time.sleep(0.5)
    #print(ser.readline().decode('ascii'))

