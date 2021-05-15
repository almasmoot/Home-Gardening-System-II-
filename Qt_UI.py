import sys  # to get the screen size and close the window
from nutrientScreen import nutrientScreen # the class for the nutrients screen 
from mistingScreen import mistingScreen   # the class for the misting screen 
from homeScreen import homeScreen         # the class for the home screen  
from lightingScreen import lighingScreen  # the class for the lighting screen
from PyQt5.QtCore import Qt     # all the pyqt5 libraries we need
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

BUTTONFONT = QFont("times", 30) # font for the tabs
LABELFONT1 = QFont("times", 60) # font for the bigger labels (reservoir, temperature)
LABELFONT2 = QFont("times", 30) # font for the readings for the labels (60%)
WB = 500 # Width buffer for the tabs
HB = -65 # Hight buffer for the tabs

size = (0,0) # This will get the screen size as the tabs are configured based on that.

class MainWindow(QMainWindow):  # Main window for the gui
    def __init__(self, parent=None): # init function
        super(MainWindow, self).__init__(parent) # remake the init funtion with what we want
        self.BWIDTH = int((size.width()+WB) / 8) # Setting the button (tab) width
        self.BHEIGHT = int((size.height()+HB) / 4) # Setting the button (tab) height
        self.setStyleSheet("background-color: rgb(128,255,149)") # Set the background color
        # self.setWindowFlag(Qt.FramelessWindowHint)  # if we want a framless window uncomment this code
        self.startHome()

    def startHome(self):
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
        
        
        self.Window = homeScreen(self)
        self.setCentralWidget(self.Window)
        
        
        self.showMaximized()


    # Home is clicked this will run, right now it will make the home light green and all other tabs dark green as to show which tab is currently selected
    def home_clicked(self):
        self.Home.setStyleSheet("background-color: rgb(128,255,149); border: none")
        self.Misting.setStyleSheet("background-color: green; border: none")
        self.Lighting.setStyleSheet("background-color: green; border: none")
        self.Nutrients.setStyleSheet("background-color: green; border: none")
        self.Window = homeScreen(self)      # change to the home screen
        self.setCentralWidget(self.Window)

    # Misting is clicked this will run, right now it will make the home light green and all other tabs dark green as to show which tab is currently selected
    def mist_clicked(self):
        self.Home.setStyleSheet("background-color: green; border: none")
        self.Misting.setStyleSheet("background-color: rgb(128,255,149); border: none")
        self.Lighting.setStyleSheet("background-color: green; border: none")
        self.Nutrients.setStyleSheet("background-color: green; border: none")
        self.Window = mistingScreen(self)      # change to the misting screen
        self.setCentralWidget(self.Window)

    # Lighting is clicked this will run, right now it will make the home light green and all other tabs dark green as to show which tab is currently selected
    def light_clicked(self):
        self.Home.setStyleSheet("background-color: green; border: none")
        self.Misting.setStyleSheet("background-color: green; border: none")
        self.Lighting.setStyleSheet("background-color: rgb(128,255,149); border: none")
        self.Nutrients.setStyleSheet("background-color: green; border: none")
        self.Window = lighingScreen(self)      # change to the lighting screen
        self.setCentralWidget(self.Window)

    # Nutrients is clicked this will run, right now it will make the home light green and all other tabs dark green as to show which tab is currently selected
    def nutri_clicked(self):
        self.Home.setStyleSheet("background-color: green; border: none")
        self.Misting.setStyleSheet("background-color: green; border: none")
        self.Lighting.setStyleSheet("background-color: green; border: none")
        self.Nutrients.setStyleSheet("background-color: rgb(128,255,149); border: none")
        self.Window = nutrientScreen(self)      # change to the nutrients screen
        self.setCentralWidget(self.Window)

# I like the look of a more C++ program so this will run like main
if __name__=='__main__':
    app = QApplication(sys.argv) # Sets the application
    screen = app.primaryScreen() # This is to get the screen
    size = screen.size()  # With the screen we can get the screen size and base the tabs off of that
    win = MainWindow()    # Make the main window
    win.show()              # shows the main window
    sys.exit(app.exec_()) # on exit