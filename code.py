###################### IMPORTACIÓN DE LIBRERIAS
import time
import cv2
import os
import sqlite3 
import sys
from PyQt5 import QtWidgets, QtGui, uic
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox 
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
from SqliteH import *

app = QtWidgets.QApplication([])
gui1 = uic.loadUi('1.ui')
gui2 = uic.loadUi('2.ui')
gui3 = uic.loadUi('3.ui')

def Acceder():
    gui2.show()
    gui1.hide()
def Salir():
    gui1.destroy()
    sys.exit()
def Regresar():
    gui2.hide()
    gui1.show()
def CargaDatos():
    conexion = SqliteHelper('Conferencias.db')    
    usuarios = conexion.Seleccionar('SELECT * FROM Eventos')
    for no_fila, usuario in enumerate(usuarios):
            gui2.Tabla.insertRow(no_fila)
            for no_columna, dato in enumerate(usuario):
                tabla = QtWidgets.QTableWidgetItem(str(dato))
                gui2.Tabla.setItem(no_fila, no_columna, tabla)
def LimpiarDatos():
    print(gui2.Tabla.rowCount())
    while(gui2.Tabla.rowCount()>0):
        gui2.Tabla.removeRow(0)
def Refresca():
    LimpiarDatos()
    CargaDatos()
def Registrar():
    gui3.show()
    gui2.hide()
def Regresar2():
    gui3.hide()
    gui2.show()
def Add():
    db = sqlite3.connect('Conferencias.db')
    cursor = db.cursor()
    
    
    Evento = gui3.evento.currentText()
    Nombre = gui3.nombre.text()
    Tel = gui3.telefono.text()
    Correo = gui3.correo.text()
    print(Evento,Nombre,Tel,Correo)
    
    if Evento == 'Conferencia - Las redes Sociales':
        cursor.execute("SELECT * FROM RedesSociales")
        long = len(cursor.fetchall())
        if long < 5:
            sql2 = '''INSERT INTO RedesSociales(Nombre, Teléfono, Correo) VALUES(?,?,?)'''
            cursor.execute(sql2,(Nombre, Tel, Correo))
            db.commit() 
            gui3.nombre.clear()
            gui3.telefono.clear()
            gui3.correo.clear()
            Regresar2()
        else:
            print('El evento está lleno. ')
            gui3.nombre.clear()
            gui3.telefono.clear()
            gui3.correo.clear()
            showError()
    elif Evento == 'Conferencia - Industria 4.0 ':
        cursor.execute("SELECT * FROM Industria4_0")
        long = len(cursor.fetchall())
        if long < 4:
            sql2 = '''INSERT INTO Industria4_0(Nombre, Teléfono, Correo) VALUES(?,?,?)'''
            cursor.execute(sql2,(Nombre, Tel, Correo))
            db.commit() 
            gui3.nombre.clear()
            gui3.telefono.clear()
            gui3.correo.clear()
            Regresar2()
        else:
            print('El evento está lleno. ')
            gui3.nombre.clear()
            gui3.telefono.clear()
            gui3.correo.clear()
            showError()
    elif Evento == 'Conferencia - Mejora tu CV':
        cursor.execute("SELECT * FROM Mejora_tu_CV")
        long = len(cursor.fetchall())
        print(long)
        if long < 3:
            sql2 = '''INSERT INTO Mejora_tu_CV(Nombre, Teléfono, Correo) VALUES(?,?,?)'''
            cursor.execute(sql2,(Nombre, Tel, Correo))
            db.commit() 
            gui3.nombre.clear()
            gui3.telefono.clear()
            gui3.correo.clear()
            Regresar2()
        else:
            print('El evento está lleno. ')
            gui3.nombre.clear()
            gui3.telefono.clear()
            gui3.correo.clear()
            showError()
def showError():
    msgBox = QMessageBox()
    msgBox.setIcon(QMessageBox.Critical)
    msgBox.setText('El Evento está lleno. ')
    msgBox.setWindowTitle('Full')
    msgBox.setStandardButtons(QMessageBox.Ok)
    msgBox.buttonClicked.connect(Regresar2)
    msgBox.exec()
    
gui1.acceder.clicked.connect(Acceder)
gui1.salir.clicked.connect(Salir)

gui2.salir.clicked.connect(Regresar)
gui2.Visualizar.clicked.connect(Refresca)
gui2.registrar.clicked.connect(Registrar)

gui3.salir.clicked.connect(Regresar2)
gui3.registrar.clicked.connect(Add)

gui1.show()
app.exec()