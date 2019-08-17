# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(435, 262)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.openSh = QtWidgets.QGroupBox(self.centralwidget)
        self.openSh.setGeometry(QtCore.QRect(10, 0, 121, 241))
        self.openSh.setObjectName("openSh")
        self.pwr_ref = QtWidgets.QLCDNumber(self.centralwidget)
        self.pwr_ref.setGeometry(QtCore.QRect(190, 40, 64, 23))
        self.pwr_ref.setObjectName("pwr_ref")
        self.pwr_actual = QtWidgets.QLCDNumber(self.centralwidget)
        self.pwr_actual.setGeometry(QtCore.QRect(190, 90, 64, 23))
        self.pwr_actual.setObjectName("pwr_actual")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(190, 20, 101, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(190, 70, 81, 16))
        self.label_2.setObjectName("label_2")
        self.save_reference = QtWidgets.QPushButton(self.centralwidget)
        self.save_reference.setGeometry(QtCore.QRect(290, 40, 121, 23))
        self.save_reference.setObjectName("save_reference")
        self.ref_active = QtWidgets.QCheckBox(self.centralwidget)
        self.ref_active.setGeometry(QtCore.QRect(290, 70, 191, 17))
        self.ref_active.setObjectName("ref_active")
        self.led_on = QtWidgets.QCheckBox(self.centralwidget)
        self.led_on.setGeometry(QtCore.QRect(190, 130, 70, 17))
        self.led_on.setObjectName("led_on")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(20, 20, 90, 203))
        self.widget.setObjectName("widget")
        self.formLayout = QtWidgets.QFormLayout(self.widget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.open_1 = QtWidgets.QRadioButton(self.widget)
        self.open_1.setObjectName("open_1")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.open_1)
        self.open_2 = QtWidgets.QRadioButton(self.widget)
        self.open_2.setObjectName("open_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.open_2)
        self.open_3 = QtWidgets.QRadioButton(self.widget)
        self.open_3.setObjectName("open_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.open_3)
        self.open_4 = QtWidgets.QRadioButton(self.widget)
        self.open_4.setObjectName("open_4")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.open_4)
        self.open_5 = QtWidgets.QRadioButton(self.widget)
        self.open_5.setObjectName("open_5")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.open_5)
        self.open_6 = QtWidgets.QRadioButton(self.widget)
        self.open_6.setObjectName("open_6")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.open_6)
        self.open_7 = QtWidgets.QRadioButton(self.widget)
        self.open_7.setObjectName("open_7")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.open_7)
        self.open_all = QtWidgets.QRadioButton(self.widget)
        self.open_all.setObjectName("open_all")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.open_all)
        self.close_all = QtWidgets.QRadioButton(self.widget)
        self.close_all.setObjectName("close_all")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.LabelRole, self.close_all)
        self.openSh.raise_()
        self.open_1.raise_()
        self.open_2.raise_()
        self.open_3.raise_()
        self.open_4.raise_()
        self.open_5.raise_()
        self.open_6.raise_()
        self.open_7.raise_()
        self.open_all.raise_()
        self.close_all.raise_()
        self.pwr_ref.raise_()
        self.pwr_actual.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.save_reference.raise_()
        self.ref_active.raise_()
        self.led_on.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.save_reference.clicked.connect(self.pp)
        self.open_1.toggled.connect(self.Radio)
        
    def pp(self):
        print('123')
        
    def Radio(self):
        print('to radio')

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.openSh.setTitle(_translate("MainWindow", "Open Shutter"))
        self.label.setText(_translate("MainWindow", "Reference Power"))
        self.label_2.setText(_translate("MainWindow", "Power"))
        self.save_reference.setText(_translate("MainWindow", "Save reference"))
        self.ref_active.setText(_translate("MainWindow", "reference measurment"))
        self.led_on.setText(_translate("MainWindow", "LED ON"))
        self.open_1.setText(_translate("MainWindow", "open 1"))
        self.open_2.setText(_translate("MainWindow", "open 2"))
        self.open_3.setText(_translate("MainWindow", "open 3"))
        self.open_4.setText(_translate("MainWindow", "open 4"))
        self.open_5.setText(_translate("MainWindow", "open 5"))
        self.open_6.setText(_translate("MainWindow", "open 6"))
        self.open_7.setText(_translate("MainWindow", "open 7"))
        self.open_all.setText(_translate("MainWindow", "open all"))
        self.close_all.setText(_translate("MainWindow", "close all"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
