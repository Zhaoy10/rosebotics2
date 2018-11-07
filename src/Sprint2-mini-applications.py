"""
  Capstone Project.  Code written by Rui Fang.
  Fall term, 2018-2019.
"""

import time
import rosebotics_even_newer as rb
import ev3dev.ev3 as ev3


def main():
    print('Testing arm function')
    run_test_arm()
    time.sleep(5)
    # print('Testing beep when wave hands')
    # run_test_beep_when_wave_hands()
    # time.sleep(5)
    # print('Testing beep when see big blob')
    # run_test_beep_if_blob()
    # time.sleep(5)


def run_test_beep_when_wave_hands():
    pass

def run_test_beep_if_blob():
    pass


def run_test_arm():
    robot = rb.Snatch3rRobot()
    print('calibrating')
    robot.arm.calibrate()
    print("Motor degree reset to {}".format(robot.arm.motor.get_degrees_spun()))
    time.sleep(5)
    print('moving to 4500')
    robot.arm.move_arm_to_position(4500)
    time.sleep(3)
    print('moving to 1000')
    robot.arm.move_arm_to_position(1000)


main()
