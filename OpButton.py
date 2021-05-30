from PyQt5.QtWidgets import *
from PyQt5.QtCore import QPropertyAnimation

class OpButton(QPushButton):
    def __init__(self, *args, **kwargs):
        super(OpButton, self).__init__(*args, **kwargs)
        effect = QGraphicsOpacityEffect(self)
        self.setGraphicsEffect(effect)

        self.animation = QPropertyAnimation(effect, b"opacity")

        self.animation.setStartValue(0)
        self.animation.setEndValue(1)

        self.animation.setLoopCount(1)
        self.animation.setDuration(0)