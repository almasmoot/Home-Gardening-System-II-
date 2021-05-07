import PySimpleGUI as sg
import json
import generate_test_json

# Define the window's contents
layout = [[sg.Text(size=(40,1), key='-OUTPUT-')],
          [sg.Button('Quit')]]

# Create the window
window = sg.Window('Window Title', layout, size=(800, 480), no_titlebar=True)
string = ''
# Display and interact with the Window using an Event Loop
while True:
    data = json.loads(open("touch_screen/test_data.json", "r").read())
    event, values = window.read(timeout=1000)
    # See if user wants to quit or window was closed
    if event == sg.WINDOW_CLOSED or event == 'Quit':
        break
    if data.get("humidity") < 50:
        string = "HUMIDITY IS TOO LOW"
        window.TKroot.configure(background="red")
    elif data.get("temp") < 50:
        string = "TEMPERATURE IS TOO LOW"
        window.TKroot.configure(background="orange")
    elif data.get("water_pressure") < 50:
        string = "WATER PRESSURE IS TOO LOW"
        window.TKroot.configure(background="green")
    elif data.get("water_level") < 50:
        string = "WATER LEVEL IS TOO LOW"
        window.TKroot.configure(background="yellow")
    else:
        string = 'EVERYTHING IS OKAY'
        window.TKroot.configure(background="blue")
    window['-OUTPUT-'].update(string)
    generate_test_json.generate_new_data()
    # Output a message to the window

# Finish up by removing from the screen
window.close()