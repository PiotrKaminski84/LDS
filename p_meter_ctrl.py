# -*- coding: utf-8 -*-
"""
Created on Fri Jun 14 10:58:38 2019

@author: Kaminskipi
"""

from p_meter_mock import PowerMeter
import math

class PowerMeterCtrl():
    
    def __init__(self,pin,pin_ref,mc):
        self.mc =mc
        self.pin=pin
        self.pin_ref=pin_ref
        self.pwr_meter=PowerMeter(self.pin)
        self.pwr_metr_ref=PowerMeter(self.pin_ref)
        self.ref = {}
        self.meas = {}
        self.losses ={}
     

    def get_ref(self):
        self.get_ref_p()
        return self.ref
    
    def get_ref_p(self):
       for i in range(1,8):
            self.mc.open_motor(1)
            r = self.pwr_meter.get_reading()
            ref = self.pwr_metr_ref.get_reading()
            self.ref[i]=[r,ref]        
    
    def get_meas(self):
        self.get_meas_p()
        self.calc_losses()
        return self.losses
    
    def calc_losses(self):
        for k,v in self.meas.items():
            ref_m=self.ref[k][0]
            ref_r=self.ref[k][1]
            m=v[0]
            r=v[1]
            self.losses[k]=10*math.log10(m/ref_m*r/ref_r)
        return self.losses
            
    def get_meas_p(self):
       for i in range(1,8):
            self.mc.open_motor(1)
            r = self.pwr_meter.get_reading()
            ref = self.pwr_metr_ref.get_reading()
            self.meas[i]=[r,ref]
    
    def get_reading(self):
 
        pwr =self.pwr_meter.get_reading()
        return str(pwr)