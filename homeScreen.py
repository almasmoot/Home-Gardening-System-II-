import sys  # to get the screen size and close the window
from PyQt5.QtCore import Qt     # all the pyqt5 libraries we need
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

BUTTONFONT = QFont("times", 30) # font for the tabs
LABELFONT1 = QFont("times", 60) # font for the bigger labels (reservoir, temperature)
LABELFONT2 = QFont("times", 30) # font for the readings for the labels (60%)

class homeScreen(QWidget):
    def __init__(self, parent):
        super(homeScreen, self).__init__(parent)
        self.initUI(parent)

    def initUI(self, parent): # initUI function will set up all the labels and buttons we want for the ui                     

        self.Reservoir = QLabel(self)              # Make the Reservoir label                             
        self.Reservoir.setText("Reservoir")        # Set the text                                         
        self.Reservoir.setFont(LABELFONT1)         # Set the font for the label                           
        self.Reservoir.setAlignment(Qt.AlignCenter)# This will align it to the center                        
        self.R_amount = QLabel(self)               # Make the Reservoir amount label                      
        self.R_amount.setText("%60")               # set the text (this should implement a variable later)
        self.R_amount.setFont(LABELFONT2)          # set the font                                          
        self.R_amount.setAlignment(Qt.AlignCenter) # align it in the center                                  

        self.Temperature = QLabel(self)              # Make the Temperature label                             
        self.Temperature.setText("Temperature")      # Set the text                                         
        self.Temperature.setFont(LABELFONT1)         # Set the font for the label                           
        self.Temperature.setAlignment(Qt.AlignCenter)# This will align it to the center                     
        self.T_amount = QLabel(self)                 # Make the Temperature amount label                      
        self.T_amount.setText("75 F")                # set the text (this should implement a variable later)
        self.T_amount.setFont(LABELFONT2)            # set the font                                          
        self.T_amount.setAlignment(Qt.AlignCenter)   # align it in the center                                

        self.Humidity = QLabel(self)              # Make the Humidity label                             
        self.Humidity.setText("Humidity")         # Set the text                                          
        self.Humidity.setFont(LABELFONT1)         # Set the font for the label                           
        self.Humidity.setAlignment(Qt.AlignCenter)# This will align it to the center                     
        self.H_amount = QLabel(self)              # Make the Humidity amount label                      
        self.H_amount.setText("%50")              # set the text (this should implement a variable later)
        self.H_amount.setFont(LABELFONT2)         # set the font                                          
        self.H_amount.setAlignment(Qt.AlignCenter)# align it in the center                               

        self.Pressure = QLabel(self)              # Make the Pressure label                             
        self.Pressure.setText("Pressure")         # Set the text                                         
        self.Pressure.setFont(LABELFONT1)         # Set the font for the label                           
        self.Pressure.setAlignment(Qt.AlignCenter)# This will align it to the center                     
        self.P_amount = QLabel(self)              # Make the Pressure amount label                      
        self.P_amount.setText("80 PSI")           # set the text (this should implement a variable later) 
        self.P_amount.setFont(LABELFONT2)         # set the font                                          
        self.P_amount.setAlignment(Qt.AlignCenter)# align it in the center                               

        tabs = QVBoxLayout()    # Make the layout for the tabs
        labels = QVBoxLayout()  # Make the layout for the labels, this will hold the layouts for each set of labels as it will better space them
        resLab = QVBoxLayout()  # Make the layout for the Reservoir
        temLab = QVBoxLayout()  # Make the layout for the Temperature
        humLab = QVBoxLayout()  # Make the layout for the Humidity
        presLab = QVBoxLayout() # Make the layout for the Pressure
        
        columns = QHBoxLayout() # This will be the main layout
        columns.setContentsMargins(0,0,0,0)  # This will remove the margin around the layouts, making the tabs reach the edge of the screen.
        labels.setSpacing(60)                # This sets the spacing betweent the groups of labels, example: both reservoir labels will be close
                                             # while the space between the reservoir labels and the temperature lebels will be 60
        labels.setAlignment(Qt.AlignVCenter) # Further align all the labels in the center

        resLab.addWidget(self.Reservoir) # Add the reservoir label to the reservoir layout  
        resLab.addWidget(self.R_amount)  # Add the reservoir amount to the reservoir layout

        temLab.addWidget(self.Temperature) # Add the temperature label to the temperature layout
        temLab.addWidget(self.T_amount)    # Add the temperature amount to the temperature layout

        humLab.addWidget(self.Humidity) # Add the humidity label to the humidity layout
        humLab.addWidget(self.H_amount) # Add the humidity amount to the humidity layout

        presLab.addWidget(self.Pressure) # Add the pressure label to the pressure layout
        presLab.addWidget(self.P_amount) # Add the pressure amount to the pressure layout

        # Add all the label layouts to the main label layouts, this is done so they are grouped together nicely and easier to manage
        labels.addItem(resLab) 
        labels.addItem(temLab) 
        labels.addItem(humLab) 
        labels.addItem(presLab)
        
        # Add the tabs to the tabs layout
        tabs.addWidget(parent.Home)
        tabs.addWidget(parent.Misting)
        tabs.addWidget(parent.Lighting)
        tabs.addWidget(parent.Nutrients)
        
        # Add the tabs and labels to the main layout
        columns.addItem(tabs)
        columns.addItem(labels)

        # set the windows main layout
        self.setLayout(columns)

        # make the screen maximized when it starts
        self.showMaximized()
