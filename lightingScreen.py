from OpButton import OpButton
from PyQt5.QtCore import Qt     # all the pyqt5 libraries we need
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

SIZE = (480, 800)

FONT = "Cambria"

BUTTONFONT = QFont(FONT, (int(SIZE[0]/12))) # font for the tabs
LABELFONT1 = QFont(FONT, (int(SIZE[0]/20))) # font for the bigger labels (reservoir, temperature)
LABELFONT2 = QFont(FONT, (int(SIZE[0]/25))) # font for the readings for the labels (60%)
MINTIME = 6
MAXTIME = 9

BUTTONSTYLE = "font: bold; color: rgb(107,138,116); background-color: white; border: none; border-radius: 40px" # rgb(93,173,236)

def setButton(button, text, func):
    button.setStyleSheet(BUTTONSTYLE)
    button.setFont(BUTTONFONT)
    button.setText(text)
    button.clicked.connect(func)
    button.setFixedSize(100, 100)                                                     # this will set the size of the button     
    button.animation.stop()
    button.animation.start()
    button.animation.setDuration(250)

class lighingScreen(QWidget):
    def __init__(self, parent):
        super(lighingScreen, self).__init__(parent)
        self.par = parent
        self.startTime = parent.StartTime
        self.endTime = parent.EndTime
        self.duration = self.endTime - self.startTime

        self.initUI(parent)

    def initUI(self, parent): # initUI function will set up all the labels and buttons we want for the ui                     

        self.label1 = QLabel(self)                    # Make the current misting label label                             
        self.label1.setText("Light duration")         # Set the text                                         
        self.label1.setFont(LABELFONT1)               # Set the font for the label                           
        self.label1.setAlignment(Qt.AlignCenter)      # This will align it to the center                        
        self.label1.setMinimumWidth((int(SIZE[1]/1.16)))             # This was added to set the width so the tabs stay in place, the number set will need to be changed according to screen used
        self.label1.setStyleSheet("font: bold; color: white")
        
        self.label2 = QLabel(self)                                      # Make the Reservoir amount label                      
        self.label2.setText(str(self.duration) + " hours")              # set the text (this should implement a variable later)
        self.label2.setFont(LABELFONT2)                                 # set the font                                          
        self.label2.setAlignment(Qt.AlignCenter)                        # align it in the center
        self.label2.setStyleSheet("font: bold; color: white")

        self.startLabel = QLabel(self)
        self.startLabel.setText("Start time: " + str(self.startTime) + ":00 am")
        self.startLabel.setFont(LABELFONT2)
        self.startLabel.setStyleSheet("font: bold; color: white")
        self.startLabel.setAlignment(Qt.AlignHCenter)

        self.endLabel = QLabel(self)
        self.endLabel.setText("End time: " + str(12 if(self.endTime == 12) else self.endTime % 12) + ":00 pm")
        self.endLabel.setFont(LABELFONT2)
        self.endLabel.setStyleSheet("font: bold; color: white")
        self.endLabel.setAlignment(Qt.AlignHCenter)  

        self.increaseStart = OpButton(self)
        setButton(self.increaseStart, "+", self.incStart)

        self.decreaseStart = OpButton(self)
        setButton(self.decreaseStart, "-", self.decStart)

        self.increaseEnd = OpButton(self)
        setButton(self.increaseEnd, "+", self.incEnd)

        self.decreaseEnd = OpButton(self)
        setButton(self.decreaseEnd, "-", self.decEnd)                   

        tabs = QVBoxLayout()    # Make the layout for the tabs
        labels = QVBoxLayout()  # Make the layout for the labels, this will hold the layouts for each set of labels as it will better space them
        duration = QVBoxLayout()  # Make the layout for the Reservoir
        timing = QHBoxLayout()  # Make the layout for the Temperature
        buttonsStart = QHBoxLayout()  # Make the layout for the Humidity
        buttonsEnd = QHBoxLayout() # Make the layout for the Pressure
        buttons = QHBoxLayout()
        
        columns = QHBoxLayout() # This will be the main layout
        columns.setContentsMargins(0,0,0,0)  # This will remove the margin around the layouts, making the tabs reach the edge of the screen.
        labels.setSpacing(60)                # This sets the spacing betweent the groups of labels, example: both reservoir labels will be close
                                             # while the space between the reservoir labels and the temperature lebels will be 60
        labels.setAlignment(Qt.AlignVCenter) # Further align all the labels in the center

        duration.addWidget(self.label1) # Add the reservoir label to the reservoir layout  
        duration.addWidget(self.label2)  # Add the reservoir amount to the reservoir layout

        timing.addWidget(self.startLabel) # Add the temperature label to the temperature layout
        timing.addWidget(self.endLabel)    # Add the temperature amount to the temperature layout

        buttonsStart.addWidget(self.decreaseStart) # Add the humidity label to the humidity layout
        buttonsStart.addWidget(self.increaseStart) # Add the humidity amount to the humidity layout
        buttonsStart.setSpacing((int(SIZE[0]/19.2)))

        buttonsEnd.addWidget(self.decreaseEnd) # Add the pressure label to the pressure layout
        buttonsEnd.addWidget(self.increaseEnd) # Add the pressure amount to the pressure layout
        buttonsEnd.setSpacing((int(SIZE[0]/19.2)))

        buttons.addItem(buttonsStart)
        buttons.addItem(buttonsEnd)
        buttons.setSpacing((int(SIZE[0]/9.6)))

        # Add all the label layouts to the main label layouts, this is done so they are grouped together nicely and easier to manage
        labels.addItem(duration) 
        labels.addItem(timing) 
        labels.addItem(buttons) 
        # labels.addItem(buttonsEnd)
        
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

    def incStart(self):
        self.increaseStart.animation.stop()
        self.increaseStart.animation.start()
        if (self.startTime + 1 <= MAXTIME):
            self.startTime = (self.startTime + 1)
            self.par.StartTime = self.startTime
        self.duration = self.endTime - self.startTime
        self.label2.setText(str(self.duration) + " hours")
        self.startLabel.setText("Start time: " + str(self.startTime) + ":00 am")

    def decStart(self):
        self.decreaseStart.animation.stop()
        self.decreaseStart.animation.start()
        if (self.startTime - 1 >= MINTIME):
            self.startTime = (self.startTime - 1)
            self.par.StartTime = self.startTime
        self.duration = self.endTime - self.startTime
        self.label2.setText(str(self.duration) + " hours")
        self.startLabel.setText("Start time: " + str(self.startTime) + ":00 am")

    def incEnd(self):
        self.increaseEnd.animation.stop()
        self.increaseEnd.animation.start()
        if (((self.endTime + 1) % 12) <= MAXTIME):
            self.endTime = (self.endTime + 1)
            self.par.EndTime = self.endTime
        self.duration = self.endTime - self.startTime
        self.label2.setText(str(self.duration) + " hours")
        self.endLabel.setText("End time: " + str(12 if(self.endTime == 12) else self.endTime % 12) + ":00 pm")

    def decEnd(self):
        self.decreaseEnd.animation.stop()
        self.decreaseEnd.animation.start()
        if (((self.endTime - 1) % 12) >= MINTIME):
            self.endTime = (self.endTime - 1)
            self.par.EndTime = self.endTime
        self.duration = self.endTime - self.startTime
        self.label2.setText(str(self.duration) + " hours")
        self.endLabel.setText("End time: " + str(12 if(self.endTime == 12) else self.endTime % 12) + ":00 pm")