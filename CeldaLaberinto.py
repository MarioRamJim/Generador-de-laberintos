import sys
import PySide6.QtGui
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from PySide6.QtSql import *
from PySide6.QtCore import *
from PySide6.QtCore import QUrl
import pymysql, pymysql.cursors

class celdaLaberinto(QWidget):
    def __init__(self,size):
        super().__init__()
        
        self.size = (50,50)
        self.layout = QGridLayout()

        self.setLayout(self.layout)
        

