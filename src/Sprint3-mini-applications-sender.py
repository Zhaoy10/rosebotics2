import ev3dev.ev3 as ev3
import time
import rosebotics_even_newer as rb
import tkinter
from tkinter import ttk
import mqtt_remote_method_calls as com


mqtt_client = com.MqttClient()
mqtt_client.connect('fr', 'robo32')
time.sleep(1)



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
    gui.title = 'Robot Controller'
    gui.geometry('80x100')

    frame1 = ttk.Frame(gui, padding=10)
    frame1.grid()

    redup = ttk.Button(frame1, text='Red Up', command=red_up_on_click())
    redup.grid()

    blueup = ttk.Button(frame1, text='Blue Up', command=None)
    blueup.grid()

    gui.mainloop()


def red_up_on_click():
    mqtt_client.send_message('move', [11])
    print('Red On Click')


def blue_up_on_clicl():
    mqtt_client.send_message('move', [-11])
    print('Blue On Click')


def run_brick_button():
    pass


run_tests()
