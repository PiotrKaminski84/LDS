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
        self.connected=False
        try: 
            self.ser=serial.Serial("COM4",9600) # /dev/ttyACM0
            self.connected=True
        except:
            self.connected=False 
            print('no serial connection')
        self.start_serial_monitoring()
        self.new_message=1
        self.message=list()

        
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
        if self.connected:
            self.ser.write(cm.encode())
        
    def read_ser(self):
       # time.sleep(1)
       if self.connected:
           ret=self.ser.readline()
           return ret
       return 'ref pwr not connected'
    
    def get_pwr(self):
        self.send_ser("MS")
        self.new_message=0        
        read=False
        while read==False:
            if self.new_message==1:                
                msg=self.message
                if len(msg)>3:
                    if msg[0:3]=='ref':
                        read=True
                        return(msg[7:])
                self.new_message=0
        return '' 
    
    def monitorSerial(self):
        r=''
        i=1
        while True:
           # time.sleep(0.2)
            if self.new_message!=1:
                r=self.read_ser()
                i+=1                
                if r!='':
                    print(r)
                    self.new_message=1
                    self.message=r
                    r=''
                if i==1000:
                    i=0
                
    def start_serial_monitoring(self):
        threading.Thread(target=self.monitorSerial,args=())
        
    def __del__(self):
        self.ser.close()
    
if __name__=='__main__':
    s=MotorController()
    p=s.get_pwr()
    print(p)
    p=s.get_pwr()
    print(p)