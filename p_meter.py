# -*- coding: utf-8 -*-
"""
Created on Fri Jun 14 10:58:38 2019

@author: Kaminskipi
"""

class PowerMeter_mock():
    
    def __init__(self,pin):
        self.pin=pin
        self.connect(self.pin)
        
    def connect(self,pin):
        pass
    
    def get_reading(self):
        return '0.1'