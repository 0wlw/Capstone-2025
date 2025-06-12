import random
import serial
import time

ser = serial.Serial('COM3', 9600)
ser.timeout = 1
time.sleep(1)

moves = ["U1", "U2", "U3", "R1", "R2", "R3", "F1", "F2", "F3", "L1", "L2", "L3", "B1", "B2", "B3", "D1", "D2", "D3", ]
limited_moves = ["R1", "R2", "R3", "F1", "F2", "F3", "L1", "L2", "L3", "B1", "B2", "B3", ]

def scramble(num_moves=5, limit_faces=True):
    if limit_faces:
        for i in range(num_moves):
            index = random.randint(0, 17)
            move = limited_moves[index]

            ser.write(move.strip().encode())
            print("Sent: ", move)
            time.sleep(2)
    else:
        for i in range(num_moves):
            index = random.randint(0, 17)
            move = moves[index]

            ser.write(move.strip().encode())
            print("Sent: ", move)
            time.sleep(2)

scramble()
