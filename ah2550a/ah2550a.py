# -*- coding: utf-8 -*-
"""
Created on Thu Oct 05 14:55:32 2017

@author: Johannes
"""

import numpy as np
#from useful_stuff.useful import *

import visa
rm=visa.ResourceManager()



class AH2550A:
    '''one argumet: GPIB address, usually 28
    average is set to 6
    voltage is set to 1V
    timeout is set to 30 seconds. change by setting ah.timeout=xxxx (in ms)'''
    
    def __init__(self,GPIB_address=28,voltage=1,average=6,timeout=30000):
        try:
            self.ah=rm.get_instrument('GPIB0::{}'.format(GPIB_address))
            self.ah.write('V {}'.format(voltage))
            self.ah.write('AV {}'.format(average))
            self.ah.timeout=timeout
        except:
            print('device could not be found. check if device is turned on and connected and if GPIB address is correct')
            
        self.timeout=self.ah.timeout
    
    def set_timeout(self,time):
        '''set timeout time to wait for answer of bridge. when using long averaging time it might be needed to increase timeout
        timeout in ms --> not all values are possible. it will pick the closest possible time'''
        try:
            self.ah.timeout=time
            self.timeout=self.ah.timeout
        except:
            print('timeout could not be set')   
            
 
        
    def set_loss_unit(self,unit=2):
        '''** unit = 1: Q (nanosiemens)
        ** unit = 2: D (tan delta)
        ** unit = 3: seriel resistance (GOhm)
        ** unit = 4: paralel resistance (GOhm)
        ** unit = 5: loss vector'''
        if unit in (1,2,3,4,5):
            self.ah.write('UN {}'.format(unit))
        else:
            print('unit could not be set!')
            
    def get_loss_unit(self):
        '''** unit = 1: Q (nanosiemens)
        ** unit = 2: D (tan delta)
        ** unit = 3: seriel resistance (GOhm)
        ** unit = 4: paralel resistance (GOhm)
        ** unit = 5: loss vector'''
        try:
            unit=self.ah.ask('SH UN')
            return unit
        except:
            print('couldn"t read loss unit')
            
            
    def set_voltage(self,voltage):
        if isinstance(voltage,float) or isinstance(voltage,int):
            try:
                self.ah.write('V {}'.format(round(voltage,2)))
            except:
                print('error')
        else:
            print('parameter must be of type float or int')
            
    def get_voltage(self):
        '''get voltage'''
        try:
            voltage=self.ah.ask('SH V')
            return voltage
        except:
            print('couldn"t read voltage')

     
    def set_average(self,av):
        '''set average. possible values are from 1,...,16'''
        if av in range(16):
            self.ah.write('AV {}'.format(av))
        else:
            print('couldn"t set average time')

    def get_average(self):
        '''get average'''
        try:
            voltage=self.ah.ask('SH AV')
            return voltage
        except:
            print('couldn"t read average')
    
            
    def zero_on(self):
        try:
            self.ah.write('Z')
        except:
            pass

    def zero_off(self):
        try:
            self.ah.write('Z HA')
        except:
            pass

            
    def get_value(self):
        '''returns capacitance (pF), loss (depending on unit set before) and applied voltage'''
        try:
            a=self.ah.ask('SI').split()
            C,D,V=float(a[1]),float(a[4]),float(a[7])
            return C,D,V
        except:
            print('error')













