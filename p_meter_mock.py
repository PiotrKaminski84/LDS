# -*- coding: utf-8 -*-
"""
Created on Fri Jun 14 10:58:38 2019

@author: Kaminskipi
"""
import random
class PowerMeter():
    
    def __init__(self,pin):
        self.pin=pin
        
    def connect(self,pin):
        pass
    
    def get_reading(self):
        pwr = 0.1 + random.randint(0,9)/10
        return pwr