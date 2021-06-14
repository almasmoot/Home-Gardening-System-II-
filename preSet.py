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
BUTTONSTYLE = "font: bold; color: rgb(107,138,116); background-color: white; border: none; border-radius: 30px" # rgb(93,173,236)
BUTTONSTYLE2 = "font: bold; color: rgb(107,138,116); background-color: white; border: none; border-radius: 25px" # rgb(93,173,236)

STYLE = "font: bold; color: white;"

NUMLABELS = 4

def setButton(button, text, func, width, height, style, font):
    button.setStyleSheet(style)
    button.setFont(font)
    button.setText(text)
    button.clicked.connect(func)
    button.setFixedSize(width, height)                                                  # this will set the size of the button     
    button.animation.stop()
    button.animation.start()
    button.animation.setDuration(250)

def makeLabel(label, text, font, style):
    label.setText(text)        # Set the text                                         
    label.setFont(font)         # Set the font for the label                           
    label.setAlignment(Qt.AlignCenter)# This will align it to the center    
    label.setStyleSheet(style)  # Set the style of the label
    label.setFixedHeight(100)

class preSet(QScrollArea):
    def __init__(self, parent, *args, **kwargs):
        super(preSet, self).__init__(parent)
        QScrollArea.__init__(self, *args, **kwargs)
        
        self.par = parent
        self.FILE = "cold.csv"
        self.initUI(parent)

    def initUI(self, parent): # initUI function will set up all the labels and buttons we want for the ui

        columns = QHBoxLayout() # This will be the main layout
        tabs = QVBoxLayout()    # Make the layout for the tabs
        labels = QVBoxLayout()  # Make the layout for the labels, this will hold the layouts for each set of labels as it will better space them

        plantBtn = QHBoxLayout()
        self.plantLst = QListWidget()  # list of plants
        listLay = QVBoxLayout()
        scrollBar = QScrollBar()

        ## -- KEEP --
        ## This will initialize the text box and text layout
        # textBox = QLineEdit()
        # textLay = QHBoxLayout()

        ## -- KEEP --
        ## text submit button is the button that will add current text in the text box to the current csv file
        # self.textSubmit = OpButton()
        # setButton(self.textSubmit, "Add", self.addPlant, 100, 50, BUTTONSTYLE2, LABELFONT2)

        self.cold = OpButton()
        setButton(self.cold, "Cold", self.coldP, 200, 120, BUTTONSTYLE, BUTTONFONT)

        self.warm = OpButton()
        setButton(self.warm, "Warm", self.warmP, 200, 120, BUTTONSTYLE, BUTTONFONT)

        self.hot = OpButton()
        setButton(self.hot, "Hot", self.hotP, 200, 120, BUTTONSTYLE, BUTTONFONT)

        ## -- KEEP --
        ## This is the text box that in theory will allow the user to add a plant to the list
        # textBox.setStyleSheet("background-color: white; border-radius: 25px")
        # textBox.setFixedSize(400, 50)
        # textBox.setFont(LABELFONT2)
        
        listLay.setContentsMargins(50, 20, 50, 20) # left top right bottom
        scrollBar.setMinimum(0)
        scrollBar.setMaximum(2000)
        scrollBar.setStyleSheet("QScrollBar:vertical { border: 5px solid white; width: 80px; margin: 15px 15px 15px 15px; border-radius: 15px;} "
                                 + "QScrollBar::handle:vertical {background-color: rgb(107,138,116); border-radius: 20px;}"
                                + " QScrollBar::sub-line:vertical {width: 0px; height: 0px;}"
                                + " QScrollBar::add-line:vertical {width: 0px; height: 0px;}")
        self.plantLst.setVerticalScrollBar(scrollBar)
        self.plantLst.setStyleSheet("background-color: white; border-radius: 25px;")
        

        with open("cold.csv", "r") as f:
            self.plants = f.readlines()
            self.numPlants = []
            for line in range(0, len(self.plants)):
                text = self.plants[line].replace(',', '')
                item = QListWidgetItem(text)
                item.setFont(LABELFONT2)
                item.setTextAlignment(Qt.AlignCenter)
                self.plantLst.addItem(item)

        plantBtn.addWidget(self.cold)
        plantBtn.addWidget(self.warm)
        plantBtn.addWidget(self.hot)
        plantBtn.setAlignment(Qt.AlignCenter)
        plantBtn.setContentsMargins(0, 10, 0, 0)
        plantBtn.setSpacing(15)
        
        ## -- KEEP --
        ## this will set up and add the text box and add button to the text layout to be added to the preset ui
        # textLay.setSpacing(20)
        # textLay.addWidget(textBox)
        # textLay.addWidget(self.textSubmit)
        # textLay.setAlignment(Qt.AlignCenter)
        # textLay.setContentsMargins(0, 0, 0, 10)

        listLay.addWidget(self.plantLst)

        labels.setAlignment(Qt.AlignVCenter) # Further align all the labels in the center
        labels.addItem(plantBtn)
        labels.addItem(listLay)
        # labels.addItem(textLay) # uncomment this to add the text box and the add button layout to the ui
        
        # Add the tabs to the tabs layout
        tabs.addWidget(parent.Home)
        tabs.addWidget(parent.Misting)
        tabs.addWidget(parent.Lighting)
        tabs.addWidget(parent.Nutrients)
        tabs.addWidget(parent.preSet)
        
        # Add the tabs and labels to the main layout
        columns.setContentsMargins(0,0,0,0)  # This will remove the margin around the layouts, making the tabs reach the edge of the screen.
                                             # while the space between the reservoir labels and the temperature lebels will be 60
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

        self.setList("hot.csv")

    # When a plant in the list is cliked on
    # def plantSelect(self):
    #     pass

    # Add plant function should add the text from the text box to the current csv file
    # current problem is that there is no key board for the user to use.
    # def addPlant(self):
    #     self.textSubmit.animation.stop()
    #     self.textSubmit.animation.start()

    def setList(self, file):
        self.FILE = file
        self.plantLst.clear()
        with open(file, "r") as f:
            self.plants = f.readlines()
            self.numPlants = []
            for line in range(0, len(self.plants)):
                text = self.plants[line].replace(',', '')
                item = QListWidgetItem(text)
                item.setFont(LABELFONT2)
                item.setTextAlignment(Qt.AlignCenter)
                self.plantLst.addItem(item)