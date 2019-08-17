# -*- coding: utf-8 -*-
"""
Created on Tue Aug 13 21:42:21 2019

@author: piotr_000
"""

import serial
import datetime
import time

class Connector():
    
    def __init__(self):
        self.ser = serial.Serial("COM4",9600,timeout=1000)
        self.message_list=dict()
        
        
    def __del__(self):
        self.ser.close()
        
        
    def send_ser(self,msg):
        self.ser.write(msg.encode())
        
    def read(self):
        return self.ser.readline()
        
    def read_ser(self,no_reads):
        for _ in range(1,no_reads+1):
            rs=True
            while (rs):
              if(self.ser.inWaiting()):
                msg=self.read()
                print(msg)
                rs=False
            tm=datetime.datetime.now()
            self.message_list[tm]=(msg)
            
        
    def print_data(self):
        for k,v in self.message_list.items():
            print ("{} read {}".format(k,v))
            
if __name__=='__main__':
    c=Connector()
    m=c.read()
    print(m)
    c.send_ser("MS")
    
#    for i in range(1,50):
#            m=c.read()
#            tm=datetime.datetime.now()
#            print(tm)
#            print(m)
    c.read_ser(3)
    c.print_data()
    c.send_ser("MS")
    c.read_ser(2)
    c.print_data()
    c.send_ser("MS")
    c.read_ser(2)
    c.print_data()
    c.__del__()