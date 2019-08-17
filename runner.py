# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from main_app import Ui_MainWindow

class runner(QtWidgets.QMainWindow, Ui_MainWindow):
    
    def __init__(self):      
        #QtWidgets.QDialog.__init__(self)
        super.__init__()
        self.save_reference.clicked.connect(self.test)
    

    def test(self):
        print('123')

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = runner()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

