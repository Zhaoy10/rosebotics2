"""
  Capstone Project.  Code written by PUT_YOUR_NAME_HERE.
  Fall term, 2018-2019.
"""

import rosebotics as rb
import time


def main():
    """ Runs YOUR specific part of the project """
    run_test_go_straight_inches()
    run_test_spin_in_place_degrees()
    run_test_turn_degrees()



def run_test_go_straight_inches():
    frnb = rb.Snatch3rRobot()
    print("Test 1 Starts")
    frnb.drive_system.go_straight_inches(10)
    frnb.drive_system.stop_moving()
    time.sleep(5)

    print('Test 2 Starts')
    frnb.drive_system.go_straight_inches(-20)
    frnb.drive_system.stop_moving()
    time.sleep(5)

def run_test_spin_in_place_degrees():
    frnb = rb.Snatch3rRobot()
    print('Test 1 Starts')
    frnb.drive_system.spin_in_place_degrees(90)
    frnb.drive_system.stop_moving()
    time.sleep(5)

    print('Test 2 Starts')
    frnb.drive_system.spin_in_place_degrees(-180)
    frnb.drive_system.stop_moving()
    time.sleep(5)

def run_test_turn_degrees():
    frnb = rb.Snatch3rRobot()
    print('Test 1 Starts')
    frnb.drive_system.start_moving(100, 100)
    time.sleep(2)
    frnb.drive_system.turn_degrees(120)
    frnb.drive_system.stop_moving()
    time.sleep(5)

    print('Test 2 Starts')
    frnb.drive_system.start_moving(100, 100)
    time.sleep(2)
    frnb.drive_system.turn_degrees(-60)
    frnb.drive_system.stop_moving()
    time.sleep(5)

main()
