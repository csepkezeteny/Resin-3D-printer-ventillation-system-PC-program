import serial
import time
import VentSysGUI as VSG

serial_connection = serial.Serial(VSG.serial_port, VSG.serial_baud_rate, timeout=1)
time.sleep(2)



def readSerial():
    read_serial = serial_connection.readline().decode().strip()

def writeSerial():
    pass
#-----------------------------------------------------------
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
#-----------------------------------------------------------

