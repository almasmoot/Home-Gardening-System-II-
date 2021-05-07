import PySimpleGUI as sg

BackGround = 'green' # Background color for everyting
padding = (0,50) # (Width,Height)

# Define the window's contents
# defining a column each element in the list is a row
col_layout1 =  [[sg.Text("Reservoir", font=("helvatica", 50), size=(80,0), justification="c", background_color=BackGround, key="R", enable_events=True) ],  # print out "Reservoir"
               [sg.Text("%60", font=("helvetica", 30), size=(200,1), justification="c", background_color=BackGround)]]                               # "%60" this will be change to a variable later just wanted to get a rough design out

col_layout2 =  [[sg.Text("Temperature", font=("helvatica", 50), size=(80,1), justification="c", background_color=BackGround)],# "Temperature"
               [sg.Text("75"+chr(176), font=("helvetica", 30), size=(200,1), justification="c", background_color=BackGround)]]                       # "75" should also become a variable later

col_layout3 =  [[sg.Text("Humidity", font=("helvatica", 50), size=(80,0), justification="c", background_color=BackGround)],   # "Humidity"
               [sg.Text("%50", font=("helvetica", 30), size=(200,1), justification="c", background_color=BackGround)]]                               # "%50" another stand in that needs to be changed to a variable

col_layout4 =  [[sg.Text("Water Pressure", font=("helvatica", 50), size=(80,1), justification="c", background_color=BackGround)], # "Water Pressure"
               [sg.Text("80 psi", font=("helvetica", 30), size=(200,1), justification="c", background_color=BackGround)]]                            # "80 psi" should be variable

# Another column to have better control over where the buttons are placed
col_buttons = [ [sg.Button("Home", size=(30, 15), button_color=BackGround)],
           [sg.Button("Misting", size=(30, 15), button_color=BackGround)],  # Mising Button
           [sg.Button("Light", size=(30, 15), button_color=BackGround)],         # Light Button
           [sg.Button("Nutrients", size=(30, 15), button_color=BackGround)] ]    # Nutrients Button

columns = [[sg.Column(col_layout1, background_color=BackGround, pad=padding)],
           [sg.Column(col_layout2, background_color=BackGround, pad=padding)],
           [sg.Column(col_layout3, background_color=BackGround, pad=padding)],
           [sg.Column(col_layout4, background_color=BackGround, pad=padding)]]

# Actual layout takes the other columns as variables as it only put things in rows.
layout = [[sg.Column(col_buttons, background_color=BackGround), sg.Column(columns, background_color=BackGround, pad=(0,0))]]


# Create the window
window = sg.Window('Control center', layout, finalize=True, no_titlebar=False, background_color=BackGround)      # Window Defintion
window.maximize() # Make the window to fit to the size of the screen

while True: # while the window is running
    event, values = window.read() # Gets all the events and values while the window is running
    if (event == sg.WIN_CLOSED):
        break
    if (event == 'Misting'): # Functionality for the misting button
        pass # Not yet implemented
    if (event == 'Light'): # Functionality of the light button
        pass # Not yet implemented
    if (event == 'Nutrients'): # Functionality of the Nutrients button
        pass # Not yet implemented
    if (event == 'R'):
        window.TKroot.configure(background="blue")

    
    
# Finish up by removing from the screen
window.close()  