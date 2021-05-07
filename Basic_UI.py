import PySimpleGUI as sg

# Define the window's contents
# defining a column each element in the list is a row
col_layout =  [[sg.Text("Reservoir", font=("helvatica", 70), size=(80,1), justification="c")],  # print out "Reservoir"
               [sg.Text("%60", size=(200,1), justification="c")],                               # "%60" this will be change to a variable later just wanted to get a rough design out
               [sg.Text("Temperature", font=("helvatica", 70), size=(80,1), justification="c")],# "Temperature"
               [sg.Text("75"+chr(176), size=(200,1), justification="c")],                       # "75" should also become a variable later
               [sg.Text("Humidity", font=("helvatica", 70), size=(80,1), justification="c")],   # "Humidity"
               [sg.Text("%50", size=(200,1), justification="c")],                               # "%50" another stand in that needs to be changed to a variable
               [sg.Text("Water Pressure", font=("helvatica", 70), size=(80,1), justification="c")], # "Water Pressure"
               [sg.Text("80 psi", size=(200,1), justification="c")]]                            # "80 psi" should be variable

# Another column to have better control over where the buttons are placed
col_buttons = [ [sg.Button("Misting", size=(40, 20))],  # Mising Button
           [sg.Button("Light", size=(40, 20))],         # Light Button
           [sg.Button("Nutrients", size=(40, 20))] ]    # Nutrients Button

# Actual layout takes the other columns as variables as it only put things in rows.
layout = [[sg.Column(col_buttons), sg.Column(col_layout, pad=(0,0))]]

# Create the window
window = sg.Window('Control center', layout, finalize=True)      # Window Defintion
window.maximize() # Make the window to fit to the size of the screen

while True: # while the window is running
    events, values = window.read() # Gets all the events and values while the window is running
    if (event == 'Misting'): # Functionality for the misting button
        pass # Not yet implemented
    if (event == 'Light'): # Functionality of the light button
        pass # Not yet implemented
    if (event == 'Nutrients'): # Functionality of the Nutrients button
        pass # Not yet implemented
    
# Finish up by removing from the screen
window.close()  