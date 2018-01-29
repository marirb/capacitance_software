# -*- coding: utf-8 -*-
"""
Created on Mon Oct 23 21:29:22 2017

@author: Johannes
"""

import sys
import os
from capacitance_GUI import *
from matplotlib import rc
import matplotlib.pyplot as pl
import numpy as np
from useful_stuff.useful import *
import time
#import visa



from ppms.ppms import BLUE_9T_PPMS
from wk6440a.wk6440a import WK6440
from ah2550a.ah2550a import AH2550A




import logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
# create a file handler
year,month,day=time.gmtime()[:3]
handler = logging.FileHandler('C:/capacitance_GUI/log/log-{}-{}-{}.log'.format(year,month,day))
handler.setLevel(logging.INFO)
# create a logging format
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
# add the handlers to the logger
logger.addHandler(handler)






class GUI_capacitance(QtGui.QMainWindow):

    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self,parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ppms_connected = False
        self.wk_connected = False
        self.ah_connected = False
        

        self.ui.actionsavepng.triggered.connect(self.savepng)
        
        try:
#            self.ppms=BLUE_9T_PPMS()
            self.ppms.set_bridge_channel_configuration(1,500,100)
            T,self.rate,approach=self.ppms.get_temperature_setpoint()
            self.ui.label_setpoint_value.setText(str(T))
            self.ui.label_rate_value.setText(str(self.rate))
            self.ui.label_approach_value.setText(approach)
            index = self.ui.comboBox_approach.findText(approach,QtCore.Qt.MatchFixedString)
            self.ui.comboBox_approach.setCurrentIndex(index)
            temp=self.ppms.get_temperature()
            self.ui.lcd_label_temperature.display(np.round(temp,2))
            logger.info('successfully connected to blue 9T PPMS')
            self.ppms_connected=True
        except:
            logger.info('connection to PPMNS failed')
            error=QtGui.QErrorMessage()
            error.showMessage('connection to PPMS could not be established. check if device is turned on and gpib cable is connected.\n further check that MultiVu siftware is closed and EOS is set to 13')
            error.exec_()
            
        try:
#            self.wk=WK6440()
            f=self.wk.get_freq()
            l=self.wk.get_level()
            s=self.wk.get_speed()
            self.ui.label_WK_frequency_value.setText(str(f))
            self.ui.label_WK_voltage_value.setText(str(l))
            self.ui.label_WK_speed_value.setText(s)
            index = self.ui.comboBox_WK_speed.findText(s, QtCore.Qt.MatchFixedString)
            self.ui.comboBox_WK_speed.setCurrentIndex(index)
            logger.info('successfully connected to WK6440a')
            self.wk_connected=True
        except:
            logger.info('connection to WK6440a failed')
            error=QtGui.QErrorMessage()
            error.showMessage('could not connect to the WK6440a. check if it is turned on and cables are connected')
            error.exec_()
            
        try:
            self.ah=AH2550A()
            l=self.ah.get_voltage()
            a=self.ah.get_average()
            self.ui.label_AH_voltage_value.setText(str(l))
            self.ui.label_AH_average_value.setText(str(a))
            index = self.ui.spinBox_AH_average.setValue(int(a))
            logger.info('successfully connected to AH2550a')
            self.ah_connected = True
        except:
            logger.info('connection to AH2550a failed')
            error=QtGui.QErrorMessage()
            error.showMessage('could not connect to the AH2550a. check if it is turned on and cables are connected')
            error.exec_()
#                       
        

        '''create and connect timers'''
        self.timer_data_wk1_only = QtCore.QTimer(self)
        QtCore.QObject.connect(self.timer_data_wk1_only, QtCore.SIGNAL("timeout()"), self.update_temp_measurment_wk_only)
        
        self.timer_data_wk1 = QtCore.QTimer(self)
        QtCore.QObject.connect(self.timer_data_wk1, QtCore.SIGNAL("timeout()"), self.update_temp_measurment1)
        
        self.timer_data_wk2 = QtCore.QTimer(self)
        QtCore.QObject.connect(self.timer_data_wk2, QtCore.SIGNAL("timeout()"), self.update_temp_measurment2)

        self.timer_data_ah1 = QtCore.QTimer(self)
        QtCore.QObject.connect(self.timer_data_ah1, QtCore.SIGNAL("timeout()"), self.update_temp_measurment1)
                
        self.timer_temp = QtCore.QTimer(self)
        QtCore.QObject.connect(self.timer_temp, QtCore.SIGNAL("timeout()"), self.update_temp)
        if self.ppms_connected:
            self.timer_temp.start(1000)
        else:
            pass
        
#        self.timerplot = QtCore.QTimer(self)
                
        
        '''connect buttons'''        
        self.ui.pushButton_set_temperature.clicked.connect(self.set_temperature)
        self.ui.pushButton_AH_settings.clicked.connect(self.set_ah_settings)
        self.ui.pushButton_WK_settings.clicked.connect(self.set_wk_settings)
        
        self.ui.pushButton_measurement_start.clicked.connect(self.initialize_measurement)
        self.ui.pushButton_measurement_stop.clicked.connect(self.stop_measurement_wk)
        
        
        '''variables'''
        self.running = False
        self.data=np.zeros(6)
        self.t0=0
        self.t=[]
        self.fname=''
        self.T1=0
        self.T2=0
        self.T3=0
        self.delta=0.5
        self.temperature_steps=[]
        self.temperature_index=0
        self.wait=False


    def initialize_measurement(self):
        if self.wk_connected and self.ui.groupBox_WK_settings.isChecked and self.ah_connected and self.ui.groupBox_AH_settings.isChecked:
            error=QtGui.QErrorMessage()
            error.showMessage('both groupboxes for AH and WK are checked: uncheck one of them to be able to start a measurement')
            error.exec_()
        elif self.wk_connected and self.ui.groupBox_WK_settings.isChecked:
            self.create_data_file_wk()
        elif self.ah_connected and self.ui.groupBox_AH_settings.isChecked:
            self.create_data_file_ah()

    def create_data_file_wk(self):
        if self.ppms_connected and self.ui.groupBox_measurement.isChecked():
            voltage=self.wk.get_level()
            freq=self.wk.get_freq()
            temp,self.rate,mode=self.ppms.get_temperature_setpoint()
            bias=self.wk.get_bias_info()
            speed=self.wk.get_speed()        
            self.T1=float(self.ui.lineEdit_measurement_temp_start.text())
            self.T2=float(self.ui.lineEdit_measurement_temp_2.text())
            self.T3=float(self.ui.lineEdit_measurement_temp_final.text())        
            self.fname = str(QtGui.QFileDialog.getSaveFileName(self, 'Filename','','*.txt'))
            print(self.fname)
            data=[]
            date=time.asctime()
            np.savetxt(self.fname, data, delimiter = '\t', header = date + '\n frequency: {} Hz'.format(freq) + '\n voltage: {} V'.format(voltage) + '\n rate: {} K/min'.format(self.rate) +
            '\n bias: {}, {}'.format(bias[0],bias[1]) +
            '\n speed {}'.format(speed) +
            '\n temperature 1,2 and 3: {}, {}, {}'.format(self.T1,self.T2,self.T3) +
            '\n time (s) \t PPMS time (s) \t Status \t PPMS temperature (K) \t field (Oe) \t resistance CH1 \t excitation Ch1 \t sample temperature \t capacitance \t loss D')
            self.ui.label_setpoint_value.setText(str(self.T2)+' K')  
            self.ui.groupBox_temperature.setChecked(False)
            self.ui.groupBox_AH_settings.setChecked(False)
            self.ui.groupBox_WK_settings.setChecked(False)
            self.start_measurement_wk()
        else:
            voltage=self.wk.get_level()
            freq=self.wk.get_freq()
            bias=self.wk.get_bias_info()
            speed=self.wk.get_speed()
            self.fname = str(QtGui.QFileDialog.getSaveFileName(self, 'Filename','','*.txt'))
            print(self.fname)
            print(type(self.fname))
            data=[]
            date=time.asctime()
            np.savetxt(self.fname, data, delimiter = '\t', header = date + '\n frequency: {} Hz'.format(freq) + '\n voltage: {} V'.format(voltage)  +
            '\n bias: {}, {}'.format(bias[0],bias[1]) +
            '\n speed {}'.format(speed) +
            '\n time (s) \t capacitance \t loss D')
            self.start_measurement_wk_only()

            

    
    def start_measurement_wk(self):
        temp=self.ppms.get_temperature()
        if np.abs(temp-self.T1)<0.02:
            self.timer_temp.stop()
            num_points=int(np.abs(self.T1-self.T2)/self.delta)
            self.temperature_steps=np.linspace(self.T1,self.T2,num_points+1)        
            self.running=True
            self.t0=time.time()
            try:
                d=self.ppms.get_important_data()
            except:
                logger.info('error when reading important data from PPMS')
            try:
                t=time.time()-self.t0
                C,D=self.wk.measure_data()
            except:
                logger.info('error when reading important data from WK6440a')
            T=x124321_R2Temp(d[4])
            d=np.hstack([t,d,T,C,D])
            self.data=d        
            self.timer_data_wk1.start(1000)
            self.ppms.set_temperature(self.T2,self.rate,1)
        else:
            self.start_measurement_wk()
            
    def start_measurement_wk_only(self):
        self.running=True
        self.t0=time.time()
        try:
            t=time.time()-self.t0
            C,D=self.wk.measure_data()
        except:
            logger.info('error when reading important data from WK6440a')
        d=np.hstack([t,C,D])  
        self.data=d        
        self.timer_data_wk1_only.start(1000)
        
        
    def stop_measurement_wk(self):
        if self.ppms_connected:
            self.running=False
            self.timer_data_wk1.stop()
            self.timer_data_wk2.stop()
            self.ui.groupBox_temperature.setCheckable(True)
            self.ui.groupBox_temperature.setChecked(True)
            self.timer_temp.start(1000)
        else:
            self.running=False
            self.timer_data_wk1_only.stop()        
        


    def update_temp_measurment1(self):
        temp=self.ppms.get_temperature()
#        temp=self.get_sample_temperature()
        if self.T1>self.T2:
            if (temp-self.temperature_steps[self.temperature_index])<0.02:
                self.update_data_wk()
                self.temperature_index=self.temperature_index+1
            else:
                pass
        else:
            if (self.temperature_steps[self.temperature_index]-temp)<0.02:
                self.update_data_wk()
                self.temperature_index=self.temperature_index+1
            else:
                pass
        if self.temperature_index==len(self.temperature_steps):
            self.timer_data_wk1.stop()
            self.temperature_index=0
            self.running=False
            self.wait=True
            QtCore.QTimer.singleShot(10000, self.wait_for_turnaround)
            print 'wait 10 seconds'
        else:
            pass
        self.ui.lcd_label_temperature.display('{0:.2f}'.format(temp))
        
        
    def update_temp_measurment2(self):
        temp=self.ppms.get_temperature()
#        temp=self.get_sample_temperature()
        if self.T2>self.T3:
            if (temp-self.temperature_steps[self.temperature_index])<0.02:
                self.update_data_wk()
                self.temperature_index=self.temperature_index+1
            else:
                pass
        else:
            if (self.temperature_steps[self.temperature_index]-temp)<0.02:
                self.update_data_wk()
                self.temperature_index=self.temperature_index+1
            else:
                pass
        if self.temperature_index==len(self.temperature_steps):
            self.stop_measurement_wk()
        else:
            pass
        self.ui.lcd_label_temperature.display('{0:.2f}'.format(temp))
        
    def update_temp_measurment_wk_only(self):
        self.update_data_wk_only()


    def wait_for_turnaround(self):
        if self.wait:
            self.wait=False
            num_points=int(np.abs(self.T2-self.T3)/self.delta)
            self.temperature_steps=np.linspace(self.T2,self.T3,num_points+1)
        else:
            pass
        temp=self.ppms.get_temperature()
        if np.abs(temp-self.T2)<0.02:     
            self.running=True
            try:
                d=self.ppms.get_important_data()
            except:
                logger.info('error when reading important data from PPMS')
            try:
                t=time.time()-self.t0
                C,D=self.wk.measure_data()
            except:
                logger.info('error when reading important data from WK6440a')
            T=x124321_R2Temp(d[4])
            d=np.hstack([t,d,T,C,D])
            self.data=np.vstack([self.data,d])
            self.timer_data_wk2.start(1000)
            self.ui.label_setpoint_value.setText(str(self.T3)+' K') 
            self.ppms.set_temperature(self.T3,self.rate,1)
        else:
            self.wait_for_turnaround()
            print(temp)


    def update_data_wk(self):
        try:
            d=self.ppms.get_important_data()
        except:
            logging.info('error when reading important data from PPMS')
        try:
            t=time.time()-self.t0
            C,D=self.wk.measure_data()
        except:
            logger.info('error when reading data from WK6440a')
        T=x124321_R2Temp(d[4])
        d=np.hstack([t,d,T,C,D])
        print(d)
        with open(self.fname,'a') as f:
            f.write('\t'.join(map(str, d))+'\n')
        self.data=np.vstack([self.data,d])
        self.ui.pw1p1.setData(x=self.data[:,7],y=self.data[:,8]) 
        
    def update_data_wk_only(self):
        try:
            t=time.time()-self.t0
            C,D=self.wk.measure_data()
        except:
            logger.info('error when reading data from WK6440a')
        d=np.hstack([t,C,D])
        with open(self.fname,'a') as f:
            f.write('\t'.join(map(str, d))+'\n')
        self.data=np.vstack([self.data,d])
        self.ui.pw1p1.setData(x=self.data[:,0],y=self.data[:,1])
        
    def update_temp(self):
        temp=self.ppms.get_temperature()
        if temp==1.0:
            temp=self.ppms.get_temperature()
        else:
            pass
        self.ui.lcd_label_temperature.display('{0:.2f}'.format(temp))
        
        

    def set_wk_settings(self):
        voltage=float(self.ui.lineEdit_WK_voltage.text()) 
        freq=float(self.ui.lineEdit_WK_frequency.text())
        speed=self.ui.comboBox_WK_speed.currentText()
        self.wk.set_level(voltage)
        self.wk.set_freq(freq)
        self.wk.set_speed(speed)
        self.get_wk_settings()
        
    
    def get_wk_settings(self):
        f=self.wk.get_freq()
        l=self.wk.get_level()
        s=self.wk.get_speed()
        self.ui.label_WK_frequency_value.setText(str(f)+' Hz')
        self.ui.label_WK_voltage_value.setText(str(l)+' V')
        self.ui.label_WK_speed_value.setText(s)
        index = self.ui.comboBox_WK_speed.findText(s, QtCore.Qt.MatchFixedString)
        self.ui.comboBox_WK_speed.setCurrentIndex(index)
     
       
    def set_ah_settings(self):
        voltage = float(self.ui.lineEdit_AH_voltage.text()) 
        average = self.ui.spinBox_AH_average.value()
        self.ah.set_voltage(voltage)
        self.ah.set_average(average)
        self.get_ah_settings()
        
    def get_ah_settings(self):
        l=self.ah.get_voltage()
        a=self.ah.get_average()
        self.ui.label_AH_voltage_value.setText(str(l)+' V')
        self.ui.label_AH_average_value.setText(str(a))
        self.ui.spinBox_AH_average.setValue(int(a))
     
        
    def set_temperature(self):
        temp=float(self.ui.lineEdit_setpoint.text())
        rate=float(self.ui.lineEdit_rate.text())
        mode=self.ui.comboBox_approach.currentIndex()
        self.ppms.set_temperature(temp,rate,mode)
        QtCore.QTimer.singleShot(10, self.get_ppms_settings)
        
        
    def get_ppms_settings(self):
        try:
            temp,self.rate,mode=self.ppms.get_temperature_setpoint()
            self.ui.label_setpoint_value.setText(str(temp)+' K')
            self.ui.label_rate_value.setText(str(self.rate)+' K/min')
            self.ui.label_approach_value.setText(mode)
            index = self.ui.comboBox_approach.findText(mode,QtCore.Qt.MatchFixedString)
            self.ui.comboBox_approach.setCurrentIndex(index)  
        except:
            print('problem get ppms settings')
            logger.info('error in get_ppms_settings')
        

    def savepng(self):
        if self.running==False:
            fname = QtGui.QFileDialog.getSaveFileName(self, 'Save file as png','','*.png')
            if fname:
                pl.rcParams.update(matplotlib_parameters2(size=3,textsize=1.6))
                #cmap=cm.Set1
                #color=[cmap(i) for i in np.linspace(0, 1, 9)]
                pl.rcParams['axes.color_cycle'] = tableau20

                fig,ax=pl.figure(),pl.axes()
                xmin=np.min(self.T[:])
                xmax=np.max(self.T[:])
                ymin=np.min(self.C[:])
                ymax=np.max(self.C[:])
                xrang=xmax-xmin
                yrange=ymax-ymin
                ax.plot(self.T,self.C,'o-',lw=2,markersize=15)
                ax.set_xlabel(r'Temperature (K)')
                ax.set_ylabel(r'Capacitance (pF)')
                ax.set_xlim(xmin-0.02*xrang,xmax+0.02*xrang)
                ax.set_ylim(ymin-0.05*yrange,ymax+0.05*yrange)
                ax.grid(True)
#                pl.legend(loc=1,ncol=1)
#                ax.set_title(fname)
                
                pl.savefig(fname,dpi=150)
                pl.close()



#    def get_sample_temperature(self):
#        try:
#            d=self.ppms.get_important_data()
#        except:
#            logging.info('error when reading important data from PPMS')
#        T=x124321_R2Temp(d[4])
#        return T



if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = GUI_capacitance()
    myapp.show()
    sys.exit(app.exec_())