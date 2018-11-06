import ev3dev.ev3 as ev3
import time
import rosebotics_even_newer as rb
import tkinter
from tkinter import ttk
import mqtt_remote_method_calls as com


def main():

    mqtt_client = com.MqttClient()
    mqtt_client.connect('fr', 'robo32')
    time.sleep(1)

    run_tests()

    while True:
        s = input("Enter a message: ")
        mqtt_client.send_message("say_it", [s])



def run_tests():
    # run_infrared_beacon()
    # time.sleep(5)
    run_infrared_beacon_buttons()
    time.sleep(5)
    # run_brick_button()
    # time.sleep(5)


def run_infrared_beacon():
    gui = tkinter.Tk()
    gui.geometry('100x100')

    frame1 = ttk.Frame(gui, padding=10)
    frame1.grid()

    irbtn = ttk.Button(frame1, text='Infrared Beacon', command=None)
    irbtn.grid()

    gui.mainloop()


def move_to_beacon():
    pass


def run_infrared_beacon_buttons():
    gui = tkinter.Tk()
    gui.geometry('80x100')

    frame1 = ttk.Frame(gui, padding=10)
    frame1.grid()

    redup = ttk.Button(frame1, text='Red Up', command=None)
    redup.grid()

    blueup = ttk.Button(frame1, text='Blue Up', command=None)
    blueup.grid()

    gui.mainloop()


def red_up_on_click():
    global mqtt_client
    mqtt_client.send_message('move', [11])


def run_brick_button():
    pass



main()
