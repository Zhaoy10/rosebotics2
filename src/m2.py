"""
  Capstone Project.  Code written by PUT_YOUR_NAME_HERE.
  Fall term, 2018-2019.
"""

import rosebotics as rb
import time


def main():
    """ Runs YOUR specific part of the project """
    frjb=rb.Snatch3rRobot()
    while True:
        if frjb.touch_sensor.get_value()==0:
            frjb.drive_system.start_moving(80,50)
            if frjb.color_sensor.get_color()!=1:
                frjb.drive_system.start_moving(90,-50)
        if frjb.touch_sensor.get_value()==1:
            frjb.drive_system.stop_moving()






main()
