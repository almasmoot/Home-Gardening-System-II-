import sys  # to get the screen size and close the window
from PyQt5.QtCore import Qt     # all the pyqt5 libraries we need
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

BUTTONFONT = QFont("times", 30) # font for the tabs
LABELFONT1 = QFont("times", 60) # font for the bigger labels (reservoir, temperature)
LABELFONT2 = QFont("times", 30) # font for the readings for the labels (60%)
WB = 500 # Width buffer for the tabs
HB = -65 # Hight buffer for the tabs
MINNUTR = 0
MAXNUTR = 1500
INTERVAL = 25

class nutrientScreen(QWidget):
    def __init__(self, parent):
        super(nutrientScreen, self).__init__(parent)
        # self.BWIDTH = BWIDTH
        # self.BHEIGHT = BHIGHT
        self.nutrAmount = 300
        self.initUI(parent)

    def initUI(self, parent): # initUI function will set up all the labels and buttons we want for the ui                     

        self.Nutr = QLabel(self)              # Make the Reservoir label                             
        self.Nutr.setText("Nutrients:")        # Set the text                                         
        self.Nutr.setFont(LABELFONT1)         # Set the font for the label                           
        self.Nutr.setAlignment(Qt.AlignCenter)# This will align it to the center                             

        self.amount = QLabel(self)
        self.amount.setText(str(self.nutrAmount) + " ppm")
        self.amount.setFont(LABELFONT2)
        self.amount.setAlignment(Qt.AlignCenter)             

        tabs = QVBoxLayout()    # Make the layout for the tabs
        labels = QVBoxLayout()  # Make the layout for the labels, this will hold the layouts for each set of labels as it will better space them
        nutrLay = QVBoxLayout()  # Make the layout for the Reservoir
        # temLab = QVBoxLayout()  # Make the layout for the Temperature
        # humLab = QVBoxLayout()  # Make the layout for the Humidity
        # presLab = QVBoxLayout() # Make the layout for the Pressure
        
        columns = QHBoxLayout() # This will be the main layout
        columns.setContentsMargins(0,0,0,0)  # This will remove the margin around the layouts, making the tabs reach the edge of the screen.
        labels.setSpacing(60)                # This sets the spacing betweent the groups of labels, example: both reservoir labels will be close
                                             # while the space between the reservoir labels and the temperature lebels will be 60
        labels.setAlignment(Qt.AlignVCenter) # Further align all the labels in the center

        nutrLay.addWidget(self.Nutr) # Add the reservoir label to the reservoir layout  
        nutrLay.addWidget(self.amount)  # Add the reservoir amount to the reservoir layout

        # temLab.addWidget(self.Temperature) # Add the temperature label to the temperature layout
        # temLab.addWidget(self.T_amount)    # Add the temperature amount to the temperature layout

        # humLab.addWidget(self.Humidity) # Add the humidity label to the humidity layout
        # humLab.addWidget(self.H_amount) # Add the humidity amount to the humidity layout

        # presLab.addWidget(self.Pressure) # Add the pressure label to the pressure layout
        # presLab.addWidget(self.P_amount) # Add the pressure amount to the pressure layout

        # Add all the label layouts to the main label layouts, this is done so they are grouped together nicely and easier to manage
        labels.addItem(nutrLay) 
        # labels.addItem(temLab) 
        # labels.addItem(humLab) 
        # labels.addItem(presLab)
        
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
