import sys
from PySide6.QtWidgets import *
from PySide6.QtSql import *
from PySide6.QtCore import *
from MainWindow_GUI import MainWindow 
from SecondWindow import SecondWindow
from PySide6.QtCore import QUrl
import pymysql, pymysql.cursors

class MainWindow(QMainWindow, MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.laberinto = QWidget()
        self.laberinto.setStyleSheet("background-color:black;border-color:red")
        self.laberinto.setParent(self.centralwidget)
        self.laberinto.setObjectName(u"laberinto")
        self.laberinto.setGeometry(QRect(150, 170, 150, 150))

        
        self.laberinto2 = QWidget()
        self.laberinto2.setStyleSheet("background-color:black;border-color:red")
        self.laberinto2.setParent(self.centralwidget)
        self.laberinto2.setObjectName(u"laberinto")
        self.laberinto2.setGeometry(QRect(200, 170, 150, 150))

        
        self.laberinto3 = QWidget()
        self.laberinto3.setStyleSheet("background-color:black;border-color:red")
        self.laberinto3.setParent(self.centralwidget)
        self.laberinto3.setObjectName(u"laberinto")
        self.laberinto3.setGeometry(QRect(250, 170, 150, 150))

        
        self.laberinto4 = QWidget()
        self.laberinto4.setStyleSheet("background-color:black;border-color:red")
        self.laberinto4.setParent(self.centralwidget)
        self.laberinto4.setObjectName(u"laberinto")
        self.laberinto4.setGeometry(QRect(150, 220, 150, 150))

        
        self.laberinto5 = QWidget()
        self.laberinto5.setStyleSheet("background-color:black;border-color:red")
        self.laberinto5.setParent(self.centralwidget)
        self.laberinto5.setObjectName(u"laberinto")
        self.laberinto5.setGeometry(QRect(150, 270, 150, 150))

        
        self.laberinto6 = QWidget()
        self.laberinto6.setStyleSheet("background-color:black;border-color:red")
        self.laberinto6.setParent(self.centralwidget)
        self.laberinto6.setObjectName(u"laberinto")
        self.laberinto6.setGeometry(QRect(200, 220, 150, 150))

        
        self.laberinto7 = QWidget()
        self.laberinto7.setStyleSheet("background-color:black;border-color:red")
        self.laberinto7.setParent(self.centralwidget)
        self.laberinto7.setObjectName(u"laberinto")
        self.laberinto7.setGeometry(QRect(200, 270, 150, 150))

        
        self.laberinto8 = QWidget()
        self.laberinto8.setStyleSheet("background-color:black;border-color:red")
        self.laberinto8.setParent(self.centralwidget)
        self.laberinto8.setObjectName(u"laberinto")
        self.laberinto8.setGeometry(QRect(250, 220, 150, 150))

        
        self.laberinto9 = QWidget()
        self.laberinto9.setStyleSheet("background-color:black;border-color:red")
        self.laberinto9.setParent(self.centralwidget)
        self.laberinto9.setObjectName(u"laberinto")
        self.laberinto9.setGeometry(QRect(250, 270, 150, 150))


    def insertarEmpleado(self):

        self.connection = pymysql.connect(host='localhost',
                                             user='root',
                                            password='admin',
                                            database='PythonDB',
                                            cursorclass=pymysql.cursors.DictCursor)
        with self.connection:

            with self.connection.cursor() as cursor:

                sentencia = "select dni from empleados order by dni desc"
                cursor.execute(sentencia)
                id = cursor.fetchone()

            with self.connection.cursor() as cursor:

                if id != None:

                    idNueva = str(int(id["dni"])+1)
                    sentencia = "insert into empleados values ('Empleado "+ idNueva +"','a','a','"+ idNueva +"','"+"1D')"
                    cursor.execute(sentencia)
                    self.connection.commit()
                    print("insercion del empleado " + idNueva + " realizada con exito")

                else:

                    sentencia = "insert into empleados values ('Empleado 1' , 'a' , 'a' , '1', '1D')"
                    cursor.execute(sentencia)
                    self.connection.commit()
                    print("insercion del empleado 1 realizada con exito")

    def insertarCliente(self):

        self.connection = pymysql.connect(host='localhost',
                                            user='root',
                                            password='admin',
                                            database='PythonDB',
                                            cursorclass=pymysql.cursors.DictCursor)
        with self.connection:

            with self.connection.cursor() as cursor:

                sentencia = "select * from clientes order by id desc"
                cursor.execute(sentencia)
                id = cursor.fetchone()

            with self.connection.cursor() as cursor:
                
                print(id["id"])

                if id != None:

                    idNueva = str(id["id"]+1)

                    sentencia = "insert into clientes values ("+idNueva+",'Cliente "+ idNueva +"','"+ idNueva +"D')"
                    cursor.execute(sentencia)
                    self.connection.commit()
                    print("insercion del cliente " + idNueva + " realizada con exito")

                else:

                    sentencia = "insert into clientes values ( 1,'Cliente 1','1D')"
                    cursor.execute(sentencia)
                    self.connection.commit()
                    print("insercion del cliente 1 realizada con exito")

    def inicioSesion(self):
        usuario = self.lineEditUsuario.text()
        passwd = self.lineEditPasswd.text() 

        self.connection = pymysql.connect(host='localhost',
                                            user='root',
                                            password='admin',
                                            database='PythonDB',
                                            cursorclass=pymysql.cursors.DictCursor)

        with self.connection:

             with self.connection.cursor() as cursor:
                 
                sentencia = "SELECT codigo FROM usuarios WHERE EXISTS (SELECT nombre , pass FROM usuarios WHERE nombre = '"+usuario+"' and pass='"+passwd+"');"
                cursor.execute(sentencia)
                id = cursor.fetchone()

                if (id!=None):
                    self.destroy()
                    window = SecondWindow(id)
                    window.show()
                    QApplication(sys.argv).exec()
