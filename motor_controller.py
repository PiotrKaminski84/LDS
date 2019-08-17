# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 08:21:58 2019

@author: Kaminskipi
"""
import smbus
import time



class MotorController():
    
    def __init__(self):
        self.bus=smbus.SMBus(1)
        self.address=0x74
        self.CLOSE_POS=180
        self.OPEN_POS=0
        self.MOTORS=(1,2,3,4,5,6,7)
        self.motor_addr={1:(1,2),2:(3,4),3:(5,6),4:(7,8),5:(9,10),6:(11,12),7:(13,14)}
        
    def set_close_pos(self,close_pos):
        self.CLOSE_POS=close_pos
    
    def set_open_pos(self,open_pos):
        self.OPEN_POS=open_pos
        
    def writeRegister (self,register,value):
        self.bus.write_byte_data(self.address, register, value)
        
    def open_all(self):
        for m in self.MOTORS:
            self.writeRegister(self.motor_addr[m][0],self.OPEN_POS)
            self.writeRegister(self.motor_addr[m][1],128)
        self.ack()
    
    def close_all(self):
        for m in self.MOTORS:
            self.writeRegister(self.motor_addr[m][0],self.CLOSE_POS)
            self.writeRegister(self.motor_addr[m][1],128)
        self.ack()
    
    def open_motor(self,to_open):
        for m in self.MOTORS:
            if m==to_open:
                self.writeRegister(self.motor_addr[m][0],self.OPEN_POS)
            else:
                self.writeRegister(self.motor_addr[m][0],self.CLOSE_POS)
            self.writeRegister(self.motor_addr[m][1],128)
        self.ack()
        
    def ack(self):
        self.writeRegister(37,0)
        
if __name__=="__main__":
    mc=MotorController()
    mc.open_all()
    time.sleep(1)
    mc.close_all()
    time.sleep(1)
    mc.open_motor(1)
    time.sleep(1)
    mc.open_motor(2)
    time.sleep(1)
    mc.open_motor(3)
    time.sleep(1)
    mc.open_motor(4)
    time.sleep(1)
    mc.open_motor(5)
    time.sleep(1)
    mc.open_motor(6)
    time.sleep(1)
    mc.open_motor(7)
    time.sleep(1)
    mc.close_all()