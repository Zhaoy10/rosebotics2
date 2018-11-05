import time
import rosebotics_even_newer as rb


def main():
    print('Testing beep when wave hands')
    run_test_beep_when_wave_hands()
    time.sleep(3)
    print('Testing beep when see big objects')
    run_test_beep_when_sees_big()
    time.sleep(3)


def run_test_beep_when_wave_hands():
    robot = rb.Snatch3rRobot()
    robot.camera.set_signature()





def run_test_beep_when_sees_big():



main()