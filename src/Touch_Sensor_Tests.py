"""
  Capstone Project.  Code written by PUT_YOUR_NAME_HERE.
  Fall term, 2018-2019.
"""

import rosebotics as rb
import time


def main():
    """ Runs YOUR specific part of the project """
    run_test_wait_until_pressed()
    run_test_wait_until_released()

def run_test_wait_until_pressed():
    frnb = rb.Snatch3rRobot()
    print("Test 1 Starts")
    frnb.drive_system.start_moving(60, 60)
    time.sleep(2)
    frnb.touch_sensor.wait_until_pressed()
    print('Press Detected!')
    frnb.drive_system.stop_moving()
    time.sleep(5)

def run_test_wait_until_released():
    frnb = rb.Snatch3rRobot()
    print('Test 1 Starts')
    frnb.drive_system.start_moving(60, 60)
    time.sleep(2)
    frnb.touch_sensor.wait_until_released()
    print('Release Detected!')
    frnb.drive_system.stop_moving()
    time.sleep(5)


main()
