import serial
import time

ser = serial.Serial('COM3', 9600)
ser.timeout = 1
time.sleep(1)


move = "R1"
ser.write(move.strip().encode())
print("Sent: ", move)
time.sleep(2)

move = "B2"
ser.write(move.strip().encode())
print("Sent: ", move)
time.sleep(2)

move = "F1"
ser.write(move.strip().encode())
print("Sent: ", move)
time.sleep(2)

move = "L2"
ser.write(move.strip().encode())
print("Sent: ", move)
time.sleep(2)

move = "R2"
ser.write(move.strip().encode())
print("Sent: ", move)
time.sleep(2)














