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
        self.ser=serial.Serial("/dev/ttyUSB1",9600,timeout=100)
        
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
       # time.sleep(1)
        ret=self.ser.readline()
        #ret+=self.ser.read_all()
        return ret
    
    def get_pwr(self):
        self.send_ser("MS")
        self.new_message=0        
        read=False
        i=0
        while read==False:
            i+=1
            msg=self.monitorSerial()                     
            if len(msg)>3:
                if msg[0:3]=='ref':
                    read=True
                    return(msg)
            self.new_message=0
            if i==10:
                self.send_ser("MS")
        return '' 
    
    def monitorSerial(self):
        r=''
        i=1
        while True:  
            time.sleep(0.1)
            if self.ser.in_waiting:
                r=self.read_ser()
            i+=1                
            if r!='':
                return r
            if i==20:
                return r
            
            
    def __del__(self):
        self.ser.close()
    
if __name__=='__main__':
    s=MotorController()
    print('Test')
    p=s.get_pwr()
    print(p)
    p=s.get_pwr()
    print(p)
    
    s.__del__()
