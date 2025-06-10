import twophase.solver as tpsv
import serial
import time

#arduino = serial.Serial(port='/dev/cu.usbmodem14101', baudrate=9600, timeout=.1)
#time.sleep(2) 
#print("Connected to board.")

cubestring = ""
colors = ['W', 'R', 'G', 'Y', 'O', 'B']
color_string = ""

for color in colors:
    message_str = "Enter the colors on the ", color, " face: "
    color_string += input(message_str)

for letter in color_string:
    if letter == "W":
        cubestring += "U"
    elif letter == "R":
        cubestring += "R"
    elif letter == "G":
        cubestring += "F"
    elif letter == "Y":
        cubestring += "D"
    elif letter == "O":
        cubestring += "L"
    elif letter == "B":
        cubestring += "B"

print(cubestring)
print(tpsv.solve(cubestring, 19, 2))
solution = tpsv.solve(cubestring, 19, 2)
print(type(solution))

send_str = ""
for move in solution.split(' '):
    print(move)
    if move == "U1":
        send_str = "11"
    elif move == "U2":
        send_str = "12"
    elif move == "U3":
        send_str = "13"
    elif move == "R1": ######
        send_str = "21"
    elif move == "R2":
        send_str = "22"
    elif move == "R3":
        send_str = "23"
    elif move == "F1": ######
        send_str = "31"
    elif move == "F2":
        send_str = "32"
    elif move == "F3":
        send_str = "33"
    elif move == "D1": ######
        send_str = "41"
    elif move == "D2":
        send_str = "42"
    elif move == "D3":
        send_str = "43"
    elif move == "L1": ######
        send_str = "51"
    elif move == "L2":
        send_str = "52"
    elif move == "L3":
        send_str = "53"
    elif move == "B1": ######
        send_str = "61"
    elif move == "B2":
        send_str = "62"
    elif move == "B3":
        send_str = "63"

    print(send_str) #BUGS: THE NUMBER OF MOVES SHOWN IN SOLUTION STR NEEDS TO BE REMOVED
