"""
  Capstone Project.  Code written by PUT_YOUR_NAME_HERE.
  Fall term, 2018-2019.
"""

import rosebotics as rb
import time


def main():
    """ Runs YOUR specific part of the project """
    frjb=rb.Snatch3rRobot()
    frjb.drive_system.start_moving(100,-100)
    time.sleep(5)
    frjb.drive_system.stop_moving()

main()
