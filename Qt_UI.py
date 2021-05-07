import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *


size = (0,0)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.BWIDTH = int(size.width() / 8)
        self.BHEIGHT = int(size.height() / 4)
        
        self.initUI()

    def initUI(self):
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setStyleSheet("background-color: rgb(128,255,149)")

        self.Home = QPushButton(self)
        self.Home.setStyleSheet("background-color: green; border: none")
        self.Home.resize(self.BWIDTH, self.BHEIGHT)
        self.Home.setFont(QFont("Times", 20))
        self.Home.setText("Home")
        self.Home.clicked.connect(self.home_clicked)

        self.Misting = QPushButton(self)
        self.Misting.move(0, self.BHEIGHT)
        self.Misting.setStyleSheet("background-color: green; border: none")
        self.Misting.resize(self.BWIDTH, self.BHEIGHT)
        self.Misting.setFont(QFont("Times", 20))
        self.Misting.setText("Misting")
        self.Misting.clicked.connect(self.mist_clicked)

        self.Lighting = QPushButton(self)
        self.Lighting.move(0, self.BHEIGHT*2)
        self.Lighting.setStyleSheet("background-color: green; border: none")
        self.Lighting.resize(self.BWIDTH, self.BHEIGHT)
        self.Lighting.setFont(QFont("Times", 20))
        self.Lighting.setText("Lighting")
        self.Lighting.clicked.connect(self.light_clicked)

        self.Nutrients = QPushButton(self)
        self.Nutrients.move(0, self.BHEIGHT*3)
        self.Nutrients.setStyleSheet("background-color: green; border: none")
        self.Nutrients.resize(self.BWIDTH, self.BHEIGHT)
        self.Nutrients.setFont(QFont("Times", 20))
        self.Nutrients.setText("Nutrients")
        self.Nutrients.clicked.connect(self.nutri_clicked)

        self.Reservoir = QLabel(self)
        self.Reservoir.resize(320,90) # Width, Hight
        self.Reservoir.move(size.width()/2, 100)
        self.Reservoir.setText("Reservoir")
        self.Reservoir.setFont(QFont("Times", 40))
        self.R_amount = QLabel(self)
        self.R_amount.resize(120,30) # Width, Hight
        self.R_amount.move(size.width()/2 + 80, 180)
        self.R_amount.setText("%60")
        self.R_amount.setFont(QFont("Times", 25))

        self.Temperature = QLabel(self)
        self.Temperature.resize(330,90) # Width, Hight
        self.Temperature.move((size.width()/2 - 50), 350)
        self.Temperature.setText("Temperature")
        self.Temperature.setFont(QFont("Times", 40))
        self.T_amount = QLabel(self)
        self.T_amount.resize(120,30) # Width, Hight
        self.T_amount.move(size.width()/2 + 80, 430)
        self.T_amount.setText("75 F")
        self.T_amount.setFont(QFont("Times", 25))

        self.Humidity = QLabel(self)
        self.Humidity.resize(320,90) # Width, Hight
        self.Humidity.move(size.width()/2, 600)
        self.Humidity.setText("Humidity")
        self.Humidity.setFont(QFont("Times", 40))
        self.H_amount = QLabel(self)
        self.H_amount.resize(120,30) # Width, Hight
        self.H_amount.move(size.width()/2 + 80, 680)
        self.H_amount.setText("%50")
        self.H_amount.setFont(QFont("Times", 25))

        self.Pressure = QLabel(self)
        self.Pressure.resize(320,90) # Width, Hight
        self.Pressure.move(size.width()/2, 850)
        self.Pressure.setText("Pressure")
        self.Pressure.setFont(QFont("Times", 40))

        self.showMaximized()

    def home_clicked(self):
        self.Home.setStyleSheet("background-color: rgb(128,255,149); border: none")
        self.Misting.setStyleSheet("background-color: green; border: none")
        self.Lighting.setStyleSheet("background-color: green; border: none")
        self.Nutrients.setStyleSheet("background-color: green; border: none")

    def mist_clicked(self):
        self.Home.setStyleSheet("background-color: green; border: none")
        self.Misting.setStyleSheet("background-color: rgb(128,255,149); border: none")
        self.Lighting.setStyleSheet("background-color: green; border: none")
        self.Nutrients.setStyleSheet("background-color: green; border: none")

    def light_clicked(self):
        self.Home.setStyleSheet("background-color: green; border: none")
        self.Misting.setStyleSheet("background-color: green; border: none")
        self.Lighting.setStyleSheet("background-color: rgb(128,255,149); border: none")
        self.Nutrients.setStyleSheet("background-color: green; border: none")

    def nutri_clicked(self):
        self.Home.setStyleSheet("background-color: green; border: none")
        self.Misting.setStyleSheet("background-color: green; border: none")
        self.Lighting.setStyleSheet("background-color: green; border: none")
        self.Nutrients.setStyleSheet("background-color: rgb(128,255,149); border: none")

if __name__=='__main__':
    app = QApplication(sys.argv)
    screen = app.primaryScreen()
    size = screen.size()
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())