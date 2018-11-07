"""
  Capstone Project.  Code written by Rui Fang.
  Fall term, 2018-2019.
"""

import time
import rosebotics_even_newer as rb
import ev3dev.ev3 as ev3


def main():
    print('Testing arm function')
    # run_test_arm()
    # time.sleep(5)
    print('Testing beep when wave hands')
    # run_test_beep_when_wave_hands()
    time.sleep(5)
    print('Testing beep when see big blob')
    run_test_beep_if_blob()
    time.sleep(5)


def run_test_beep_when_wave_hands():
    robot = rb.Snatch3rRobot()
    print(robot.beacon_button_sensor.get_channel())
    while True:
        distance = robot.beacon_sensor.get_distance_to_beacon()
        # angle = robot.beacon_sensor.get_heading_to_beacon()
        print(distance)
        time.sleep(0.5)
        if distance >=9 and distance <= 13:
            break
    ev3.Sound.beep()


def run_test_beep_if_blob():
    robot = rb.Snatch3rRobot()
    while True:
        print('Prepare your blob in 3 seconds')
        time.sleep(3)
        if robot.camera.get_biggest_blob().get_area() >= 1000:
            print(robot.camera.get_biggest_blob().get_area())
            break
    ev3.Sound.beep()


def run_test_arm():
    robot = rb.Snatch3rRobot()
    print('calibrating')
    robot.arm.calibrate()
    print("Should be around 0:", robot.arm.motor.get_degrees_spun())
    time.sleep(5)
    print('moving to 4500')
    robot.arm.move_arm_to_position(4500)
    time.sleep(3)
    print('moving to 1000')
    robot.arm.move_arm_to_position(1000)


main()
