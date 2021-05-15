import sys  # to get the screen size and close the window
from PyQt5.QtCore import Qt     # all the pyqt5 libraries we need
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

BUTTONFONT = QFont("times", 40) # font for the tabs
LABELFONT1 = QFont("times", 60) # font for the bigger labels (reservoir, temperature)
LABELFONT2 = QFont("times", 50) # font for the readings for the labels (60%)

class mistingScreen(QWidget):  # this is the class that will have all the fucntions, labels and a buttons for the misting screen
    def __init__(self, parent):   # initialize function
        super(mistingScreen, self).__init__(parent)
        self.interval = 10  # interval variable in minutes
        self.initUI(parent)  # initalize the ui

    def initUI(self, parent): # initUI function will set up all the labels and buttons we want for the ui                     

        self.label1 = QLabel(self)                          # Make the current misting label label                             
        self.label1.setText("Current misting interval")     # Set the text                                         
        self.label1.setFont(LABELFONT1)                     # Set the font for the label                           
        self.label1.setAlignment(Qt.AlignCenter)            # This will align it to the center                        
        self.label1.setMinimumWidth(1610)                   # This was added to set the width so the tabs stay in place, the number set will need to be changed according to screen used
        
        self.label2 = QLabel(self)                                      # Make the Reservoir amount label                      
        self.label2.setText("every " + str(self.interval) + " minutes") # set the text (this should implement a variable later)
        self.label2.setFont(LABELFONT2)                                 # set the font                                          
        self.label2.setAlignment(Qt.AlignCenter)                        # align it in the center 

        self.increase = QPushButton()                                                            # this will make a push button                                  
        self.increase.setStyleSheet("background-color: blue; border: none; border-radius: 40px") # this will set the style, blue, no border and round the edges          
        self.increase.setFont(LABELFONT1)                                                        # this will set the font for the increase button               
        self.increase.setText("+")                                                               # this will set the text to "+"                                  
        self.increase.clicked.connect(self.inc)                                                  # this will set the funtion for increase button                     
        self.increase.setFixedSize(200, 200)                                                     # this will set the size of the button                          

        self.decrease = QPushButton()                                                            # this will make a push button                                   
        self.decrease.setStyleSheet("background-color: blue; border: none; border-radius: 40px") # this will set the style, blue, no border and round the edges          
        self.decrease.setFont(LABELFONT1)                                                        # this will set the font for the decrease button                 
        self.decrease.setText("-")                                                               # this will set the text to "-"                                      
        self.decrease.clicked.connect(self.dec)                                                  # this will set the funtion for decrease button                      
        self.decrease.setFixedSize(200, 200)                                                     # this will set the size of the button                                                         

        tabs = QVBoxLayout()    # Make the layout for the tabs
        labels = QVBoxLayout()  # Make the layout for the labels, this will hold the layouts for each set of labels as it will better space them
        intervalLab = QVBoxLayout()  # Make the layout for the interval labels
        intButtonsLab = QHBoxLayout()  # Make the layout for the interval button labels

        columns = QHBoxLayout() # This will be the main layout
        columns.setContentsMargins(0,0,0,0)  # This will remove the margin around the layouts, making the tabs reach the edge of the screen.
        labels.setSpacing(150)                # This sets the spacing betweent the groups of labels, example: both reservoir labels will be close
                                             # while the space between the reservoir labels and the temperature lebels will be 60
        labels.setAlignment(Qt.AlignVCenter) # Further align all the labels in the center

        intervalLab.addWidget(self.label1) # Add the current misting interval labal to the layout 
        intervalLab.addWidget(self.label2)  # Add the actual interval number to the layout

        intButtonsLab.addWidget(self.decrease) # Add the decrease button to the layout
        intButtonsLab.addWidget(self.increase)    # Add the increase button to the layout

        # Add all the label layouts to the main label layouts, this is done so they are grouped together nicely and easier to manage
        labels.addItem(intervalLab) 
        labels.addItem(intButtonsLab)
        
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

    # increment the interval, this funtion will increase the misting interval by 1, (in minutes)
    def inc(self):
        self.interval = self.interval + 1
        self.label2.setText("every " + str(self.interval) + " minutes")

    # decrement the interval, this funtion will decrease the misting interval by 1, (in minutes)
    def dec(self):
        self.interval = self.interval - 1
        self.label2.setText("every " + str(self.interval) + " minutes")