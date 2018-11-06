import ev3dev.ev3 as ev3
import time
import rosebotics_even_newer as rb
import tkinter
from tkinter import ttk


def main():
    run_tests()


def run_tests():
    run_infrared_beacon()
    time.sleep(5)
    # run_infrared_beacon_button()
    # time.sleep(5)
    # run_brick_button()
    # time.sleep(5)


def run_infrared_beacon():
    bcGUI = tkinter.Tk()
    bcGUI.geometry('50x50')

    frame1 = ttk.Frame(bcGUI, padding=10)
    frame1.grid()

    irbtn = ttk.Button(frame1, text='Infrared Beacon', command=move_to_beacon())
    irbtn.grid()

    bcGUI.mainloop()


def move_to_beacon():
    robot = rb.Snatch3rRobot()
    while True:
        robot.drive_system.spin_in_place_degrees(3)
        angle = robot.beacon_sensor.get_heading_to_beacon()
        if angle <= 5 and angle >= -5:
            while True:
                robot.drive_system.start_moving()
                if robot.beacon_sensor.get_distance_to_beacon() <= 5:
                    break
        break


def run_infrared_beacon_button():
    pass


def run_brick_button():
    pass



main()
