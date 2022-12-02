import sys
from PySide6.QtWidgets import *
from PySide6.QtSql import *
from PySide6.QtCore import *
from Mainwindow import MainWindow
from PySide6.QtCore import QUrl
from celdaLaberinto import celdaLaberinto
from SecondWindow import SecondWindow
# Inicialización de la pantalla principal y ejecución del programa


if __name__ == '__main__':

    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
