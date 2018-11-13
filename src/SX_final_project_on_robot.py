import mqtt_remote_method_calls as mqtt
import rosebotics_even_newer as robo


def main():
    robot = robo.Snatch3rRobot()
    mqtt_client = mqtt.MqttClient(robot)
    mqtt_client.connect_to_pc()
    robot.loop_forever()
    robot.find_beacon()
    mqtt_client.send_message("finished")


main()