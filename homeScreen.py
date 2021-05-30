from PyQt5.QtCore import Qt, QTimer     # all the pyqt5 libraries we need
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from generate_test_json import generate_new_data
import json

SIZE = (480, 800)

FONT = "Cambria" # font for the text

BUTTONFONT = (QFont(FONT, (int(SIZE[0]/16)))) # font for the tabs
LABELFONT1 = (QFont(FONT, (int(SIZE[0]/16)))) # font for the bigger labels (reservoir, temperature)
LABELFONT2 = (QFont(FONT, (int(SIZE[0]/32)))) # font for the readings for the labels (60%)

STYLE = "font: bold; color: white;"

def makeLabel(label, text, font, style):
    label.setText(text)        # Set the text                                         
    label.setFont(font)         # Set the font for the label                           
    label.setAlignment(Qt.AlignCenter)# This will align it to the center    
    label.setStyleSheet(style)  # Set the style of the label

class homeScreen(QWidget):
    def __init__(self, parent):
        super(homeScreen, self).__init__(parent)
        self.par = parent
        self.initUI(parent)

        timer = QTimer(self)

        timer.timeout.connect(self.updateVariables)

        timer.start(1000) # 1 minute = 60000

    def initUI(self, parent): # initUI function will set up all the labels and buttons we want for the ui                     

        self.Reservoir = QLabel(self)              # Make the Reservoir label                             
        makeLabel(self.Reservoir, "Reservoir", LABELFONT1, STYLE)   
        self.R_amount = QLabel(self)               # Make the Reservoir amount label                      
        makeLabel(self.R_amount, (str(parent.ResAmt) + " %"), LABELFONT2, STYLE )                   

        self.Temperature = QLabel(self)              # Make the Temperature label                             
        makeLabel(self.Temperature, "Temperature", LABELFONT1, STYLE)                    
        self.T_amount = QLabel(self)                 # Make the Temperature amount label                      
        makeLabel(self.T_amount, (str(parent.TmpAmt)+ "°F"), LABELFONT2, STYLE)                         

        self.Humidity = QLabel(self)              # Make the Humidity label                             
        makeLabel(self.Humidity, "Humidity", LABELFONT1, STYLE)                    
        self.H_amount = QLabel(self)              # Make the Humidity amount label                      
        makeLabel(self.H_amount, (str(parent.HumAmt) + " %"), LABELFONT2, STYLE)                      

        self.Pressure = QLabel(self)              # Make the Pressure label                             
        makeLabel(self.Pressure, "Pressure", LABELFONT1, STYLE)                     
        self.P_amount = QLabel(self)              # Make the Pressure amount label                      
        makeLabel(self.P_amount, (str(parent.PrsAmt) + " PSI"), LABELFONT2, STYLE)                             

        tabs = QVBoxLayout()    # Make the layout for the tabs
        labels = QVBoxLayout()  # Make the layout for the labels, this will hold the layouts for each set of labels as it will better space them
        resLab = QVBoxLayout()  # Make the layout for the Reservoir
        temLab = QVBoxLayout()  # Make the layout for the Temperature
        humLab = QVBoxLayout()  # Make the layout for the Humidity
        presLab = QVBoxLayout() # Make the layout for the Pressure
        # these will allow for the labels to be in four corners instead of stacked
        row1 = QHBoxLayout()    
        row2 = QHBoxLayout()    
        
        columns = QHBoxLayout() # This will be the main layout
        columns.setContentsMargins(0,0,0,0)  # This will remove the margin around the layouts, making the tabs reach the edge of the screen.
        labels.setSpacing(int(SIZE[1]/6.4))                # This sets the spacing betweent the groups of labels, example: both reservoir labels will be close
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

        # add the labels to the rows they will be in
        row1.addItem(resLab)
        row1.addItem(temLab)
        row2.addItem(humLab)
        row2.addItem(presLab)

        # Add all the label layouts to the main label layouts, this is done so they are grouped together nicely and easier to manage
        labels.addItem(row1) 
        labels.addItem(row2) 
        
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
        
    def updateVariables(self):
        generate_new_data()

        #Use with statement
        with open("data.json", "r") as data:

            json_data = json.loads(data.read())

            self.par.ResAmt = json_data["home_screen"].get("water_level")
            self.par.TmpAmt = json_data["home_screen"].get("temp")
            self.par.HumAmt = json_data["home_screen"].get("humidity")
            self.par.PrsAmt = json_data["home_screen"].get("water_pressure")

            self.R_amount.setText(str(self.par.ResAmt) + "%")
            self.T_amount.setText(str(self.par.TmpAmt) + "°F")
            self.H_amount.setText(str(self.par.HumAmt) + "%")
            self.P_amount.setText(str(self.par.PrsAmt) + "PSI")
        