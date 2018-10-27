"""
  Capstone Project.  Code written by PUT_YOUR_NAME_HERE.
  Fall term, 2018-2019.
"""

import rosebotics as rb
import time


def main():
    run_follow_black()
    run_draw_polygons(3)
    run_draw_polygons(5)
    run_draw_polygons(6)
    """ Runs YOUR specific part of the project """


def run_follow_black():
    frjb=rb.Snatch3rRobot()
    while True:
        if frjb.touch_sensor.get_value()==0:
            frjb.drive_system.start_moving(80,50)
            if frjb.color_sensor.get_color()!=1:
                frjb.drive_system.start_moving(90,-50)
        if frjb.touch_sensor.get_value()==1:
            break
    time.sleep(5)

def run_draw_polygons(x):
    frnb = rb.Snatch3rRobot()
    degree = 180-((x-2)*180/x)
    for k in range(x):
        frnb.drive_system.start_moving(100, 100)
        time.sleep(1)
        frnb.drive_system.turn_degrees(degree)
    frnb.drive_system.stop_moving()


main()
