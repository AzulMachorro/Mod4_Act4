import os
from PyQt5 import QtGui, QtCore
#from PyQt5.QtCore import *
#from PyQt5.QtGui import *
from Mod4Act4ui import *

class Ui_MainWindow(QtWidgets.QMainWindow,Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)
#-------------------------------------------------------------
#Se nombran los elementos
        self.label.setText("Nombre el archivo")
        self.label_2.setText("Texto a escribir")
        self.label_3.setText("Numero de lineas en el archivo")
        self.label_4.setText("Numero de vocales")
        self.label_5.setText("Numero de consonantes")
        self.pushButton.setText("Actualizar")
#-------------------------------------------------------------
#Acciones de los elementos
        self.pushButton.clicked.connect(self.detectData)

    def detectData(self, bool_I):
        f = open(self.lineEdit.text(), "w")
        data = self.lineEdit_2.text()
        lines = int(self.lineEdit_3.text())
        [f.write(data + "\n") for _ in range(lines)]
        con = 0
        for i in data:
            if(i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u'):
                con += 1
        self.lineEdit_4.setText(str(con*lines))
        self.lineEdit_5.setText(str((len(data) - con)*lines))

    def Actualizar(self):
        self.lineEdit_5.setText("")
        self.lineEdit_5.setText("Hola")

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = Ui_MainWindow()
    window.show()
    app.exec_()
