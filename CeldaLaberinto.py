import sys
import PySide6.QtGui
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from PySide6.QtSql import *
from PySide6.QtCore import *
from PySide6.QtCore import QUrl
import pymysql, pymysql.cursors

class celdaLaberinto (QWidget):
    def __init__(self,left,right,top,bot):
        super().__init__()

        self.setStyleSheet("background-color:white")
        cp = PySide6.QtGui.QGuiApplication.primaryScreen().availableGeometry().center() 

        print(cp)

        self.width = cp.x()/10
        self.height = self.width
        
if __name__ == '__main__':

    app = QApplication(sys.argv)
    window = celdaLaberinto(True,True,True,True)
    window.show()
    sys.exit(app.exec())