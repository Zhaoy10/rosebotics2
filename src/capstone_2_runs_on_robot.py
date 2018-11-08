"""
Mini-application:  Buttons on a Tkinter GUI tell the robot to:
  - Go forward at the speed given in an entry box.

Also: responds to Beacon button-presses by beeping, speaking.

This module runs on the ROBOT.
It uses MQTT to RECEIVE information from a program running on the LAPTOP.

Authors:  David Mutchler, his colleagues, and Shuang XIa.
"""
# ------------------------------------------------------------------------------
# DO: 1. PUT YOUR NAME IN THE ABOVE LINE.  Then delete this DO.
# ------------------------------------------------------------------------------

# ------------------------------------------------------------------------------
# DO: 2. With your instructor, review the "big picture" of laptop-robot
# DO:    communication, per the comment in mqtt_sender.py.
# DO:    Once you understand the "big picture", delete this DO.
# ------------------------------------------------------------------------------

import rosebotics_even_newer as rb
import time
import mqtt_remote_method_calls as com
import ev3dev.ev3 as ev3


def main():
    # --------------------------------------------------------------------------
    # DO: 3. Construct a Snatch3rRobot.  Test.  When OK, delete this DO.
    # --------------------------------------------------------------------------
    robot = rb.Snatch3rRobot()
    # --------------------------------------------------------------------------
    # DO: 4. Add code that constructs a   com.MqttClient   that will
    # DO:    be used to receive commands sent by the laptop.
    # DO:    Connect it to this robot.  Test.  When OK, delete this DO.
    # --------------------------------------------------------------------------
    rc = RemoteControlEtc(robot)
    mqtt_client = com.MqttClient(rc)
    mqtt_client.connect_to_pc()
    # --------------------------------------------------------------------------
    # DO: 5. Add a class for your "delegate" object that will handle messages
    # DO:    sent from the laptop.  Construct an instance of the class and
    # DO:    pass it to the MqttClient constructor above.  Augment the class
    # DO:    as needed for that, and also to handle the go_forward message.
    # DO:    Test by PRINTING, then with robot.  When OK, delete this DO.
    # --------------------------------------------------------------------------

    # --------------------------------------------------------------------------
    # DO: 6. With your instructor, discuss why the following WHILE loop,
    # DO:    that appears to do nothing, is necessary.
    # DO:    When you understand this, delete this DO.
    # --------------------------------------------------------------------------
    while True:
        # ----------------------------------------------------------------------
        # DO: 7. Add code that makes the robot beep if the top-red button
        # DO:    on the Beacon is pressed.  Add code that makes the robot
        # DO:    speak "Hello. How are you?" if the top-blue button on the
        # DO:    Beacon is pressed.  Test.  When done, delete this DO.
        # ----------------------------------------------------------------------
        print('Pressing the Top-Red Beacon button makes the robot beep once.  '
              'Pressing the Top-Blue Beacon button makes the robot say “Hello. How are you?”')
        print('exit by ctrl + c ')

        while True:
            if robot.beacon_button_sensor.is_top_red_button_pressed() is True:
                ev3.Sound.beep().wait(0.1)

            if robot.beacon_button_sensor.is_top_blue_button_pressed() is True:
                ev3.Sound.speak("hello. How are you?").wait(0.1)

        time.sleep(0.01)  # For the delegate to do its work


class RemoteControlEtc(object):
    def __init__(self, robot):
        self.robot = robot
        """
        Stores the robot.
        :type robot: rb.Snatch3rRobot
        """

    def go_forward(self, speed_string):
        """Makes the robot go forward at the given speed."""
        print("Telling the robot to start moving at", speed_string)
        speed = int(speed_string)
        self.robot.drive_system.start_moving(speed, speed)


main()