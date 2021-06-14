from mistingScreen import MININTERVAL
from lightingScreen import BUTTONSTYLE
import sys  # to get the screen size and close the window
from PyQt5.QtCore import QSize, Qt, qSetFieldWidth     # all the pyqt5 libraries we need
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from OpButton import OpButton
import json

SIZE = (480, 800)

FONT = "Cambria"

BUTTONFONT = QFont(FONT, (int(SIZE[0]/12))) # font for the tabs
LABELFONT1 = QFont(FONT, (int(SIZE[0]/16))) # font for the bigger labels (reservoir, temperature)
LABELFONT2 = QFont(FONT, (int(SIZE[0]/19))) # font for the readings for the labels (60%)
# WB = 500 # Width buffer for the tabs
# HB = -65 # Hight buffer for the tabs
BUTTONSTYLE = "font: bold; background-color: white; border: none; border-radius: 40px; color: rgb(107,138,116)" # rgb(93,173,236)
MINNUTR = 0
MAXNUTR = 1500
INTERVAL = 25

def setButton(button, text, func):
    button.setStyleSheet(BUTTONSTYLE)
    button.setFont(BUTTONFONT)
    button.setText(text)
    button.clicked.connect(func)
    button.setFixedSize(100, 100)                                                     # this will set the size of the button     
    button.animation.stop()
    button.animation.start()
    button.animation.setDuration(250)

class nutrientScreen(QWidget):
    def __init__(self, parent):
        super(nutrientScreen, self).__init__(parent)
        # self.BWIDTH = BWIDTH
        # self.BHEIGHT = BHIGHT
        # self.lastValue = 0
        self.par = parent
        self.nutrAmount = parent.NutrAmt
        self.initUI(parent)
        self.temp_nutrients = 0

    def initUI(self, parent): # initUI function will set up all the labels and buttons we want for the ui                     

        self.Nutr = QLabel(self)              # Make the Reservoir label                             
        self.Nutr.setText("Nutrients:")        # Set the text                                         
        self.Nutr.setFont(LABELFONT1)         # Set the font for the label                           
        self.Nutr.setAlignment(Qt.AlignCenter)# This will align it to the center
        self.Nutr.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.Nutr.setStyleSheet("font: bold; color: white")                    

        self.amount = QLabel(self)
        self.amount.setText(str(self.nutrAmount) + " ppm")
        self.amount.setFont(LABELFONT2)
        self.amount.setAlignment(Qt.AlignCenter)
        self.amount.setStyleSheet("font: bold; color: white")

        self.increment = OpButton()
        setButton(self.increment, "+", self.inc)

        self.decrement = OpButton()
        setButton(self.decrement, "-", self.dec)

        self.slider = QSlider(orientation=Qt.Horizontal)
        self.slider.setFixedWidth((int(SIZE[1]/2)))
        self.slider.setFixedHeight(100)
        self.slider.setStyleSheet("""QSlider::groove:horizontal {
                                            border: 0px solid #bbb;
                                            background: white;
                                            height: 30px;
                                            border-radius: 15px;
                                        }
                                            QSlider::handle:horizontal {
                                            background: rgb(107,138,116);
                                            border: 5px solid #fff;
                                            width: 70px;
                                            margin-top: -20px;
                                            margin-bottom: -20px;
                                            border-radius: 35px;
                                        }
                                    """)
        
        self.slider.setMinimum(MINNUTR)
        self.slider.setMaximum(MAXNUTR/INTERVAL)
        self.slider.setValue(int(self.nutrAmount / (int(INTERVAL))))
        self.slider.valueChanged.connect(self.slide)
    

        tabs = QVBoxLayout()    # Make the layout for the tabs
        labels = QVBoxLayout()  # Make the layout for the labels, this will hold the layouts for each set of labels as it will better space them
        nutrLay = QVBoxLayout()  # Make the layout for the Reservoir
        nutrBtn = QHBoxLayout()  # Make the layout for the Temperature
        slideLay = QHBoxLayout()
        
        columns = QHBoxLayout() # This will be the main layout
        columns.setContentsMargins(0,0,0,0)  # This will remove the margin around the layouts, making the tabs reach the edge of the screen.
        labels.setSpacing(60)                # This sets the spacing betweent the groups of labels, example: both reservoir labels will be close
                                             # while the space between the reservoir labels and the temperature lebels will be 60
        labels.setAlignment(Qt.AlignVCenter) # Further align all the labels in the center

        nutrLay.addWidget(self.Nutr) # Add the reservoir label to the reservoir layout  
        nutrLay.addWidget(self.amount)  # Add the reservoir amount to the reservoir layout
        
        nutrBtn.addWidget(self.decrement)
        nutrBtn.addWidget(self.increment)

        slideLay.addWidget(self.slider)

        # Add all the label layouts to the main label layouts, this is done so they are grouped together nicely and easier to manage
        labels.addItem(nutrLay) 
        labels.addItem(nutrBtn)
        labels.addItem(slideLay)
        
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

    def inc(self):
        self.increment.animation.stop()
        self.increment.animation.start()
        if (self.nutrAmount < MAXNUTR):
            self.nutrAmount = self.nutrAmount + INTERVAL
            self.par.NutrAmt = self.nutrAmount
        self.slider.setValue(int(self.nutrAmount / (int(INTERVAL))))

        self.amount.setText(str(self.nutrAmount) + " ppm")
        self.updateVariables(self.nutrAmount)

    def dec(self):
        self.decrement.animation.stop()
        self.decrement.animation.start()
        if (self.nutrAmount > MINNUTR):
            self.nutrAmount = self.nutrAmount - INTERVAL
            self.par.NutrAmt = self.nutrAmount
        self.slider.setValue(int(self.nutrAmount / (int(INTERVAL))))

        self.amount.setText(str(self.nutrAmount) + " ppm")
        self.updateVariables(self.nutrAmount)
    
    def slide(self, value):
        
        self.nutrAmount = value * INTERVAL
        self.par.NutrAmt = self.nutrAmount
        self.amount.setText(str(self.nutrAmount) + " ppm")
        self.updateVariables(self.nutrAmount)

    def updateVariables(self, value):
        if self.temp_nutrients == value:
            with open("data.json", "r") as data:
                json_data = data.read()
                json_data = json.loads(json_data)
            with open("data.json", "w") as data:
                json_data["nutrient_screen"]["ppm"] = value
                data.write(json.dumps(json_data))
        else:
            self.temp_nutrients = value

        
