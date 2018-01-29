# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'capacitance_GUI.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import pyqtgraph as pg

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)



class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(1000, 800)
        
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        
        
        '''Temperature groupbox with gridlayout'''
        self.groupBox_temperature = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_temperature.setGeometry(QtCore.QRect(30, 20, 231, 161))
        self.groupBox_temperature.setObjectName(_fromUtf8("groupBox"))
        self.groupBox_temperature.setCheckable(True)
        
        self.gridLayoutWidget = QtGui.QWidget(self.groupBox_temperature)        
        self.gridLayoutWidget.setGeometry(QtCore.QRect(9, 19, 211, 101))
        self.gridLayoutWidget.setObjectName(_fromUtf8("gridLayoutWidget"))
        self.gridLayout_temperature = QtGui.QGridLayout(self.gridLayoutWidget)
        self.gridLayout_temperature.setObjectName(_fromUtf8("gridLayout_temperature"))
        
        self.label_rate = QtGui.QLabel(self.gridLayoutWidget)
        self.label_rate.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_rate.setObjectName(_fromUtf8("label_rate"))
        self.gridLayout_temperature.addWidget(self.label_rate, 1, 0, 1, 1)
        
        self.label_setpoint = QtGui.QLabel(self.gridLayoutWidget)
        self.label_setpoint.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_setpoint.setObjectName(_fromUtf8("label_setpoint"))
        self.gridLayout_temperature.addWidget(self.label_setpoint, 0, 0, 1, 1)
        
        self.label_approach = QtGui.QLabel(self.gridLayoutWidget)
        self.label_approach.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_approach.setObjectName(_fromUtf8("label_approach"))
        self.gridLayout_temperature.addWidget(self.label_approach, 2, 0, 1, 1)
        
        self.lineEdit_setpoint = QtGui.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_setpoint.setObjectName(_fromUtf8("lineEdit_setpoint"))
        self.gridLayout_temperature.addWidget(self.lineEdit_setpoint, 0, 1, 1, 1)
        
        self.lineEdit_rate = QtGui.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_rate.setObjectName(_fromUtf8("lineEdit_rate"))
        self.gridLayout_temperature.addWidget(self.lineEdit_rate, 1, 1, 1, 1)
        
        self.comboBox_approach = QtGui.QComboBox(self.gridLayoutWidget)
        self.comboBox_approach.setObjectName(_fromUtf8("comboBox_approach"))
        self.comboBox_approach.addItem(_fromUtf8(""))
        self.comboBox_approach.addItem(_fromUtf8(""))
#        self.comboBox_approach.addItem(_fromUtf8(""))
        self.gridLayout_temperature.addWidget(self.comboBox_approach, 2, 1, 1, 1)
        
        self.label_setpoint_value = QtGui.QLabel(self.gridLayoutWidget)
        self.label_setpoint_value.setAlignment(QtCore.Qt.AlignCenter)
        self.label_setpoint_value.setObjectName(_fromUtf8("label_setpoint_value"))
        self.gridLayout_temperature.addWidget(self.label_setpoint_value, 0, 2, 1, 1)
        
        self.label_rate_value = QtGui.QLabel(self.gridLayoutWidget)
        self.label_rate_value.setAlignment(QtCore.Qt.AlignCenter)
        self.label_rate_value.setObjectName(_fromUtf8("label_rate_value"))
        self.gridLayout_temperature.addWidget(self.label_rate_value, 1, 2, 1, 1)
        self.label_approach_value = QtGui.QLabel(self.gridLayoutWidget)
        self.label_approach_value.setAlignment(QtCore.Qt.AlignCenter)
        self.label_approach_value.setObjectName(_fromUtf8("label_approach_value"))
        self.gridLayout_temperature.addWidget(self.label_approach_value, 2, 2, 1, 1)
        self.pushButton_set_temperature = QtGui.QPushButton(self.groupBox_temperature)
        self.pushButton_set_temperature.setGeometry(QtCore.QRect(147, 130, 70, 23))
        self.pushButton_set_temperature.setObjectName(_fromUtf8("pushButton"))
        
        
        
        '''Temperature display'''
        self.lcd_label_temperature = QtGui.QLCDNumber(self.centralwidget)
        self.lcd_label_temperature.setGeometry(270,40,90,30)
        self.lcd_label_temperature.setSegmentStyle(QtGui.QLCDNumber.Flat)
        self.lcd_label_temperature.setNumDigits(6)
        palette = self.lcd_label_temperature.palette()
        # foreground color
        palette.setColor(palette.WindowText, QtGui.QColor(255, 0, 0))
        # background color
        palette.setColor(palette.Background, QtGui.QColor(100, 100, 255))
        self.lcd_label_temperature.setPalette(palette)
        
        
        '''AH settings-----------------------------------------------------------------------------------'''
        self.groupBox_AH_settings = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_AH_settings.setGeometry(QtCore.QRect(30, 190, 301, 131))
        self.groupBox_AH_settings.setCheckable(True)
        self.groupBox_AH_settings.setChecked(False)
        self.groupBox_AH_settings.setObjectName(_fromUtf8("groupBox_AH_settings"))
        
        self.pushButton_AH_settings = QtGui.QPushButton(self.groupBox_AH_settings)
        self.pushButton_AH_settings.setGeometry(QtCore.QRect(97, 98, 70, 23))
        self.pushButton_AH_settings.setObjectName(_fromUtf8("pushButton_AH_settings"))
        
        self.gridLayoutWidget_2 = QtGui.QWidget(self.groupBox_AH_settings)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(10, 21, 174, 71))
        self.gridLayoutWidget_2.setObjectName(_fromUtf8("gridLayoutWidget_2"))
        self.gridLayout_AH_settings = QtGui.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_AH_settings.setObjectName(_fromUtf8("gridLayout_AH_settings"))
        
        self.lineEdit_AH_voltage = QtGui.QLineEdit(self.gridLayoutWidget_2)
        self.lineEdit_AH_voltage.setObjectName(_fromUtf8("lineEdit_AH_voltage"))
        self.gridLayout_AH_settings.addWidget(self.lineEdit_AH_voltage, 0, 1, 1, 1)
        
        self.spinBox_AH_average = QtGui.QSpinBox(self.gridLayoutWidget_2)
        self.spinBox_AH_average.setMinimum(1)
        self.spinBox_AH_average.setMaximum(16)
        self.spinBox_AH_average.setProperty("value", 6)
        self.spinBox_AH_average.setObjectName(_fromUtf8("spinBox_AH_average"))
        self.gridLayout_AH_settings.addWidget(self.spinBox_AH_average, 1, 1, 1, 1)
        
        self.label_AH_voltage = QtGui.QLabel(self.gridLayoutWidget_2)
        self.label_AH_voltage.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_AH_voltage.setObjectName(_fromUtf8("label_AH_voltage"))
        self.gridLayout_AH_settings.addWidget(self.label_AH_voltage, 0, 0, 1, 1)
        
        self.label_AH_average = QtGui.QLabel(self.gridLayoutWidget_2)
        self.label_AH_average.setMinimumSize(QtCore.QSize(45, 0))
        self.label_AH_average.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_AH_average.setObjectName(_fromUtf8("label_AH_average"))
        self.gridLayout_AH_settings.addWidget(self.label_AH_average, 1, 0, 1, 1)
        
        self.label_AH_voltage_value = QtGui.QLabel(self.gridLayoutWidget_2)
        self.label_AH_voltage_value.setMinimumSize(QtCore.QSize(60, 0))
        self.label_AH_voltage_value.setObjectName(_fromUtf8("label_AH_voltage_value"))
        self.gridLayout_AH_settings.addWidget(self.label_AH_voltage_value, 0, 2, 1, 1)
        
        self.label_AH_average_value = QtGui.QLabel(self.gridLayoutWidget_2)
        self.label_AH_average_value.setObjectName(_fromUtf8("label_AH_average_value"))
        self.gridLayout_AH_settings.addWidget(self.label_AH_average_value, 1, 2, 1, 1)
        
        self.pushButton_AH_set_zero = QtGui.QPushButton(self.groupBox_AH_settings)
        self.pushButton_AH_set_zero.setGeometry(QtCore.QRect(207, 20, 75, 23))
        self.pushButton_AH_set_zero.setObjectName(_fromUtf8("pushButton_AH_set_zero"))
        
        self.checkBox_AH_zero_on_off = QtGui.QCheckBox(self.groupBox_AH_settings)
        self.checkBox_AH_zero_on_off.setGeometry(QtCore.QRect(210, 48, 60, 17))
        self.checkBox_AH_zero_on_off.setObjectName(_fromUtf8("checkBox_AH_zero_on_off"))
        
        self.label_AH_zero = QtGui.QLabel(self.groupBox_AH_settings)
        self.label_AH_zero.setGeometry(QtCore.QRect(200, 71, 90, 20))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        self.label_AH_zero.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_AH_zero.setFont(font)
        self.label_AH_zero.setFrameShape(QtGui.QFrame.Box)
        self.label_AH_zero.setAlignment(QtCore.Qt.AlignCenter)
        self.label_AH_zero.setObjectName(_fromUtf8("label_AH_zero"))
        
        
        
        '''WK settings-------------------------------------------------------------------------------'''
        self.groupBox_WK_settings = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_WK_settings.setGeometry(QtCore.QRect(30, 340, 191, 161))
        self.groupBox_WK_settings.setCheckable(True)
        self.groupBox_WK_settings.setChecked(False)
        self.groupBox_WK_settings.setObjectName(_fromUtf8("groupBox_WK_settings"))
        
        self.gridLayoutWidget_3 = QtGui.QWidget(self.groupBox_WK_settings)
        self.gridLayoutWidget_3.setGeometry(QtCore.QRect(10, 20, 174, 101))
        self.gridLayoutWidget_3.setObjectName(_fromUtf8("gridLayoutWidget_3"))
        self.gridLayout_WK_settings = QtGui.QGridLayout(self.gridLayoutWidget_3)
        self.gridLayout_WK_settings.setObjectName(_fromUtf8("gridLayout_WK_settings"))
        
        self.lineEdit_WK_voltage = QtGui.QLineEdit(self.gridLayoutWidget_3)
        self.lineEdit_WK_voltage.setObjectName(_fromUtf8("lineEdit_WK_voltage"))
        self.gridLayout_WK_settings.addWidget(self.lineEdit_WK_voltage, 0, 1, 1, 1)
        
        self.label_WK_frequency = QtGui.QLabel(self.gridLayoutWidget_3)
        self.label_WK_frequency.setMinimumSize(QtCore.QSize(50, 0))
        self.label_WK_frequency.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_WK_frequency.setObjectName(_fromUtf8("label_WK_frequency"))
        self.gridLayout_WK_settings.addWidget(self.label_WK_frequency, 1, 0, 1, 1)
        
        self.comboBox_WK_speed = QtGui.QComboBox(self.gridLayoutWidget_3)
        self.comboBox_WK_speed.setObjectName(_fromUtf8("comboBox_WK_speed"))
        self.comboBox_WK_speed.addItem(_fromUtf8(""))
        self.comboBox_WK_speed.addItem(_fromUtf8(""))
        self.comboBox_WK_speed.addItem(_fromUtf8(""))
        self.comboBox_WK_speed.addItem(_fromUtf8(""))
        self.gridLayout_WK_settings.addWidget(self.comboBox_WK_speed, 2, 1, 1, 1)
        
        self.label_WK_speed = QtGui.QLabel(self.gridLayoutWidget_3)
        self.label_WK_speed.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_WK_speed.setObjectName(_fromUtf8("label_WK_speed"))
        self.gridLayout_WK_settings.addWidget(self.label_WK_speed, 2, 0, 1, 1)
        
        self.label_WK_voltage = QtGui.QLabel(self.gridLayoutWidget_3)
        self.label_WK_voltage.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_WK_voltage.setObjectName(_fromUtf8("label_WK_voltage"))
        self.gridLayout_WK_settings.addWidget(self.label_WK_voltage, 0, 0, 1, 1)
        
        self.label_WK_voltage_value = QtGui.QLabel(self.gridLayoutWidget_3)
        self.label_WK_voltage_value.setMinimumSize(QtCore.QSize(60, 0))
        self.label_WK_voltage_value.setAlignment(QtCore.Qt.AlignCenter)
        self.label_WK_voltage_value.setObjectName(_fromUtf8("label_WK_voltage_value"))
        self.gridLayout_WK_settings.addWidget(self.label_WK_voltage_value, 0, 2, 1, 1)
        
        self.label_WK_frequency_value = QtGui.QLabel(self.gridLayoutWidget_3)
        self.label_WK_frequency_value.setAlignment(QtCore.Qt.AlignCenter)
        self.label_WK_frequency_value.setObjectName(_fromUtf8("label_8"))
        self.gridLayout_WK_settings.addWidget(self.label_WK_frequency_value, 1, 2, 1, 1)
        
        self.label_WK_speed_value = QtGui.QLabel(self.gridLayoutWidget_3)
        self.label_WK_speed_value.setAlignment(QtCore.Qt.AlignCenter)
        self.label_WK_speed_value.setObjectName(_fromUtf8("label_WK_speed_value"))
        self.gridLayout_WK_settings.addWidget(self.label_WK_speed_value, 2, 2, 1, 1)
        
        self.lineEdit_WK_frequency = QtGui.QLineEdit(self.gridLayoutWidget_3)
        self.lineEdit_WK_frequency.setObjectName(_fromUtf8("lineEdit_WK_frequency"))
        self.gridLayout_WK_settings.addWidget(self.lineEdit_WK_frequency, 1, 1, 1, 1)
        
        self.pushButton_WK_settings = QtGui.QPushButton(self.groupBox_WK_settings)
        self.pushButton_WK_settings.setGeometry(QtCore.QRect(100, 130, 70, 23))
        self.pushButton_WK_settings.setObjectName(_fromUtf8("pushButton_WK_settings"))
                
        
        
        '''menubar + statusbar'''        
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 883, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuEdit = QtGui.QMenu(self.menubar)
        self.menuEdit.setObjectName(_fromUtf8("menuEdit"))
        
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        self.statusbar.showMessage('flame on motherfuckers!!!')
        
        MainWindow.setStatusBar(self.statusbar)
        self.actionLoad_file = QtGui.QAction(MainWindow)
        self.actionLoad_file.setObjectName(_fromUtf8("actionLoad_file"))
        self.actionStart = QtGui.QAction(MainWindow)
        self.actionStart.setObjectName(_fromUtf8("actionStart"))
        self.actionExit = QtGui.QAction(MainWindow)
        self.actionExit.setObjectName(_fromUtf8("actionExit"))
        self.actionSettings = QtGui.QAction(MainWindow)
        self.actionSettings.setObjectName(_fromUtf8("actionSettings"))
        self.actionsavepng=QtGui.QAction(MainWindow)
        self.actionsavepng.setText('save as png')
        self.actionsavepng.setShortcut('Ctrl+A')
        self.actionsavepng.setStatusTip('Save Picture')
        self.menuFile.addAction(self.actionLoad_file)
        self.menuFile.addAction(self.actionStart)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menuEdit.addAction(self.actionSettings)
        self.menuEdit.addAction(self.actionsavepng)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())


        '''measurement groupbox'''
        self.groupBox_measurement = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_measurement.setGeometry(QtCore.QRect(420, 430, 251, 111))
        self.groupBox_measurement.setObjectName(_fromUtf8("groupBox_measurement"))
        self.groupBox_measurement.setCheckable(True)
        self.groupBox_measurement.setChecked(False)
        self.gridLayoutWidget_4 = QtGui.QWidget(self.groupBox_measurement)
        self.gridLayoutWidget_4.setGeometry(QtCore.QRect(19, 19, 131, 91))
        self.gridLayoutWidget_4.setObjectName(_fromUtf8("gridLayoutWidget_4"))
        self.gridLayout = QtGui.QGridLayout(self.gridLayoutWidget_4)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label_measurement_temp_start = QtGui.QLabel(self.gridLayoutWidget_4)
        self.label_measurement_temp_start.setObjectName(_fromUtf8("label_measurement_temp_start"))
        self.gridLayout.addWidget(self.label_measurement_temp_start, 0, 0, 1, 1)
        self.lineEdit_measurement_temp_final = QtGui.QLineEdit(self.gridLayoutWidget_4)
        self.lineEdit_measurement_temp_final.setObjectName(_fromUtf8("lineEdit_measurement_temp_final"))
        self.gridLayout.addWidget(self.lineEdit_measurement_temp_final, 2, 1, 1, 1)
        self.lineEdit_measurement_temp_2 = QtGui.QLineEdit(self.gridLayoutWidget_4)
        self.lineEdit_measurement_temp_2.setObjectName(_fromUtf8("lineEdit_measurement_temp_2"))
        self.gridLayout.addWidget(self.lineEdit_measurement_temp_2, 1, 1, 1, 1)
        self.lineEdit_measurement_temp_start = QtGui.QLineEdit(self.gridLayoutWidget_4)
        self.lineEdit_measurement_temp_start.setObjectName(_fromUtf8("lineEdit_measurement_temp_start"))
        self.gridLayout.addWidget(self.lineEdit_measurement_temp_start, 0, 1, 1, 1)
        self.label_measurement_temp_2 = QtGui.QLabel(self.gridLayoutWidget_4)
        self.label_measurement_temp_2.setObjectName(_fromUtf8("label_measurement_temp_2"))
        self.gridLayout.addWidget(self.label_measurement_temp_2, 1, 0, 1, 1)
        self.label_measurement_temp_final = QtGui.QLabel(self.gridLayoutWidget_4)
        self.label_measurement_temp_final.setObjectName(_fromUtf8("label_measurement_temp_final"))
        self.gridLayout.addWidget(self.label_measurement_temp_final, 2, 0, 1, 1)
        self.label_measurement_deltaT = QtGui.QLabel(self.gridLayoutWidget_4)
        self.label_measurement_deltaT.setObjectName(_fromUtf8("label_measurement_deltaT"))
        self.gridLayout.addWidget(self.label_measurement_deltaT, 3, 0, 1, 1) 
        self.lineEdit_measurement_deltaT = QtGui.QLineEdit(self.gridLayoutWidget_4)
        self.lineEdit_measurement_deltaT.setObjectName(_fromUtf8("lineEdit_measurement_deltaT"))
        self.gridLayout.addWidget(self.lineEdit_measurement_deltaT, 3, 1, 1, 1)
        
        self.pushButton_measurement_stop = QtGui.QPushButton(self.groupBox_measurement)
        self.pushButton_measurement_stop.setGeometry(QtCore.QRect(166, 58, 75, 23))
        self.pushButton_measurement_stop.setObjectName(_fromUtf8("pushButton_measurement_stop"))
        self.pushButton_measurement_start = QtGui.QPushButton(self.groupBox_measurement)
        self.pushButton_measurement_start.setGeometry(QtCore.QRect(166, 28, 75, 23))
        self.pushButton_measurement_start.setObjectName(_fromUtf8("pushButton_measurement_start"))



        '''Pyqtplot widget'''
        self.widget_pyqtplot = QtGui.QWidget(MainWindow)
        self.widget_pyqtplot.setGeometry(QtCore.QRect(380, 40, 600, 400))
        self.widget_pyqtplot.setObjectName(_fromUtf8("widget"))
        self.l = QtGui.QVBoxLayout()
        self.widget_pyqtplot.setLayout(self.l)
        
        self.pw1 = pg.PlotWidget(name='Plot1')  ## giving the plots names allows us to link their axes together
        self.l.addWidget(self.pw1)
        self.pw1p1=self.pw1.plot()#symbol='o',symbolBrush=(0,255,0), symbolPen='w',symbolSize=5
        self.pw1p1.setPen((255,0,0))
        self.pw1p1.setSymbol('o')
#        self.pw1p1.setSymbolPen('r')
#        self.pw1p1.setSymbolBrush((255,0,0))
#        self.pw1p1.setSymbolSize(5)
        self.pw1.showGrid(x=True, y=True)
        
        
#        self.pw2 = pg.PlotWidget(name='Plot2')
#        self.pw2.showGrid(x=True, y=True)
#        self.l.addWidget(self.pw2)
#        self.pw2p1=self.pw2.plot()



        
        
        '''#######'''
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Capacitance Measurement", None))
        self.groupBox_temperature.setTitle(_translate("MainWindow", "Temperature", None))
        self.label_rate.setText(_translate("MainWindow", "Rate", None))
        self.label_setpoint.setText(_translate("MainWindow", "Setpoint", None))
        self.label_approach.setText(_translate("MainWindow", "Approach", None))
        self.comboBox_approach.setItemText(0, _translate("MainWindow", "fast", None))
        self.comboBox_approach.setItemText(1, _translate("MainWindow", "no overshoot", None))
#        self.comboBox_approach.setItemText(2, _translate("MainWindow", "sweep", None))
        self.label_setpoint_value.setText(_translate("MainWindow", "300 K", None))
        self.label_rate_value.setText(_translate("MainWindow", "1 K/min", None))
        self.label_approach_value.setText(_translate("MainWindow", "no overshoot", None))
        self.pushButton_set_temperature.setText(_translate("MainWindow", "set", None))
        self.groupBox_AH_settings.setTitle(_translate("MainWindow", "AH settings", None))
        self.pushButton_AH_settings.setText(_translate("MainWindow", "set", None))
        self.label_AH_voltage.setText(_translate("MainWindow", "Voltage", None))
        self.label_AH_average.setText(_translate("MainWindow", "Average", None))
        self.label_AH_voltage_value.setText(_translate("MainWindow", "1 V", None))
        self.label_AH_average_value.setText(_translate("MainWindow", "AV=6", None))
        self.pushButton_AH_set_zero.setText(_translate("MainWindow", "set new zero", None))
        self.checkBox_AH_zero_on_off.setText(_translate("MainWindow", "Zero on", None))
        self.label_AH_zero.setText(_translate("MainWindow", "Zero off", None))
        self.groupBox_WK_settings.setTitle(_translate("MainWindow", "WK settings", None))
        self.label_WK_frequency.setText(_translate("MainWindow", "Fequency", None))
        self.comboBox_WK_speed.setItemText(0, _translate("MainWindow", "SLOW", None))
        self.comboBox_WK_speed.setItemText(1, _translate("MainWindow", "MED", None))
        self.comboBox_WK_speed.setItemText(2, _translate("MainWindow", "FAST", None))
        self.comboBox_WK_speed.setItemText(3, _translate("MainWindow", "MAX", None))
        self.label_WK_speed.setText(_translate("MainWindow", "Speed", None))
        self.label_WK_voltage.setText(_translate("MainWindow", "Voltage", None))
#        self.label_WK_voltage_value.setText(_translate("MainWindow", "1 V", None))
#        self.label_WK_frequency_value.setText(_translate("MainWindow", "1 kHz", None))
        self.label_WK_speed_value.setText(_translate("MainWindow", "slow", None))
        self.pushButton_WK_settings.setText(_translate("MainWindow", "set", None))
        self.groupBox_measurement.setTitle(_translate("MainWindow", "Measurement", None))
        self.label_measurement_temp_start.setText(_translate("MainWindow", "Temp_start", None))
        self.label_measurement_temp_2.setText(_translate("MainWindow", "Temp_2", None))
        self.label_measurement_temp_final.setText(_translate("MainWindow", "Temp_final", None))
        self.label_measurement_deltaT.setText('Delta T')        
        self.pushButton_measurement_stop.setText(_translate("MainWindow", "Stop", None))
        self.pushButton_measurement_start.setText(_translate("MainWindow", "Start", None))        
        
        self.menuFile.setTitle(_translate("MainWindow", "file", None))
        self.menuEdit.setTitle(_translate("MainWindow", "edit", None))
        self.actionLoad_file.setText(_translate("MainWindow", "load file", None))
        self.actionStart.setText(_translate("MainWindow", "start", None))
        self.actionExit.setText(_translate("MainWindow", "exit", None))
        self.actionSettings.setText(_translate("MainWindow", "settings", None))

