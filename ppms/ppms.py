# -*- coding: utf-8 -*-
"""
Created on Thu Oct 05 14:55:32 2017

@author: Johannes
"""

import numpy as np
#from matplotlib import pyplot as pl
#from glob import glob
#from scipy.optimize import curve_fit
#from scipy.interpolate import UnivariateSpline
#from matplotlib import rc,cm
#from useful_stuff.useful import *
#from matplotlib import rc_params as params
import visa
rm=visa.ResourceManager()

 
approach_mode={'0':'linear', '1':'no overshoot', '2':'oscillate'}
magnet_mode={'0': 'persistent', '1': 'driven'}
temp_approach={'0':'fast', '1':'no overshoot'}
delay=0.02




class BLUE_9T_PPMS:
    '''one argumet: GPIB address, usually 15
    automatically sets \r as EOS termination to be recognized'''
    
    def __init__(self,GPIB_address=15):
        self.ppms=rm.get_instrument('GPIB0::{}'.format(GPIB_address))
        self.ppms.read_termination='\r'
        self.ppms.clear()
#        try:
#            self.ppms.ask('TEMP?',)
#            self.ppms.ask('TEMP?')
#        except:
#            print('problem')
        print('successful')
        
        
    def get_date(self):
        '''returns: month,day,year'''
        date=self.ppms.ask('DATE?')
        return date

            
    def get_field_setpoint(self):
        '''returns field setpoint,rate, approach mode and magnet mode'''
        a=self.ppms.ask('FIELD?',delay)[:-1].split(',')
        field,rate,approach,magnet=float(a[0]),float(a[1]),a[2],a[3]
        return field,rate,approach_mode[approach],magnet_mode[magnet]
        
    
    def set_field(self,field=0,rate=100, approach=1 ,magnet=0):
        '''**approach mode:**
        0 -Linear Approach 
        1 -No Overshoot Approach
        2 -Oscillate Approach \n
        **magnet_mode:**
        0 -persitent
        1 - driven'''
        self.ppms.write('FIELD {} {} {} {}'.format(field,rate,approach,magnet))
        
        
                
    def get_data(self,flag):
        '''GETDAT? DataFlags [NoUpdateFlag]
        Get Data Query -(Immediate Mode Only) Returns the data items specified in the DataFlags parameter
        Dataflag: number, where binary version picks columns to show. e.g. 3=11  --> first and second coluns are returned'''
        a=self.ppms.ask('GETDAT? {}'.format(flag))
        return a
        
    def get_important_data(self):
        '''**returns:** array with time, status, temperature, field, resistance CH1, excitation CH1'''
        value, time, status, temperature, field, resistance, excitation=self.ppms.ask('GETDAT? 55',delay)[:-2].split(',')
        a=np.array([float(time), int(status), float(temperature), float(field), float(resistance), float(excitation)])        
        return a

        
    def get_temperature(self,update=0):
        '''returns temperature in K (as float)
        update=0 --> update all readings before returning data
        update = 1 --> return most current values'''
        temp=self.ppms.ask('GETDAT? 2 {}',delay).format(int(update))[:-1].split(',')
        return float(temp[-1])


    def get_temperature_setpoint(self):
        '''returns temperature,rate and approach mode : 0: fast \t 1: no overshoot'''
        s=self.ppms.ask('TEMP?',0.05)[:-1]
        print(s)
        temp,rate,mode=s.split(',')
        return float(temp),float(rate),temp_approach[str(int(mode))]

            
    def set_temperature(self,temp,rate=2,mode=1):
        '''mode=0 --> fast
        mode=1 --> no overshoot'''
        self.ppms.write('TEMP {} {} {}'.format(temp,rate,mode))
        
    
    def get_helium_level(self):
        '''returns helium level and when level was updated
        **0** The level reading is over one hour old or an update is in progress but the infonnation is not available yet.
        **1** The level reading is under one hour old.
        **2** The level meter is continuously on and the present reading was taken from the level meter in response to this query.'''
        l=self.ppms.ask('LEVEL?',delay)[:-1].split(',')
        return float(l[0]),float(l[1])
        
        
    def set_bridge_channel_configuration(self,channel=1, excitation=200, power=10):
        '''configures current and power limit'''
        self.ppms.write('BRIDGE {} {} {} 0 0'.format(channel, excitation, power))
        
    def get_bridge_channel_configuration(self,channel=1):
        '''returns channel, current limit, power limit and voltage limit'''
        CH,excitation,power,ac,mode,voltage=self.ppms.ask('BRIDGE? {}'.format(channel))[:-1].split(',')
        return float(excitation),float(power),float(voltage)
        
        
    def purge_seal(self):
        '''purge seal chamber'''
        self.ppms.write('CHAMBER 1')
        
    def vent_seal(self):
        '''purge seal chamber'''
        self.ppms.write('CHAMBER 2')
        
    def pump_continously(self):
        '''pump continously'''
        self.ppms.write('CHAMBER 3')
        
    def vent_continously(self):
        '''vent continously'''
        self.ppms.write('CHAMBER 4')

        
    def chamber_status(self):
        s=self.ppms.ask('CHAMBER?')[0]
        return int(s)
    
    def alarm_tone(self):
        '''makes a beep tone over speakers'''
        self.ppms.write('BEEP 1 1000')

    def clear(self):
        self.ppms.clear()

