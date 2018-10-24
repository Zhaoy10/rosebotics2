"""
  Capstone Project.  Code written by PUT_YOUR_NAME_HERE.
  Fall term, 2018-2019.
"""

import rosebotics as rb
import time


def main():
    """ Runs YOUR specific part of the project """
    run_test_trace()

def run_test_trace():
    frnb = rb.Snatch3rRobot()
    left = 60
    right = 60
    while frnb.touch_sensor.get_value() == 0:
        while frnb.color_sensor.get_color() == 1:
            frnb.drive_system.start_moving(left, right)
            break

        while frnb.color_sensor.get_color() != 1:
            left = left+5
            frnb.drive_system.start_moving(left, right)
            break
    frnb.drive_system.stop_moving()

main()
