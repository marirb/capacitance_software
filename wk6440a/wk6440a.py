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
from useful_stuff.useful import *
#from matplotlib import rc_params as params

import visa
rm=visa.ResourceManager()



speed=['MAX', 'FAST', 'MED', 'SLOW']
major=['Capacitance', 'Inductance', 'Reactance', 'Susceptance', 'Impedance', 'Admittance']
minor=['Q', 'D', 'Resistance', 'Conductance']
bias_on=['off','on']
bias_mode=['internal','external']


class WK6440:
    '''one argumet: GPIB address, usually 6'''
    
    def __init__(self,GPIB_address=6):
        try:
            self.wk=rm.get_instrument('GPIB0::{}'.format(GPIB_address))
            self.wk.write('*CLS')
        except:
            print('device could not be found. check if connected and GPIB address correct')
            
          
          
    def ask(self, string, delay=0):
        a=self.wk.ask(string,delay)
        return a


        
    def write(self, string):
        try:
            self.wk.write(string)
        except:
            print('couldnt write command')
          
 
         
    def set_freq(self, freq):
        self.wk.write(':MEAS:FREQ {}'.format(int(freq)))



    def get_freq(self):
        f=self.wk.ask(':MEAS:FREQ?')
        return int(float(f))


    def set_level(self,lev):
        self.wk.write(':MEAS:LEV {}'.format(lev))



    def get_level(self):
        l=self.wk.ask(':MEAS:LEV?')
        return np.round(float(l),3)


    def set_speed(self,speed):
        '''valid parameters: "SLOW", "MED", "FAST, "MAX" '''
        self.wk.write(':MEAS:SPEED {}'.format(speed))
            

    def get_speed(self):
        '''returns speed as string: MAX, FAST, MED, SLOW'''
        i=self.wk.ask(':MEAS:SPEED?')
        return speed[int(i)]

            
    def set_AC(self):
        '''set to AC mode'''
        self.wk.write(':MEAS:TEST: AC')

    def set_RDC(self):
        '''set to DC mode --> resistance'''
        self.wk.write(':MEAS:TEST:RDC')

    def set_parallel(self):
        '''set parallel equivalent circuit mode'''
        self.wk.write('MEAS:EQU-CCT PAR')

    def set_serial(self):
        '''set serial equivalent circuit mode'''
        self.wk.write('MEAS:EQU-CCT SER')

        
    def select_CLXBZY(self,meas='C'):
        '''valid parameters are: 'C', 'L','X','B','Z','Y' for first measurement \n
        and 'Q', 'D', 'R' 'G' for second measurement'''
        self.wk.write('MEAS:FUNC:{}'.format(meas))

    
    def measure_data(self):
        '''returns first parameter and second parameter (usually capacitance and loss D)'''
        s = self.wk.ask(':MEAS:TRIG').split( )
        C, R = float(s[0]), float(s[2])
        return C,R
        
        
    def set_internal_bias(self):
        '''selects internal voltage bias'''
        self.wk.write(':MEAS:BIAS VINT')
        
    def set_external_bias(self):
        '''selects extermal voltage bias'''
        self.wk.write(':MEAS:BIAS VEXT')
        
    def bias_on(self):
        '''turns bias on'''
        self.wk.write(':MEAS:BIAS ON')

    def bias_off(self):
        '''turns bias off'''
        self.wk.write(':MEAS:BIAS OFF')

    def get_bias_info(self):
        a,b=self.wk.ask(':MEAS:BIAS-STAT?')[:-1].split(',')
        return bias_on[int(a)],bias_mode[int(b)]












