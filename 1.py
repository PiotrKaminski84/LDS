# -*- coding: utf-8 -*-
"""
Created on Thu Jul 25 15:41:10 2019

@author: 74_fibrelaser
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 08:21:58 2019

@author: Kaminskipi
"""

#import time
import serial
import time

class MotorController():
    #store open/close pos = pickle
    def __init__(self):
        
        self.ser=serial.Serial("COM4",9600)

        
    def set_close_pos(self,close_pos):
        self.send_ser("SC{}".format(close_pos))
    
    def set_open_pos(self,open_pos):
        self.send_ser("SO{}".format(open_pos))
        
        
    def writeRegister (self,register,value):
        pass
        
    def open_all(self):
        self.send_ser("OA")
    
    def close_all(self):
        self.send_ser("CA")
    
    def open_motor(self,to_open):
        if to_open==8:
            self.open_all
        elif to_open==9:
            self.close_all()
        else:
            self.send_ser("OP{}".format(to_open-1))      

    def send_ser(self,cm):
        
        self.ser.write(cm.encode())
        
    def read_ser(self):
        ret=self.ser.read_all()
        return ret
    
    def get_pwr(self):
        self.send_ser("MS")   
        time.sleep(3)
        return self.read_ser()
    
