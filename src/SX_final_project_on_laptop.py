
import tkinter
from tkinter import ttk
import mqtt_remote_method_calls as com
import rosebotics_even_newer


def main():

    root = tkinter.Tk()

    mqtt_client = com.MqttClient()
    mqtt_client.connect_to_ev3()

    setup_gui(root, mqtt_client)

    root.mainloop()


def setup_gui(root_window, mqtt_client):

    frame = ttk.Frame(root_window, padding=10)
    frame.grid()

    seek_beacon_button = ttk.Button(frame, text="Seek Beacon")

    seek_beacon_button.grid()

    seek_beacon_button['command'] = \
        lambda: seek_beacon(mqtt_client)


def seek_beacon(mqtt_client):

    mqtt_client.send_message('find_beacon')
    print('Sending the seeking beacon')

    print('beacon found')





main()
