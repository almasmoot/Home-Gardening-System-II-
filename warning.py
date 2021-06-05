from PyQt5.QtCore import Qt, QTimer     # all the pyqt5 libraries we need
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class Warning(QWidget):
    def __init__(self, parent):
        super(Warning, self).__init__(parent)
        label = QLabel("Hello World", self)
        label.setStyleSheet("Background-color: blue")
        label.setFont(QFont("Times", 30))
        label.resize(300, 300)