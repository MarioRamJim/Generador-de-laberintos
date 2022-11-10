import sys
import PySide6.QtGui
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from PySide6.QtSql import *
from PySide6.QtCore import *
from PySide6.QtCore import QUrl
import pymysql, pymysql.cursors

class laberintoContainer (QWidget):
    def __init__(self,size):
        super().__init__()
        
        cp = PySide6.QtGui.QGuiApplication.primaryScreen().availableGeometry().center() 

        self.width =  (cp.x() * size)/10
        self.height = self.width
        
    def rellenarLaberinto(self):
        ...
