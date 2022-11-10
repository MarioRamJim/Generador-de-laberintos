from PySide6.QtCore import (QMetaObject, QRect)
from PySide6.QtGui import (QFont)
from PySide6.QtWidgets import ( QLabel, QMenuBar, QPushButton, QStatusBar, QWidget, QLineEdit)
from laberintoContainer import laberintoContainer

# Definición de la forma que tendrá la pantalla de login e inicialización de sus componentes

class MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")

        MainWindow.resize(1280, 720)

        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")

        self.laberinto = laberintoContainer(5)
        self.laberinto.setObjectName("laberinto")
        self.laberinto.setGeometry(100,100,100,100)
        self.laberinto.width = 1280
        self.laberinto.width = 720

        self.laberinto.setParent(MainWindow)

        self.retranslateLogin(MainWindow)


    #Definición de los valores que tendrán los dstintos componentes de la pantalla de login

    def retranslateLogin(self, MainWindow):
        ...

    # retranslateUi

