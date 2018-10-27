"""
  Capstone Project.  Code written by PUT_YOUR_NAME_HERE.
  Fall term, 2018-2019.
"""

import rosebotics as rb
import time


def main():
    """ Runs YOUR specific part of the project """
    run_test_wait_until_color_is()
    run_test_wait_until_intensity_is_greater_than()
    run_test_wait_until_intensity_is_less_than()



def run_test_wait_until_color_is():
    frnb = rb.Snatch3rRobot()
    print("Test 1 Starts")
    frnb.drive_system.start_moving(60, 60)
    time.sleep(2)
    frnb.color_sensor.wait_until_color_is(1)
    print('Black Detected!')
    frnb.drive_system.stop_moving()
    time.sleep(5)

    print('Test 2 Starts')
    frnb.drive_system.start_moving(60, 60)
    time.sleep(2)
    frnb.color_sensor.wait_until_color_is(6)
    print('Yellow Detected')
    frnb.drive_system.stop_moving()
    time.sleep(5)

def run_test_wait_until_intensity_is_greater_than():
    frnb = rb.Snatch3rRobot()
    print('Test 1 Starts')
    frnb.drive_system.start_moving(60, 60)
    time.sleep(2)
    frnb.color_sensor.wait_until_intensity_is_greater_than(-50)
    print('Light Detected!')
    frnb.drive_system.stop_moving()
    time.sleep(5)

    print('Test 2 Starts')
    frnb.drive_system.start_moving(60, 60)
    time.sleep(2)
    frnb.color_sensor.wait_until_intensity_is_greater_than(20)
    print('Light Detected!')
    frnb.drive_system.stop_moving()
    time.sleep(5)

def run_test_wait_until_intensity_is_less_than():
    frnb = rb.Snatch3rRobot()
    print('Test 1 Starts')
    frnb.drive_system.start_moving(60, 60)
    time.sleep(2)
    frnb.color_sensor.wait_until_intensity_is_less_than(-20)
    print('Dark Detected!')
    frnb.drive_system.stop_moving()
    time.sleep(5)

    print('Test 2 Starts')
    frnb.drive_system.start_moving(60, 60)
    time.sleep(2)
    frnb.color_sensor.wait_until_intensity_is_less_than(50)
    print('Dark Detected!')
    frnb.drive_system.stop_moving()
    time.sleep(5)

main()
