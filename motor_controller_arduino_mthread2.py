# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 08:21:58 2019

@author: Kaminskipi
"""

#import time
import serial
import time
import threading

class MotorController():
    #store open/close pos = pickle
    def __init__(self):
        
        self.ser=serial.Serial("COM4",9600)        
        time.sleep(1)
        self.read_ser()
        
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

    def read(self):
        return self.ser.readline()
        
    def read_ser(self):
       rs=True
       while (rs):
          if(self.ser.inWaiting()):
            msg=self.read()
#            print(msg)
            rs=False
       return(msg)            
    
    def get_pwr(self):
        self.send_ser("MS")
        self.read_ser()
        return self.read_ser()    
        
    def __del__(self):
        self.ser.close()
    
if __name__=='__main__':
    s=MotorController()
    p=s.get_pwr()
    print(p)
    p=s.get_pwr()
    print(p)