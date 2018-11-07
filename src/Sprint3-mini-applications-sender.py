"""
  Capstone Project.  Code written by Rui Fang.
  Fall term, 2018-2019.
"""

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
    pass


def move_to_beacon():
    gui = tkinter.TK()
    gui.title ='move to beacon'
    gui.geometry('100x100')

    frame1= ttk.Frame(gui, padding=100)
    frame1.grid()

    start = ttk.Button(frame1,text='start',command=lamda:)
    start.grid()



def run_infrared_beacon_buttons():
    """"""
    gui = tkinter.Tk()
    gui.title = 'Robot Controller'
    gui.geometry('80x150')

    frame1 = ttk.Frame(gui, padding=10)
    frame1.grid()

    frame2 = ttk.Frame(gui, padding=30)
    frame2.grid()

    redup = ttk.Button(frame1, text='Red Up', command=lambda: red_up_on_click())
    redup.grid()

    blueup = ttk.Button(frame2, text='Blue Up', command=lambda: blue_up_on_click())
    blueup.grid()

    gui.mainloop()


def red_up_on_click():
    mqtt_client.send_message('move', [11])
    print('Red On Click')


def blue_up_on_click():
    mqtt_client.send_message('move', [-11])
    print('Blue On Click')


def run_brick_button():
    pass


run_tests()
