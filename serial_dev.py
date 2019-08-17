# -*- coding: utf-8 -*-
"""
Created on Sat Aug  3 23:30:08 2019

@author: piotr_000
"""

import serial
import time
import thread

class MotorController():
    #store open/close pos = pickle
    def __init__(self):
        
        self.ser=serial.Serial("COM4",9600,timeout=None)

        

    def send_ser(self,cm):        
        self.ser.write(cm.encode())
        self.read_all()
        
    def read_ser(self):
        #time.sleep(3)
        ret=self.ser.read_all()
        return ret
    
    def read_all(self):
        rep=self.read_ser()
        return rep
            
    def get_pwr(self):
        self.send_ser("MS")
        w=self.read_ser()
        while w is None:
            w=self.read_ser()
            print(w)
        return w 
    
    def monitorSerial(self):
        r=''
        i=1
        while True:
            time.sleep(1)
            r=self.read_ser()
            i+=1
            print(r+str(i))
            if r!='':
                print(r)
                r=''
            if i==1000:
                i=0
                
    def start_serial_monitoring(self):
        thread.start_new_thread(self.monitorSerial,())
    
if __name__=='__main__':
    
    s=MotorController()
    s.start_serial_monitoring()
    s.send_ser('MS')
#    for i in range(1,1000):
#        s.read_ser()
    
   # p=s.get_pwr()
   # print(p)