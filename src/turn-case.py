"""
  Capstone Project.  Code written by PUT_YOUR_NAME_HERE.
  Fall term, 2018-2019.
"""

import rosebotics as rb
import time


def main():
    frsb=rb.Snatch3rRobot()
    frsb.drive_system.start_moving(100,0)
    time.sleep(2)
    """ Runs YOUR specific part of the project """
def test_turn():
    frsb=rb.Snatch3rRobot()
    frsb.drive_system.spin_in_place_degrees(90)
    time.sleep(5)
    frsb.drive_system.spin_in_place_degrees(-90)


main()
