from PySide6.QtCore import (QMetaObject, QRect)
from PySide6.QtGui import (QFont)
from PySide6.QtWidgets import ( QLabel, QMenuBar, QPushButton, QStatusBar, QWidget, QLineEdit,QGridLayout,QMainWindow)
from laberintoContainer import laberintoContainer

# Definición de la forma que tendrá la pantalla de login e inicialización de sus componentes

class MainWindow(object):
    def setupUi(self, MainWindow):

        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        
        MainWindow.resize(1080,720)

        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)


        self.laberinto = QWidget()
        self.laberinto.setStyleSheet("background-color:black")
        self.laberinto.setParent(self.centralwidget)
        self.laberinto.setObjectName(u"laberinto")
        self.laberinto.setGeometry(QRect(150, 170, 150, 150))

        self.retranslateLogin(MainWindow)


    #Definición de los valores que tendrán los dstintos componentes de la pantalla de login

    def retranslateLogin(self, MainWindow):
        ...

    # retranslateUi

