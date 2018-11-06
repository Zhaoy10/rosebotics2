"""
  Capstone Project.  Code written by PUT_YOUR_NAME_HERE.
  Fall term, 2018-2019.
"""

import rosebotics as rb
import time


def main():
    print('Please put the robot on the black oval')
    run_follow_black()
    time.sleep(5)
    print('Drawing triangle:')
    run_draw_polygons(3)
    time.sleep(3)
    print('Drawing pentagon:')
    run_draw_polygons(5)
    time.sleep(3)
    print('Drawing hexagon:')
    run_draw_polygons(6)
    time.sleep(5)
    print('Drive until white:')
    run_drive_until_color_is(6)
    time.sleep(3)
    print('Drive until yellow:')
    run_drive_until_color_is(4)
    time.sleep(5)
    """ Runs YOUR specific part of the project """


def run_follow_black():
    frnb=rb.Snatch3rRobot()
    while True:
        if frnb.touch_sensor.get_value() == 0:
            frnb.drive_system.start_moving(80, 50)
            if frnb.color_sensor.get_color() != 1:
                frnb.drive_system.start_moving(90, -50)
        if frnb.touch_sensor.get_value() == 1:
            break


def run_draw_polygons(x):
    frnb = rb.Snatch3rRobot()
    degree = 180-((x-2)*180/x)
    for k in range(x):
        frnb.drive_system.start_moving(100, 100)
        time.sleep(1)
        frnb.drive_system.turn_degrees(degree)
    frnb.drive_system.stop_moving()


def run_drive_until_color_is(color):
    frnb = rb.Snatch3rRobot()
    frnb.drive_system.start_moving(80,80)
    while True:
        frnb.color_sensor.wait_until_color_is(color)
        break
    frnb.drive_system.stop_moving()


main()
