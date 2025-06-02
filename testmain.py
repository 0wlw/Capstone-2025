import kociemba
import serial
import time


solution = kociemba.solve("UUUUUUUUUBBBRRRRRRRRRFFFFFFDDDDDDDDDFFFLLLLLLLLLBBBBBB")
print("Solved cube")

# Establish serial connection (adjust port as needed)
arduino = serial.Serial(port='COM8', baudrate=9600, timeout=.1)
time.sleep(2) # Wait for the connection to establish
print("Connected to board.")

def write_read(x):
    arduino.write(bytes(x, 'utf-8'))
    time.sleep(0.05)
    data = arduino.readline()
    return data
print("Solution: ", solution)

if solution == "U'":
    x = '13'

write_read(x)
print("Solution sent to board ", x)
