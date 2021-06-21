import sys  # to get the screen size and close the window
import os
from nutrientScreen import nutrientScreen # The class for the nutrients screen 
from mistingScreen import mistingScreen   # The class for the misting screen 
from homeScreen import homeScreen         # The class for the home screen  
from lightingScreen import lighingScreen  # The class for the lighting screen
from preSet import preSet                 # The class for the preset screen
from warning import Warning               # Warning class was for a popup warning window, not used
from PyQt5.QtCore import QSize, QTimer, Qt     # all the pyqt5 libraries we need
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import threading

CRITICAL = "CRITICAL"   # Critical warning, will turn the screen red
WARNING = "WARNING"     # Warning, will turn the the screen yellow

SIZE = (480, 800) # (1080, 1920) This will get the screen size as the tabs are configured based on that.

FONT = "Cambria"    # The font for all the text

BUTTONFONT = QFont(FONT, (int(SIZE[0]/32))) # font for the tabs
LABELFONT1 = QFont(FONT, (int(SIZE[0]/16))) # font for the bigger labels (reservoir, temperature)
LABELFONT2 = QFont(FONT, (int(SIZE[0]/32))) # font for the readings for the labels (60%)
# WB = 500 # Width buffer for the tabs
# HB = -65 # Hight buffer for the tabs
# BUTTONCOLOR = "rgb(58,99,70)"
BACKGROUNDCOLOR = "rgb(107,138,116)" # a light green

# The different styles used
STYLE = "background-color: rgb(255,255,255); border: none; font: bold; color: " + BACKGROUNDCOLOR + ";"
STYLE2 = "background-color: " + BACKGROUNDCOLOR + "; border: none; font: bold; color: white;"
STYLE3 = "background-color: " + BACKGROUNDCOLOR + "; border: 2px solid white; font: bold; color: white;"

def start_bluetooth():
    os.system("python client.py")

# make a tab and set all of its specifications, takes in the button (tab), the text for the tab, and the function to connect it to
def makeTab(tab, text, func):
    tab.setFixedSize((int(SIZE[1] / 5)), (int(SIZE[0] / 5))) # set the size of the tab
    tab.setStyleSheet(STYLE)                                # set the background and boarder of the tab
    tab.setFont(BUTTONFONT)                                  # Set the button (tab) font                                                             
    tab.setText(text)                                        # Set the button (tab) text                                  
    tab.clicked.connect(func)                               # set the tab function to call when clicked

class MainWindow(QMainWindow):  # Main window for the gui
    def __init__(self, parent=None): # init function
        super(MainWindow, self).__init__(parent) # remake the init funtion with what we want
        self.setFixedSize(SIZE[1], SIZE[0]) # This is for testing on anything besides the pi, it will give an acurate mesurement of the size, uncomment when using on pi
        self.sizeOfScreen = SIZE
        self.setStyleSheet("background-color: " + BACKGROUNDCOLOR) # Set the background color
        self.setWindowFlag(Qt.FramelessWindowHint)  # if we want a framless window uncomment this code
        self.BACKGROUNDCOLOR = BACKGROUNDCOLOR
        self.STYLE = STYLE
        
        # changing these will change the values on the home screen
        self.ResAmt = 100
        self.TmpAmt = 70
        self.HumAmt = 80
        self.PrsAmt = 80

        # values for the misting screen
        self.MistIntrv = 2
        self.MistSec = 0

        # values for the lighting screen
        self.StartTime = 8
        self.EndTime = 20

        # values for the nutrients screen
        self.NutrAmt = 300

        # self.currentWidget = None

        timer = QTimer(self)                        # Timer to check for warnings
        timer.timeout.connect(self.checkWarnings)   # The check warnings function will check if there is a problem
        timer.start(1000)                           # Every 10th of a second

        self.level = "working" # level for the warnings

        # self.mdi = QMdiArea()
        # self.setBackgroundRole(self.mdi)

        self.startHome() # Set up the Tabs on the left, and start the home screen.

    def startHome(self):
        

        self.Home = QPushButton(self)                              # Make a push button (Home tab)                                                        
        makeTab(self.Home, "Home", self.home_clicked)              # Make a tab, pass in the button, the text and the fucntion to call
        self.Home.animateClick()                                   # This will click the home screen tab and will start the home screen first

        self.Misting = QPushButton(self)                           # Make a push button (Misting tab)                                                        
        makeTab(self.Misting, "Misting", self.mist_clicked)        # Make a tab, pass in the button, the text and the fucntion to call

        self.Lighting = QPushButton(self)                          # Make a push button (Lighting tab)                                                           
        makeTab(self.Lighting, "Lighting", self.light_clicked)     # Make a tab, pass in the button, the text and the fucntion to call

        self.Nutrients = QPushButton(self)                         # Make a push button (Nutrients tab)                                                        
        makeTab(self.Nutrients, "Nutrients", self.nutri_clicked)   # Pass in the tab to make, the text for the tab, and the function to call   

        self.preSet = QPushButton(self)                           # Make a push button (Preset tab)                                          
        makeTab(self.preSet, "Preset", self.preSet_clicked)       # Pass in the tab to make, the text for the tab, and the function to call     
        
        # self.showMaximized() # uncomment this when on the pi
        self.show() # comment this out when on anything with a bigger screen


    # Home is clicked this will run, right now it will make the home light green and all other tabs dark green as to show which tab is currently selected
    def home_clicked(self):
        self.setBtns(btn_clk=self.Home, other=[self.Misting, self.Lighting, self.Nutrients, self.preSet])
        self.Window = homeScreen(self)      # change to the home screen
        self.setCentralWidget(self.Window)
        # self.currentWidget = self.centralWidget()

    # Misting is clicked this will run, right now it will make the home light green and all other tabs dark green as to show which tab is currently selected
    def mist_clicked(self):
        self.setBtns(btn_clk=self.Misting, other=[self.Home, self.Lighting, self.Nutrients, self.preSet])
        self.Window = mistingScreen(self)      # change to the misting screen
        self.setCentralWidget(self.Window)

    # Lighting is clicked this will run, right now it will make the home light green and all other tabs dark green as to show which tab is currently selected
    def light_clicked(self):
        self.setBtns(btn_clk=self.Lighting, other=[self.Home, self.Misting, self.Nutrients, self.preSet])
        self.Window = lighingScreen(self)      # change to the lighting screen
        self.setCentralWidget(self.Window)

    # Nutrients is clicked this will run, right now it will make the home light green and all other tabs dark green as to show which tab is currently selected
    def nutri_clicked(self):
        self.setBtns(btn_clk = self.Nutrients, other = [self.Misting, self.Home, self.Lighting, self.preSet])
        self.Window = nutrientScreen(self)      # change to the nutrients screen
        self.setCentralWidget(self.Window)

    # Preset will give a list of plants to use for certain conditions.
    def preSet_clicked(self):
        self.setBtns(btn_clk = self.preSet, other = [self.Misting, self.Home, self.Lighting, self.Nutrients])
        self.Window = preSet(self)      # change to the nutrients screen.
        self.setCentralWidget(self.Window)

    # Set buttons sets up the tabs to change to the correct colors. Parameters: self, the button clicked, and a list of other buttons that were not clicked.
    def setBtns(self, btn_clk, other):
        other[0].setStyleSheet(STYLE)   # Set the unclicked buttons to white
        other[1].setStyleSheet(STYLE)
        other[2].setStyleSheet(STYLE)
        other[3].setStyleSheet(STYLE)
        btn_clk.setStyleSheet(STYLE2)   # The button clicked will be the same color of the backgound.

    # Check warnings check the warning level and set the background accordingling.
    def checkWarnings(self):
        if (self.level == CRITICAL): # if critical
            self.setStyleSheet("Background-color: red") # background red
        elif (self.level == WARNING): # if at a warning level
            self.setStyleSheet("Background-color: rgb(200,200,50)") # background yellow
        else:  # Other wise no warning
            self.setStyleSheet("Background-color:" + BACKGROUNDCOLOR) # background is the normal color

        # Code for a popup window that will show a warning (Does not work)
        # # sub = QMdiSubWindow()
        # # sub.setWidget(QLabel("Hello World"))
        # if (self.currentWidget != Warning(self)):
        #     self.currentWidget = self.centralWidget()
        #     print(self.currentWidget)
        #     sub = Warning(self)
        #     self.setCentralWidget(sub)
        #     self.mdi.addSubWindow(sub)
        #     sub.show()
        # else:
        #     print(self.currentWidget)
        #     self.setCentralWidget(self.currentWidget)
        


# I like the look of a more C++ program so this will run like main
if __name__=='__main__':
    bluetooth_thread = threading.Thread(target = start_bluetooth, args=())
    bluetooth_thread.start()
    
    app = QApplication(sys.argv) # Sets the application
    # screen = app.primaryScreen() # This is to get the screen
    # size = screen.size()  # With the screen we can get the screen size and base the tabs off of that
    win = MainWindow()    # Make the main window
    win.show()              # shows the main window
    sys.exit(app.exec_()) # on exit
    