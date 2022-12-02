from SecondWindow_GUI import SecondWindow
from PySide6.QtWidgets import *
from PySide6.QtSql import *
from PySide6.QtCore import *

class SecondWindow(QMainWindow, SecondWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)