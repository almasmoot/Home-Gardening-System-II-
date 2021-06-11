import sys
from types import CodeType
from typing import List
from OpButton import OpButton
from PyQt5.QtCore import QSize, Qt, QTimer     # all the pyqt5 libraries we need
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import csv
from generate_test_json import generate_new_data
import json

SIZE = (480, 800)

FONT = "Cambria" # font for the text

BUTTONFONT = (QFont(FONT, (int(SIZE[0]/16)))) # font for the tabs
LABELFONT1 = (QFont(FONT, (int(SIZE[0]/16)))) # font for the bigger labels (reservoir, temperature)
LABELFONT2 = (QFont(FONT, (int(SIZE[0]/32)))) # font for the readings for the labels (60%)
BUTTONSTYLE = "font: bold; color: rgb(107,138,116); background-color: white; border: none; border-radius: 40px" # rgb(93,173,236)

STYLE = "font: bold; color: white;"

def setButton(button, text, func, width, height):
    button.setStyleSheet(BUTTONSTYLE)
    button.setFont(BUTTONFONT)
    button.setText(text)
    button.clicked.connect(func)
    button.setFixedSize(width, height)                                                  # this will set the size of the button     
    button.animation.stop()
    button.animation.start()
    button.animation.setDuration(250)

def makeLabel(label, text, font, style):
    label.setText(text)        # Set the text                                         
    label.setFont(font)         # Set the font for the label                           
    # label.setAlignment(Qt.AlignCenter)# This will align it to the center    
    label.setStyleSheet(style)  # Set the style of the label

class preSet(QScrollArea):
    def __init__(self, parent, *args, **kwargs):
        super(preSet, self).__init__(parent)
        QScrollArea.__init__(self, *args, **kwargs)

        # self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        
        # content = QWidget(self)
        # self.setWidget(content)
        
        self.par = parent
        self.FILE = "cold.csv"
        self.initUI(parent)

    def initUI(self, parent): # initUI function will set up all the labels and buttons we want for the ui                     

        self.cold = OpButton()
        setButton(self.cold, "Cold", self.coldP, 200, 120)

        self.warm = OpButton()
        setButton(self.warm, "Warm", self.warmP, 200, 120)

        self.hot = OpButton()
        setButton(self.hot, "Hot", self.hotP, 200, 120)
        
        columns = QHBoxLayout() # This will be the main layout
        # self.container = QWidget(self)c
        # self.container.setStyleSheet("background-color: blue")
        # self.container.setGeometry(200, 150, 550, 300)
        tabs = QVBoxLayout()    # Make the layout for the tabs
        labels = QVBoxLayout()  # Make the layout for the labels, this will hold the layouts for each set of labels as it will better space them
        textBox = QLineEdit()
        textBox.setStyleSheet("background-color: white; border-radius: 4px")
        textBox.setFixedSize(400, 60)
        textBox.setFont(LABELFONT1)
        textSubmit = OpButton()
        setButton(textSubmit, "Add", self.addPlant, 100, 60)
        textLay = QHBoxLayout()
        textLay.setSpacing(20)
        plantLst = QListWidget()  # Make the layout for the Reservoir
        # plantLst.setGeometry(220, 180, 540, 220)
        listLay = QVBoxLayout()
        listLay.setContentsMargins(50, 50, 50, 50)
        # plantLst.setTextA(Qt.AlignCenter)
        scrollBar = QScrollBar()
        scrollBar.setStyleSheet("QScrollBar:vertical {width: 30px; margin: 5px 3px 5px 3px; border: 1px #2A2929; border-radius: 4px; background-color: blue solid;} QScrollBar::handle:vertical {max-height: 15px; background-color: green; border-radius: 3px;} QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {background: none;}")
        plantLst.setVerticalScrollBar(scrollBar)
        plantLst.setStyleSheet("background-color: white")
        # plantLst.setSpacing(10)

        # plantLst.setAlignment(Qt.AlignCenter)
        # plantLst.setGeometry(0, 0, 50, 50)
        plantBtn = QHBoxLayout()
        # sliderLay = QHBoxLayout()
        # self.scroller = QScrollArea()
        

        with open("cold.csv", "r") as f:
            # reader = csv.reader(f)
            # self.plants = list(reader)
            self.plants = f.readlines()
            self.numPlants = []
            for line in range(0, len(self.plants)):
                text = self.plants[line].replace(',', '')
                item = QListWidgetItem(text)
                item.setFont(LABELFONT1)
                item.setTextAlignment(Qt.AlignCenter)
                # self.numPlants.append(QLabel())
                # self.numPlants[line].se
                # self.plants[line] = QLabel(self)
                # makeLabel(self.numPlants[line], text, LABELFONT1, STYLE)
                plantLst.addItem(item)
                # self.numPlants[line].move(0, 70)


        # self.container.setLayout(plantBtn)
        # self.scroller.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        # # self.scroller.setWidgetResizable(True)
        # self.scroller.setWidget(self.container)
        
        # these will allow for the labels to be in four corners instead of stacked
        # row1 = QHBoxLayout()    
        # row2 = QHBoxLayout()    
        self.slider = QSlider(orientation=Qt.Vertical)
        self.slider.setFixedWidth(40)
        self.slider.setFixedHeight(200)
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
        
        self.slider.setMinimum(0)
        self.slider.setMaximum(50)
        # self.slider.setValue(int(self.nutrAmount / (int(INTERVAL))))
        self.slider.valueChanged.connect(self.slide)

        # sliderLay.addWidget(self.slider)
        # sliderLay.setAlignment(Qt.AlignVCenter)
        # sliderLay2 = QVBoxLayout()
        # sliderLay2.addItem(sliderLay)
        # sliderLay2.setAlignment(Qt.AlignRight)

        plantBtn.addWidget(self.cold)
        plantBtn.addWidget(self.warm)
        plantBtn.addWidget(self.hot)
        plantBtn.setAlignment(Qt.AlignTop)
        plantBtn.setSpacing(15)
        
        
        columns.setContentsMargins(0,0,0,0)  # This will remove the margin around the layouts, making the tabs reach the edge of the screen.
        # labels.setSpacing(int(SIZE[1]/6.4))                # This sets the spacing betweent the groups of labels, example: both reservoir labels will be close
                                             # while the space between the reservoir labels and the temperature lebels will be 60
        labels.setAlignment(Qt.AlignTop) # Further align all the labels in the center
        # labels.setSpacing()

        # add the labels to the rows they will be in
        # content.setLayout(plantLst)
        # spacer = QSpacerItem(300, 350, QSizePolicy.Minimum, QSizePolicy.Minimum)
        textLay.addWidget(textBox)
        textLay.addWidget(textSubmit)
        textLay.setAlignment(Qt.AlignCenter)
        listLay.addWidget(plantLst)
        labels.addItem(plantBtn)
        labels.addItem(listLay)
        labels.addItem(textLay)
        # labels.addItem()
        # labels.addSpacerItem(spacer)
        # labels.addWidget(content) 
        
        # Add the tabs to the tabs layout
        tabs.addWidget(parent.Home)
        tabs.addWidget(parent.Misting)
        tabs.addWidget(parent.Lighting)
        tabs.addWidget(parent.Nutrients)
        tabs.addWidget(parent.preSet)
        
        # Add the tabs and labels to the main layout
        columns.addItem(tabs)
        columns.addItem(labels)

        # set the windows main layout
        self.setLayout(columns)

        # make the screen maximized when it starts
        self.showMaximized()

    def coldP(self):
        self.cold.animation.stop()
        self.cold.animation.start()

        self.setList("cold.csv")

    def warmP(self):
        self.warm.animation.stop()
        self.warm.animation.start()

        self.setList("warm.csv")

    def hotP(self):
        self.hot.animation.stop()
        self.hot.animation.start()

        self.setList("cold.csv")

    def plantSelect(self):
        pass

    def addPlant(self):
        pass

    def setList(self, file):
        self.FILE = file
        with open(file, "r") as f:
            # reader = csv.reader(f)
            plants = f.readlines()
            for line in range(0, len(self.numPlants)):
                if (line < len(plants)):
                    self.numPlants[line].setText(plants[line].replace(',', ''))
                else:
                    self.numPlants[line].setText("")

    def slide(self, value):
        with open(self.FILE, "r") as f:
            self.plants = f.readlines()
            for line in range(0, len(self.plants)):
                y = self.numPlants[line].y()
                if (value != 0):
                    self.lastValue = value
                    self.numPlants[line].move(0, value + y)
                    print("self.numPlants[{}].move(0, {})".format(line, value))