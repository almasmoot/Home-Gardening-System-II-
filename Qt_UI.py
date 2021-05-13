import sys  # to get the screen size and close the window
from PyQt5.QtCore import Qt     # all the pyqt5 libraries we need
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

BUTTONFONT = QFont("times", 30) # font for the tabs
LABELFONT1 = QFont("times", 60) # font for the bigger labels (reservoir, temperature)
LABELFONT2 = QFont("times", 30) # font for the readings for the labels (60%)
WB = 500 # Width buffer for the tabs
HB = -65 # Hight buffer for the tabs

size = (0,0) # This will get the screen size as the tabs are configured based on that.

class MainWindow(QWidget):  # Main window for the gui
    def __init__(self): # init function
        super().__init__() # remake the init funtion with what we want
        self.BWIDTH = int((size.width()+WB) / 8) # Setting the button (tab) width
        self.BHEIGHT = int((size.height()+HB) / 4) # Setting the button (tab) height
        
        self.initUI()  # call the initUI function to set up the visuals for the ui

    def initUI(self): # initUI function will set up all the labels and buttons we want for the ui
        # self.setWindowFlag(Qt.FramelessWindowHint)  # if we want a framless window uncomment this code
        self.setStyleSheet("background-color: rgb(128,255,149)") # Set the background color

        self.Home = QPushButton(self)                                    # Make a push button (Home tab)                                                        
        self.Home.setFixedSize(self.BWIDTH, self.BHEIGHT)                # These are the tabs and they need to be a set size to fill the left side of the screen
        self.Home.setStyleSheet("background-color: green; border: none") # set the background and boarder of the tab                                             
        self.Home.setFont(BUTTONFONT)                                    # Set the button (tab) font                                                             
        self.Home.setText("Home")                                        # Set the button (tab) text, this will be our home tab                                  
        self.Home.clicked.connect(self.home_clicked)                     # Set the function to call when the home (tab) button is pressed                         

        self.Misting = QPushButton(self)                                   # Make a push button (Misting tab)                                                        
        self.Misting.setFixedSize(self.BWIDTH, self.BHEIGHT)               # These are the tabs and they need to be a set size to fill the left side of the screen
        self.Misting.setStyleSheet("background-color: green; border: none")# set the background and boarder of the tab                                            
        self.Misting.setFont(BUTTONFONT)                                   # Set the button (tab) font                                                            
        self.Misting.setText("Misting")                                    # Set the button (tab) text, this will be our Misting tab                                  
        self.Misting.clicked.connect(self.mist_clicked)                    # Set the function to call when the Misting (tab) button is pressed                        

        self.Lighting = QPushButton(self)                                   # Make a push button (Lighting tab)                                                        
        self.Lighting.setFixedSize(self.BWIDTH, self.BHEIGHT)               # These are the tabs and they need to be a set size to fill the left side of the screen 
        self.Lighting.setStyleSheet("background-color: green; border: none")# set the background and boarder of the tab                                            
        self.Lighting.setFont(BUTTONFONT)                                   # Set the button (tab) font                                                            
        self.Lighting.setText("Lighting")                                   # Set the button (tab) text, this will be our Lighting tab                                 
        self.Lighting.clicked.connect(self.light_clicked)                   # Set the function to call when the Lighting (tab) button is pressed                       

        self.Nutrients = QPushButton(self)                                   # Make a push button (Nutrients tab)                                                        
        self.Nutrients.setFixedSize(self.BWIDTH, self.BHEIGHT)               # These are the tabs and they need to be a set size to fill the left side of the screen
        self.Nutrients.setStyleSheet("background-color: green; border: none")# set the background and boarder of the tab                                            
        self.Nutrients.setFont(BUTTONFONT)                                   # Set the button (tab) font                                                            
        self.Nutrients.setText("Nutrients")                                  # Set the button (tab) text, this will be our Nutrients tab                                 
        self.Nutrients.clicked.connect(self.nutri_clicked)                   # Set the function to call when the Nutrients (tab) button is pressed                        

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
        # tabs.setContentsMargins(0,0,0,0)   # probably not needed
        # labels.setContentsMargins(0,0,0,0) # probably not needed
        # resLab.setContentsMargins(0,0,0,0) # probably not needed
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
        tabs.addWidget(self.Home)
        tabs.addWidget(self.Misting)
        tabs.addWidget(self.Lighting)
        tabs.addWidget(self.Nutrients)
        
        # Add the tabs and labels to the main layout
        columns.addItem(tabs)
        columns.addItem(labels)

        # set the windows main layout
        self.setLayout(columns)

        # make the screen maximized when it starts
        self.showMaximized()


    # Home is clicked this will run, right now it will make the home light green and all other tabs dark green as to show which tab is currently selected
    def home_clicked(self):
        self.Home.setStyleSheet("background-color: rgb(128,255,149); border: none")
        self.Misting.setStyleSheet("background-color: green; border: none")
        self.Lighting.setStyleSheet("background-color: green; border: none")
        self.Nutrients.setStyleSheet("background-color: green; border: none")

    # Misting is clicked this will run, right now it will make the home light green and all other tabs dark green as to show which tab is currently selected
    def mist_clicked(self):
        self.Home.setStyleSheet("background-color: green; border: none")
        self.Misting.setStyleSheet("background-color: rgb(128,255,149); border: none")
        self.Lighting.setStyleSheet("background-color: green; border: none")
        self.Nutrients.setStyleSheet("background-color: green; border: none")

    # Lighting is clicked this will run, right now it will make the home light green and all other tabs dark green as to show which tab is currently selected
    def light_clicked(self):
        self.Home.setStyleSheet("background-color: green; border: none")
        self.Misting.setStyleSheet("background-color: green; border: none")
        self.Lighting.setStyleSheet("background-color: rgb(128,255,149); border: none")
        self.Nutrients.setStyleSheet("background-color: green; border: none")

    # Nutrients is clicked this will run, right now it will make the home light green and all other tabs dark green as to show which tab is currently selected
    def nutri_clicked(self):
        self.Home.setStyleSheet("background-color: green; border: none")
        self.Misting.setStyleSheet("background-color: green; border: none")
        self.Lighting.setStyleSheet("background-color: green; border: none")
        self.Nutrients.setStyleSheet("background-color: rgb(128,255,149); border: none")

# I like the look of a more C++ program so this will run like main
if __name__=='__main__':
    app = QApplication(sys.argv) # Sets the application
    screen = app.primaryScreen() # This is to get the screen
    size = screen.size()  # With the screen we can get the screen size and base the tabs off of that
    win = MainWindow()    # Make the main window
    win.show()              # shows the main window
    sys.exit(app.exec_()) # on exit