"""
  Capstone Project.  Code written by PUT_YOUR_NAME_HERE.
  Fall term, 2018-2019.
"""

import rosebotics as rb
import time


def main():
    """ Runs YOUR specific part of the project """
    run_test_wait_until_color_is()

def run_test_wait_until_color_is():
    frnb = rb.Snatch3rRobot()

    frnb.drive_system.start_moving(60, 60)
    frnb.color_sensor.wait_until_color_is(1)
    frnb.drive_system.stop_moving()
    time.sleep(5)
    frnb.drive_system.start_moving(-60, -60)
    frnb.color_sensor.wait_until_color_is(6)
    frnb.drive_system.stop_moving()


main()
