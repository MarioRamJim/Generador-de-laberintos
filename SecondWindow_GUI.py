from PySide6.QtCore import (QCoreApplication, QMetaObject, QRect, QSize)
from PySide6.QtGui import (QFont)
from PySide6.QtWidgets import (QLabel, QMenuBar, QPushButton, QSpinBox, QStatusBar, QWidget,QGridLayout)
from celdaLaberinto import celdaLaberinto

class SecondWindow(object):
    def setupUi(self, SecondWindow):
        if not SecondWindow.objectName():
            SecondWindow.setObjectName(u"SecondWindow")
        SecondWindow.resize(752, 598)

        self.centralwidget = QWidget(SecondWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        SecondWindow.setCentralWidget(self.centralwidget)


        self.retranslateUi(SecondWindow)

        QMetaObject.connectSlotsByName(SecondWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
       ...
    # retranslateUi

