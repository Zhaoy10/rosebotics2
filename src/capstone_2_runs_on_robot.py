
import rosebotics_even_newer as rb
import time
import mqtt_remote_method_calls as com
import ev3dev.ev3 as ev3


def main():

    robot = rb.Snatch3rRobot()

    rc = RemoteControlEtc(robot)
    mqtt_client = com.MqttClient(rc)
    mqtt_client.connect_to_pc()

    print('Pressing the Top-Red Beacon button makes the robot beep once.  '
          'Pressing the Top-Blue Beacon button makes the robot say “Hello. How are you?”')
    print('exit by ctrl + c ')

    while True:
        if robot.beacon_button_sensor.is_top_red_button_pressed() is True:
            ev3.Sound.beep().wait()

        if robot.beacon_button_sensor.is_top_blue_button_pressed() is True:
            ev3.Sound.speak("hello. How are you?").wait()

        time.sleep(0.01)


class RemoteControlEtc(object):
    def __init__(self, robot):
        self.robot = robot


    def go_forward(self, speed_string):
        """Makes the robot go forward at the given speed."""
        print("Telling the robot to start moving at", speed_string)
        speed = int(speed_string)
        self.robot.drive_system.start_moving(speed, speed)


main()