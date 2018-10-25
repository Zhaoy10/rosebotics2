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

    for k in range(1000):
        left = 24
        right = 20
        frnb.drive_system.start_moving(left, right)

        while frnb.color_sensor.get_color() != 1:
            if left < 60:
                left = left+1
            frnb.drive_system.start_moving(left, right)
            print(frnb.color_sensor.get_color())
            break

        frnb.drive_system.stop_moving()

main()
