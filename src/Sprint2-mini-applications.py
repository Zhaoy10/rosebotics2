import time
import rosebotics_even_newer as rb
import ev3dev.ev3 as ev3

def main():
    print('Testing arm function')
    run_test_arm()
    time.sleep(5)
    print('Testing beep when wave hands')
    run_test_beep_when_wave_hands()
    time.sleep(5)
    print('Testing beep when see big blob')
    run_test_beep_if_blob()
    time.sleep(5)


def run_test_beep_when_wave_hands():
    robot = rb.Snatch3rRobot()
    robot.beacon_button_sensor.get_channel(1)
    while True:
        distance = robot.beacon_sensor.get_distance_to_beacon()
        angle = robot.beacon_sensor.get_heading_to_beacon()
        if distance >=9 and distance <= 13:
            break
    ev3.Sound.beep()


def run_test_beep_if_blob():
    robot = rb.Snatch3rRobot()
    while True:
        print('Prepare your blob in 3 seconds')
        time.sleep(3)
        robot.camera.set_signature()
        if robot.camera.get_biggest_blob().get_area() >= 1000:
            break
    ev3.Sound.beep()


def run_test_arm():
    robot = rb.Snatch3rRobot()
    robot.arm.calibrate()
    time.sleep(3)
    robot.arm.raise_arm_and_close_claw()
    time.sleep(3)
    robot.arm.move_arm_to_position(300)


main()
