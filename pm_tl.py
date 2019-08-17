# -*- coding: utf-8 -*-
"""
Created on Thu Jul 11 14:05:37 2019

@author: Kaminskipi
"""
#import visa
#from ThorlabsPM100 import ThorlabsPM100
#rm = visa.ResourceManager()
#inst = rm.open_resource('ASRL5::INSTR')

import visa
from ThorlabsPM100 import ThorlabsPM100
rm = visa.ResourceManager()
inst = rm.open_resource('ASRL6::INSTR')
power_meter = ThorlabsPM100(inst=inst)

print (power_meter.read) # Read-only property
print (power_meter.sense.average.count) # read property
#power_meter.sense.average.count = 10 # write property
#power_meter.system.beeper.immediate() # method