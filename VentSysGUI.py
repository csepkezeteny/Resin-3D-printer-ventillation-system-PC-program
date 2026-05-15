import tkinter as tk
import tkinter.ttk as ttk

def updateData():
    "Updates the datas received from the Arduino through Bluetooth"
    pass

def emergencyButton():
    "When the emergency stop button is pushed, the system will stop complitely"
    pass

def sendConsole():
    "Send the console's content"
    pass



def makeMainWindow():
    "Creates the main window with all the widgets needed to controll the system and monitor the variables"
    main_window = tk.Tk()
    main_window.configure(bg="pink")

    fan1_frame = tk.Frame(main_window, bg="red")
    fan2_frame = tk.Frame(main_window, bg="blue")

    sensorsData_frame = tk.Frame(main_window, bg="yellow")

    console_frame = tk.Frame(main_window, bg="brown")

    settings_frame = tk.Frame(main_window, bg="black")


    fan1_frame.grid(row=0, column=0)
    fan2_frame.grid(row=0, column=1)

    sensorsData_frame.grid(row=0, column=2)

    console_frame.grid(row=1, column=2)

    settings_frame.grid(row=0, column=3)
    #Fan 1 & 2 control 
    fan1_scale = tk.Scale(fan1_frame, orient="vertical", from_= 255, to=0).pack()
    fan2_scale = tk.Scale(fan2_frame, orient="vertical", from_= 255, to=0).pack()

    fan1_entry = tk.Entry(fan1_frame).pack()
    fan2_entry = tk.Entry(fan2_frame).pack()

    fan1_label = tk.Label(fan1_frame, text="FAN 1 SPEED").pack()
    fan2_label = tk.Label(fan2_frame, text="FAN 2 SPEED").pack()

    fan_send_button = tk.Button(fan1_frame, text="Update fans speed").pack()
    #----------------

    #Sensorsdata frame
    #DHT11, DS18D20, MQ-135

    sensor1_name = tk.Label(sensorsData_frame, text="C* inside").grid(row=0, column=0)
    sensor2_name = tk.Label(sensorsData_frame, text="Humidity (%)").grid(row=0, column=1)
    sensor3_name = tk.Label(sensorsData_frame, text="Gas").grid(row=0, column=2)

    sensor1_data = tk.Label(sensorsData_frame, text="23").grid(row=1, column=0)
    sensor2_data = tk.Label(sensorsData_frame, text="54").grid(row=1, column=1)
    sensor3_data = tk.Label(sensorsData_frame, text="543").grid(row=1, column=2)


    sensors_data_prog = ttk.Progressbar(sensorsData_frame, orient="horizontal", mode="determinate").grid(row=2, column=0, columnspan=3)
    #-----------------

    #debug serial console
    console = tk.Text(console_frame, height=10, width=50).grid(row=0, column=0)
    console_send_button = tk.Button(console_frame, text="Send").grid(row=0, column=1)
    #--------------------
    #setting
    update_settings = tk.Button(settings_frame, text="Update settings").grid(row=0 , column=0, columnspan=2)

    serial_label = tk.Label(settings_frame, text="Serial port (e.g.: COM6):").grid(row=1 , column=0)
    serial_port = tk.Entry(settings_frame).grid(row=1 , column=1)

    emergency_stop = tk.Button(settings_frame, text="EMERGENCY STOP", background="red", foreground="white").grid(row=2 , column=0, columnspan=2)


    main_window.mainloop()