from homeScreen import STYLE
from PyQt5.QtCore import Qt     # all the pyqt5 libraries we need
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from OpButton import OpButton
import json

SIZE = (480, 800)

FONT = "Cambria"

BUTTONFONT = QFont(FONT, (int(SIZE[0]/12))) # font for the tabs
LABELFONT1 = QFont(FONT, (int(SIZE[0]/16))) # font for the bigger labels (reservoir, temperature)
LABELFONT2 = QFont(FONT, (int(SIZE[0]/19))) # font for the readings for the labels (60%)

MININTERVAL = 2
MAXINTERVAL = 6

BUTTONSTYLE = "font: bold; background-color: white; border: none; border-radius: 40px; color: rgb(107,138,116)" # rgb(93,173,236)
BUTTONSIZE = 100, 100

def setButton(button, text, func):
    button.setStyleSheet(BUTTONSTYLE)
    button.setFont(BUTTONFONT)
    button.setText(text)
    button.clicked.connect(func)
    button.setFixedSize(100, 100)                                                     # this will set the size of the button     
    button.animation.stop()
    button.animation.start()
    button.animation.setDuration(250)

class mistingScreen(QWidget):  # this is the class that will have all the fucntions, labels and a buttons for the misting screen
    def __init__(self, parent):   # initialize function
        super(mistingScreen, self).__init__(parent)
        # self.effect = QGraphicsOpacityEffect(self)
        self.par = parent
        self.intervalmin = parent.MistIntrv  # interval variable in minutes
        self.sec = parent.MistSec
        self.initUI(parent)  # initalize the ui
        self.temp_min = 0
        self.temp_sec = 0

    def initUI(self, parent): # initUI function will set up all the labels and buttons we want for the ui                     

        self.label1 = QLabel(self)                          # Make the current misting label label                             
        self.label1.setText("Current misting interval")     # Set the text                                         
        self.label1.setFont(LABELFONT1)                     # Set the font for the label                           
        self.label1.setAlignment(Qt.AlignCenter)            # This will align it to the center                        
        self.label1.setMinimumWidth((int(SIZE[1]/1.16)))                   # This was added to set the width so the tabs stay in place, the number set will need to be changed according to screen used
        self.label1.setStyleSheet("font: bold; color: white;")
        
        self.label2 = QLabel(self)                                      # Make the Reservoir amount label                      
        self.label2.setText("every " + str(self.intervalmin) + ":" + str('00' if(self.sec == 0) else self.sec) + " minutes") # set the text (this should implement a variable later)
        self.label2.setFont(LABELFONT2)                                 # set the font                                          
        self.label2.setAlignment(Qt.AlignCenter)                        # align it in the center 
        self.label2.setStyleSheet("font: bold; color: white;")

        self.increase = OpButton()                                                            # this will make a push button                     
        setButton(self.increase, "+", self.inc)
    

        self.decrease = OpButton()                                                            # this will make a push button                                                         
        setButton(self.decrease, "-", self.dec)                                                   

        tabs = QVBoxLayout()    # Make the layout for the tabs
        labels = QVBoxLayout()  # Make the layout for the labels, this will hold the layouts for each set of labels as it will better space them
        intervalLab = QVBoxLayout()  # Make the layout for the interval labels
        intButtonsLab = QHBoxLayout()  # Make the layout for the interval button labels

        columns = QHBoxLayout() # This will be the main layout
        columns.setContentsMargins(0,0,0,0)  # This will remove the margin around the layouts, making the tabs reach the edge of the screen.
        labels.setSpacing((int(SIZE[0]/6.4)))                # This sets the spacing betweent the groups of labels, example: both reservoir labels will be close
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
        self.increase.animation.stop()
        self.increase.animation.start()
        
        if (not(self.intervalmin == MAXINTERVAL)):
            self.sec = ((self.sec + 15) % 60)
            self.par.MistSec = self.sec
        if (self.sec % 60 == 0 and self.intervalmin < MAXINTERVAL):
            self.intervalmin = self.intervalmin + 1
            self.par.MistIntrv = self.intervalmin
        self.label2.setText("every " + str(self.intervalmin) + ":" + str('00' if(self.sec == 0) else self.sec) + " minutes")

        self.updateVariables(self.intervalmin, self.sec)
        

    # decrement the interval, this funtion will decrease the misting interval by 1, (in minutes)
    def dec(self):
        self.decrease.animation.stop()
        self.decrease.animation.start()

        if (not(self.intervalmin == MININTERVAL and self.sec == 0)):
            self.sec = ((self.sec - 15) % 60)
            self.par.MistSec = self.sec
        if ((self.sec + 15) % 60 == 0 and self.intervalmin > MININTERVAL):
            self.intervalmin = self.intervalmin - 1
            self.par.MistIntrv = self.intervalmin
        self.label2.setText("every " + str(self.intervalmin) + ":" + str('00' if(self.sec == 0) else self.sec) + " minutes")

        self.updateVariables(self.intervalmin, self.sec)

    def updateVariables(self, value_min, value_sec):
        if self.temp_min == value_min and self.temp_sec == value_sec:
            with open("data.json", "r") as data:
                json_data = data.read()
                json_data = json.loads(json_data)
            with open("data.json", "w") as data:
                json_data["misting_screen"]["duration_min"] = self.intervalmin
                json_data["misting_screen"]["duration_sec"] = self.sec
                data.write(json.dumps(json_data))
        else:
            self.temp_min = value_min
            self.temp_sec = value_sec