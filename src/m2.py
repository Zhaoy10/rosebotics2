"""
  Capstone Project.  Code written by PUT_YOUR_NAME_HERE.
  Fall term, 2018-2019.
"""

import rosebotics as rb
import time


def main():
    """ Runs YOUR specific part of the project """
    frjb=rb.Snatch3rRobot()
    while frjb.touch_sensor.get_value()==0:
        frjb.drive_system.start_moving(60,40)
        time.sleep(0.2)
        if frjb.color_sensor.get_color()!=1:
            frjb.drive_system.start_moving(0,0)
            time.sleep(20)




main()
