# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'simulation.ui'
#
# Created: Tue Jul 07 22:16:45 2015
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from __future__ import division
from PyQt4 import QtCore, QtGui
import sys
import numpy as np
from spectral import *
from PIL import Image
from Help_Simulation import Ui_HelpDialog
import time

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

class Ui_SimDialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(580, 198)
        self.frame = QtGui.QFrame(Dialog)
        self.frame.setGeometry(QtCore.QRect(0, 0, 576, 195))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.label = QtGui.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(10, 21, 171, 20))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_3 = QtGui.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(10, 50, 71, 21))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.pushButton_cancel = QtGui.QPushButton(self.frame)
        self.pushButton_cancel.setGeometry(QtCore.QRect(330, 120, 75, 23))
        self.pushButton_cancel.setObjectName(_fromUtf8("pushButton_cancel"))
        self.pushButton_cancel.clicked.connect(Dialog.close)
        self.pushButton_input = QtGui.QPushButton(self.frame)
        self.pushButton_input.setGeometry(QtCore.QRect(490, 20, 75, 23))
        self.pushButton_input.setObjectName(_fromUtf8("pushButton_input"))
        self.pushButton_input.clicked.connect(self.ip1)
        self.pushButton_output = QtGui.QPushButton(self.frame)
        self.pushButton_output.setGeometry(QtCore.QRect(490, 50, 75, 23))
        self.pushButton_output.setObjectName(_fromUtf8("pushButton_output"))
        self.pushButton_output.clicked.connect(self.op)      
        self.pushButton_run = QtGui.QPushButton(self.frame)
        self.pushButton_run.setGeometry(QtCore.QRect(240, 120, 75, 23))
        self.pushButton_run.setObjectName(_fromUtf8("pushButton_run"))
        self.pushButton_run.clicked.connect(self.run)
        self.lineEdit_input = QtGui.QLineEdit(self.frame)
        self.lineEdit_input.setGeometry(QtCore.QRect(180, 20, 301, 20))
        self.lineEdit_input.setObjectName(_fromUtf8("lineEdit_input"))
        self.lineEdit_output = QtGui.QLineEdit(self.frame)
        self.lineEdit_output.setGeometry(QtCore.QRect(180, 50, 301, 20))
        self.lineEdit_output.setObjectName(_fromUtf8("lineEdit_output"))
        self.progressBar = QtGui.QProgressBar(self.frame)
        self.progressBar.setGeometry(QtCore.QRect(10, 162, 565, 16))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self.progressBar.minimum = 0
        self.progressBar.maximum = 100
        self.pushButton_help = QtGui.QPushButton(self.frame)
        self.pushButton_help.setGeometry(QtCore.QRect(490, 120, 75, 23))
        self.pushButton_help.setObjectName(_fromUtf8("pushButton_help"))
        self.pushButton_help.clicked.connect(self.Help)
        self.label_4 = QtGui.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(10, 80, 131, 16))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.spinBox = QtGui.QSpinBox(self.frame)
        self.spinBox.setGeometry(QtCore.QRect(180, 80, 42, 22))
        self.spinBox.setObjectName(_fromUtf8("spinBox"))
        self.spinBox.setRange(0,10)
        self.toolButton = QtGui.QToolButton(self.frame)
        self.toolButton.setGeometry(QtCore.QRect(230, 80, 31, 21))
        self.toolButton.setObjectName(_fromUtf8("toolButton"))
        self.toolButton.clicked.connect(self.ip2)
        self.label_2 = QtGui.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(330, 80, 71, 16))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.lineEdit_upload = QtGui.QLineEdit(self.frame)
        self.lineEdit_upload.setGeometry(QtCore.QRect(300, 80, 21, 20))
        self.lineEdit_upload.setObjectName(_fromUtf8("lineEdit_upload"))
        self.lineEdit_rem = QtGui.QLineEdit(self.frame)
        self.lineEdit_rem.setGeometry(QtCore.QRect(430, 80, 21, 20))
        self.lineEdit_rem.setObjectName(_fromUtf8("lineEdit_rem"))
        self.label_5 = QtGui.QLabel(self.frame)
        self.label_5.setGeometry(QtCore.QRect(460, 80, 81, 16))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.lineEdit_upload.setText("0")
        self.lineEdit_rem.setText("0")

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.spinBox, QtCore.SIGNAL(_fromUtf8("valueChanged(QString)")), self.lineEdit_rem.setText)
        QtCore.QObject.connect(self.pushButton_cancel, QtCore.SIGNAL(_fromUtf8("clicked()")), Dialog.close)
        QtCore.QObject.connect(self.pushButton_run, QtCore.SIGNAL(_fromUtf8("clicked()")), Dialog.deleteLater)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def ip1(self):
        name = QtGui.QFileDialog.getOpenFileName(None, 'Open Input File')
        name1 = str(name)
        self.lineEdit_input.setText(name1)
        self.im = open_image(name1)
        self.im.__class__ 

    def ip2(self):
        self.entry = self.spinBox.value()
        NorArr = []                 #Defined an empty array
        i = 1
        while i<(self.entry+1):
            name = QtGui.QFileDialog.getOpenFileName(None, 'Choose Normalized Spectra') 
            nor = np.loadtxt(str(name), usecols=(1,), unpack=True)
            self.lineEdit_upload.setText(str(i))
            self.lineEdit_rem.setText(str(self.entry-i))
            NorArr.append(nor)      #.append adds values to the empty array, for each i
            i = i+1
            
        self.p_hyp = np.column_stack((NorArr))        #Takes the complete array as in input
        print self.p_hyp
        (self.row, self.column) = self.p_hyp.shape
        print self.row
        
    def op(self):
        #self.OutputName = self.lineEdit_output.text()      [How to take input from a lineEdit. Always use '\ ']
        self.name_op = QtGui.QFileDialog.getSaveFileName(None, 'Browse a location to Save')
        self.lineEdit_output.setText(self.name_op)

    def run(self):
        x,y,w=self.im.shape
        cimage = np.zeros((x,y,self.row))
        array = np.zeros(self.row)
        arr=np.arange(1,self.entry+1,dtype=np.float16)             
        for i in range(0,x):
                for j in range(0,y):
                        for k in range(0,w):
                                arr[k]=self.im[i,j,k]
                        arr_t=np.transpose(arr)
                        product=np.dot(self.p_hyp,arr_t)
                        for a in range(0,self.row):
                                cimage[i,j,a]=product[a]
                progress = (i/x)*100
                f_progress = int(progress)
                final_progress = f_progress+1
                self.progressBar.setValue(int(final_progress))
        envi.save_image(str(self.name_op)+'.hdr',cimage,dtype=np.float64,force=True,ext=None,interleave="bil")
        time.sleep(0.500)
        self.w = Popup()
        self.w.setGeometry(QtCore.QRect(560,340,250,80))
        self.w.show()

    def close(self):
        self.exit()

    def Help(self):
        self.window = Software_Help()
        self.window.show()
        app.exec_()    

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Data Simulation", None))
        self.label.setText(_translate("Dialog", "Input Fractional Coefficient Image", None))
        self.label_3.setText(_translate("Dialog", "Output Image", None))
        self.pushButton_run.setText(_translate("Dialog", "Run", None))
        self.pushButton_cancel.setText(_translate("Dialog", "Close", None))
        self.pushButton_input.setText(_translate("Dialog", "Browse", None))
        self.pushButton_output.setText(_translate("Dialog", "Save", None))
        self.pushButton_help.setText(_translate("Dialog", "Help", None))
        self.label_4.setText(_translate("Dialog", "Input Normalized Spectra", None))
        self.toolButton.setText(_translate("Dialog", "+", None))
        self.label_2.setText(_translate("Dialog", "Files Uploaded", None))
        self.label_5.setText(_translate("Dialog", "Files Remaining", None))
        
class Software_Help (QtGui.QMainWindow, Ui_HelpDialog):
    def __init__(self, parent = None):
        QtGui.QDialog.__init__(self, parent)
        self.ui = Ui_HelpDialog()
        self.ui.setupUi(self)
        self.ui.retranslateUi(self)

class Popup(QtGui.QDialog):
    def __init__(self):
        QtGui.QWidget.__init__(self)
        self.setWindowTitle("Message")
        self.widget = QtGui.QWidget(self)
        self.label = QtGui.QLabel("Process Completed.", self.widget)
        self.label.setGeometry(QtCore.QRect(80, 12, 100, 30))
        self.btn = QtGui.QPushButton("OK", self.widget)
        self.btn.setGeometry(QtCore.QRect(92, 42, 75, 20))
        self.btn.clicked.connect(self.close)
