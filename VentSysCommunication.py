import serial
import time

ser = serial.Serial("COM4", 9600, timeout=1)
time.sleep(2)

print("Kapcsolódva. Írj parancsot:")

while True:
    cmd = input(">> ")

    if cmd == "exit":
        break

    ser.write((cmd + "\n").encode())

    time.sleep(0.1)
    response = ser.readline().decode().strip()

    if response:
        print("Arduino:", response)

ser.close()