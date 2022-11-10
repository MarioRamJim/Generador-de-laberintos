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

        self.inicioSesionButton.clicked.connect(self.inicioSesion)



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