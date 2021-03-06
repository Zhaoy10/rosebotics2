"""
  Capstone Project.  Code written by Rui Fang.
  Fall term, 2018-2019.
"""

import mqtt_remote_method_calls as com
import time
import ev3dev.ev3 as ev3
import rosebotics_even_newer as rb
from ev3dev import


class MyDelegate(object):
    def __init__(self):
        self.robot = rb.Snatch3rRobot()
        self.mqtt_client = None  # To be set later.
        self.ev3 = ev3

    def arm_up(self):
        self.robot.arm.move_arm_to_position(5000)
        self.mqtt_client.send_message('Arm Up!')

    def move(self, inches):
        self.robot.drive_system.go_straight_inches(inches)
        self.mqtt_client.send_message('Moved for {} inches!'.format(inches))

    def find_beacon(self):
        while True:
            self.robot.drive_system.spin_in_place_degrees(3)
            angle = self.robot.beacon_sensor.get_heading_to_beacon()
            if angle <= 3 and angle >= -3:
                self.mqtt_client.send_message('Beacon Found!')
                while True:
                    self.robot.drive_system.start_moving()
                    if self.robot.beacon_sensor.get_distance_to_beacon() <= 5:
                        break
            break

    def beep_once(self):
        ev3.Sound.beep()

    def beep_twice(self):
        ev3.Sound.beep()
        time.sleep(0.15)
        ev3.Sound.beep()


def main():
     robot_action = MyDelegate()
     mqtt_client = com.MqttClient(robot_action)
     robot_action.mqtt_client = mqtt_client
     mqtt_client.connect('robo32', 'fr')
     mqtt_client.send_message('Connected!')

     while True:
         time.sleep(0.01)  # Time to allow message processing


main()
