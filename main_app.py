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
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 431, 251))
        self.tabWidget.setObjectName("tabWidget")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.label = QtWidgets.QLabel(self.tab_3)
        self.label.setGeometry(QtCore.QRect(170, 0, 101, 16))
        self.label.setObjectName("label")
        self.pwr_actual = QtWidgets.QLCDNumber(self.tab_3)
        self.pwr_actual.setEnabled(False)
        self.pwr_actual.setGeometry(QtCore.QRect(170, 70, 64, 23))
        self.pwr_actual.setObjectName("pwr_actual")
        self.measure_btn = QtWidgets.QPushButton(self.tab_3)
        self.measure_btn.setGeometry(QtCore.QRect(170, 140, 121, 23))
        self.measure_btn.setObjectName("measure_btn")
        self.layoutWidget = QtWidgets.QWidget(self.tab_3)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 10, 90, 203))
        self.layoutWidget.setObjectName("layoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.layoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.open_1 = QtWidgets.QRadioButton(self.layoutWidget)
        self.open_1.setChecked(True)
        self.open_1.setObjectName("open_1")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.open_1)
        self.open_2 = QtWidgets.QRadioButton(self.layoutWidget)
        self.open_2.setObjectName("open_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.open_2)
        self.open_3 = QtWidgets.QRadioButton(self.layoutWidget)
        self.open_3.setObjectName("open_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.open_3)
        self.open_4 = QtWidgets.QRadioButton(self.layoutWidget)
        self.open_4.setObjectName("open_4")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.open_4)
        self.open_5 = QtWidgets.QRadioButton(self.layoutWidget)
        self.open_5.setObjectName("open_5")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.open_5)
        self.open_6 = QtWidgets.QRadioButton(self.layoutWidget)
        self.open_6.setObjectName("open_6")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.open_6)
        self.open_7 = QtWidgets.QRadioButton(self.layoutWidget)
        self.open_7.setObjectName("open_7")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.open_7)
        self.open_all = QtWidgets.QRadioButton(self.layoutWidget)
        self.open_all.setObjectName("open_all")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.open_all)
        self.close_all = QtWidgets.QRadioButton(self.layoutWidget)
        self.close_all.setObjectName("close_all")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.LabelRole, self.close_all)
        self.ref_active = QtWidgets.QCheckBox(self.tab_3)
        self.ref_active.setEnabled(False)
        self.ref_active.setGeometry(QtCore.QRect(170, 170, 191, 17))
        self.ref_active.setObjectName("ref_active")
        self.label_2 = QtWidgets.QLabel(self.tab_3)
        self.label_2.setEnabled(False)
        self.label_2.setGeometry(QtCore.QRect(170, 50, 81, 16))
        self.label_2.setObjectName("label_2")
        self.led_on = QtWidgets.QCheckBox(self.tab_3)
        self.led_on.setEnabled(False)
        self.led_on.setGeometry(QtCore.QRect(170, 110, 70, 17))
        self.led_on.setObjectName("led_on")
        self.ref_pwr_display = QtWidgets.QLineEdit(self.tab_3)
        self.ref_pwr_display.setEnabled(False)
        self.ref_pwr_display.setGeometry(QtCore.QRect(170, 20, 113, 20))
        self.ref_pwr_display.setObjectName("ref_pwr_display")
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.lcd_open_pos = QtWidgets.QLCDNumber(self.tab_4)
        self.lcd_open_pos.setGeometry(QtCore.QRect(140, 20, 64, 23))
        self.lcd_open_pos.setObjectName("lcd_open_pos")
        self.lcd_closed_pos = QtWidgets.QLCDNumber(self.tab_4)
        self.lcd_closed_pos.setGeometry(QtCore.QRect(140, 50, 64, 23))
        self.lcd_closed_pos.setObjectName("lcd_closed_pos")
        self.lcd_ref = QtWidgets.QLCDNumber(self.tab_4)
        self.lcd_ref.setGeometry(QtCore.QRect(140, 80, 64, 23))
        self.lcd_ref.setObjectName("lcd_ref")
        self.label_3 = QtWidgets.QLabel(self.tab_4)
        self.label_3.setGeometry(QtCore.QRect(30, 20, 71, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.tab_4)
        self.label_4.setGeometry(QtCore.QRect(30, 43, 81, 20))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.tab_4)
        self.label_5.setGeometry(QtCore.QRect(30, 80, 61, 16))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.tab_4)
        self.label_6.setGeometry(QtCore.QRect(30, 120, 47, 13))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.tab_4)
        self.label_7.setGeometry(QtCore.QRect(10, 150, 401, 31))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.tab_4)
        self.label_8.setGeometry(QtCore.QRect(10, 170, 401, 31))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.tab_4)
        self.label_9.setGeometry(QtCore.QRect(140, 0, 47, 13))
        self.label_9.setObjectName("label_9")
        self.label_usb = QtWidgets.QLabel(self.tab_4)
        self.label_usb.setGeometry(QtCore.QRect(96, 120, 91, 20))
        self.label_usb.setObjectName("label_usb")
        self.label_11 = QtWidgets.QLabel(self.tab_4)
        self.label_11.setGeometry(QtCore.QRect(230, 0, 47, 13))
        self.label_11.setObjectName("label_11")
        self.open_input = QtWidgets.QSpinBox(self.tab_4)
        self.open_input.setGeometry(QtCore.QRect(230, 20, 42, 22))
        self.open_input.setMaximum(270)
        self.open_input.setObjectName("open_input")
        self.closed_input = QtWidgets.QSpinBox(self.tab_4)
        self.closed_input.setGeometry(QtCore.QRect(230, 50, 42, 22))
        self.closed_input.setMaximum(270)
        self.closed_input.setObjectName("closed_input")
        self.ref_power_input = QtWidgets.QDoubleSpinBox(self.tab_4)
        self.ref_power_input.setGeometry(QtCore.QRect(230, 80, 62, 22))
        self.ref_power_input.setMaximum(50.0)
        self.ref_power_input.setObjectName("ref_power_input")
        self.usb_input = QtWidgets.QLineEdit(self.tab_4)
        self.usb_input.setGeometry(QtCore.QRect(230, 120, 113, 20))
        self.usb_input.setObjectName("usb_input")
        self.input_password = QtWidgets.QLineEdit(self.tab_4)
        self.input_password.setGeometry(QtCore.QRect(300, 10, 113, 20))
        self.input_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.input_password.setObjectName("input_password")
        self.save_cfg_btn = QtWidgets.QPushButton(self.tab_4)
        self.save_cfg_btn.setGeometry(QtCore.QRect(300, 30, 111, 23))
        self.save_cfg_btn.setObjectName("save_cfg_btn")
        self.tabWidget.addTab(self.tab_4, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Reference Power"))
        self.measure_btn.setText(_translate("MainWindow", "measure"))
        self.open_1.setText(_translate("MainWindow", "open 1"))
        self.open_2.setText(_translate("MainWindow", "open 2"))
        self.open_3.setText(_translate("MainWindow", "open 3"))
        self.open_4.setText(_translate("MainWindow", "open 4"))
        self.open_5.setText(_translate("MainWindow", "open 5"))
        self.open_6.setText(_translate("MainWindow", "open 6"))
        self.open_7.setText(_translate("MainWindow", "open 7"))
        self.open_all.setText(_translate("MainWindow", "open all"))
        self.close_all.setText(_translate("MainWindow", "close all"))
        self.ref_active.setText(_translate("MainWindow", "reference measurment"))
        self.label_2.setText(_translate("MainWindow", "Power"))
        self.led_on.setText(_translate("MainWindow", "LED ON"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Control"))
        self.label_3.setText(_translate("MainWindow", "Open Position"))
        self.label_4.setText(_translate("MainWindow", "Closed Position"))
        self.label_5.setText(_translate("MainWindow", "Ref power"))
        self.label_6.setText(_translate("MainWindow", "USB"))
        self.label_7.setText(_translate("MainWindow", "This values should only be edited by qualified personel. Pleas contact engineering"))
        self.label_8.setText(_translate("MainWindow", "Changes only take effect if password is entered and Save button pressed"))
        self.label_9.setText(_translate("MainWindow", "Old"))
        self.label_usb.setText(_translate("MainWindow", "TextLabel"))
        self.label_11.setText(_translate("MainWindow", "New"))
        self.input_password.setText(_translate("MainWindow", "password"))
        self.save_cfg_btn.setText(_translate("MainWindow", "Save changes"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("MainWindow", "Settings"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

