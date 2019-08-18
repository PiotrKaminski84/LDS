# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from main_app import Ui_MainWindow
import sys
from motor_controller_arduino_mthread import MotorController #arduino_mthread
import pickle

class runner():
    
    def __init__(self):
        self.cfg = config()
#        self.cfg.save_cfg()
        self.cfg.load_cfg()
        self.mc = MotorController()
        self.a=Ui_MainWindow()
        app = QtWidgets.QApplication(sys.argv)
        MainWindow = QtWidgets.QMainWindow()
        self.a.setupUi(MainWindow)
        self.add_functions()
        MainWindow.show()
        self.display_cfg()
        sys.exit(app.exec_())
       
#        ui = Ui_MainWindow()
    def add_functions(self):     
        self.a.open_1.toggled.connect(lambda a : self.open_one(self.a.open_1,0))        
        self.a.open_2.toggled.connect(lambda a : self.open_one(self.a.open_2,1))
        self.a.open_3.toggled.connect(lambda a : self.open_one(self.a.open_3,2))
        self.a.open_4.toggled.connect(lambda a : self.open_one(self.a.open_4,3))
        self.a.open_5.toggled.connect(lambda a : self.open_one(self.a.open_5,4))
        self.a.open_6.toggled.connect(lambda a : self.open_one(self.a.open_6,5))
        self.a.open_1.toggled.connect(lambda a : self.open_one(self.a.open_7,6))
        self.a.open_all.toggled.connect(lambda a : self.open_one(self.a.open_all,8))
        self.a.close_all.toggled.connect(lambda a : self.open_one(self.a.close_all,9))
        self.a.measure_btn.clicked.connect(self.measure)
        self.a.save_cfg_btn.clicked.connect(self.save_cfg)
        
    def measure(self):
        pwr=self.mc.get_pwr()
        print(pwr)
        self.a.ref_pwr_display.setText(str(pwr))
    
    def save_cfg(self):
        if self.a.input_password.text()!='1234':
            self.a.input_password.setText('incorrect')
        else:
            self.update_cfg()
            self.display_cfg()
            self.a.input_password.setText('')
            
    def update_cfg(self):        
        self.cfg.open_pos = self.a.open_input.value()
        self.cfg.closed_pos = self.a.closed_input.value()
        self.cfg.ref_power = self.a.ref_power_input.value()
        self.cfg.usb = self.a.usb_input.text()
        self.cfg.save_cfg()

    def display_cfg(self):
        self.a.lcd_open_pos.display(self.cfg.open_pos) 
        self.a.lcd_closed_pos.display(self.cfg.closed_pos)
        self.a.lcd_ref.display(self.cfg.ref_power)
        self.a.label_usb.setText(self.cfg.usb)
        self.a.open_input.setValue(self.cfg.open_pos)
        self.a.closed_input.setValue(self.cfg.closed_pos)
        self.a.ref_power_input.setValue(self.cfg.ref_power)
        self.a.usb_input.setText(self.cfg.usb)    

    def open_one(self,btn,motor):
        if btn.isChecked()==True:
            self.mc.open_motor(motor)
            print(btn.text())
        
    def test(self):
        print('123')        

        
class config():
    
    def __init__(self):
        self.closed_pos=90
        self.open_pos=120
        self.ref_power=0
        self.usb = '/dev/ttyACM0' 
        self.file='cfg.pkl'
        
    def save_cfg(self):
        with open(self.file,'wb') as f:
            pickle.dump(self,f)
            
        
    def load_cfg(self):
        with open(self.file,'rb') as f:
            c = pickle.load(f)
            self.copy(c)
            
    def copy(self,c):
        self.closed_pos=c.closed_pos
        self.open_pos=c.open_pos
        self.ref_power=c.ref_power
        self.usb =c.usb
        self.file=c.file

if __name__ == "__main__":
    r = runner()


