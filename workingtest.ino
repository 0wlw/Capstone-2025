import serial
import time

ser = serial.Serial('/dev/cu.usbmodem14101', 9600)
ser.timeout = 1

while True:
    i = input("Enter message: ").strip()

    if i == "quit":
        print("Quiting")
        break

    ser.write(i.encode())
    time.sleep(0.5)
    print(ser.readline().decode('ascii'))

ser.close()
