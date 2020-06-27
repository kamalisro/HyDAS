# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Linear_Unmixing.ui'
#
# Created: Tue Jul 07 09:24:05 2015
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from __future__ import division
from PyQt4 import QtCore, QtGui
import sys
import numpy as np
from spectral import *
from PIL import Image
from Help_Linear import Ui_HelpDialog
import sys
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

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(540, 226)
        self.frame = QtGui.QFrame(Dialog)
        self.frame.setGeometry(QtCore.QRect(0, 0, 545, 221))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.label = QtGui.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(10, 21, 71, 20))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_3 = QtGui.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(10, 50, 71, 21))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.pushButton = QtGui.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(190, 150, 75, 23))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton.clicked.connect(self.run)
        self.pushButton_2 = QtGui.QPushButton(self.frame)
        self.pushButton_2.setGeometry(QtCore.QRect(290, 150, 75, 23))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.pushButton_2.clicked.connect(Dialog.close)
        self.pushButton_3 = QtGui.QPushButton(self.frame)
        self.pushButton_3.setGeometry(QtCore.QRect(450, 20, 75, 23))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.pushButton_3.clicked.connect(self.ip1)
        self.pushButton_4 = QtGui.QPushButton(self.frame)
        self.pushButton_4.setGeometry(QtCore.QRect(450, 50, 75, 23))
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.pushButton_4.clicked.connect(self.op)
        self.lineEdit = QtGui.QLineEdit(self.frame)
        self.lineEdit.setGeometry(QtCore.QRect(140, 20, 301, 20))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.lineEdit_3 = QtGui.QLineEdit(self.frame)
        self.lineEdit_3.setGeometry(QtCore.QRect(140, 50, 301, 20))
        self.lineEdit_3.setObjectName(_fromUtf8("lineEdit_3"))
        self.progressBar = QtGui.QProgressBar(self.frame)
        self.progressBar.setGeometry(QtCore.QRect(10, 190, 526, 16))
        self.progressBar.setProperty("value", 0)
        self.progressBar.minimum = 0
        self.progressBar.maximum = 100 
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self.pushButton_help = QtGui.QPushButton(self.frame)
        self.pushButton_help.setGeometry(QtCore.QRect(450, 150, 75, 23))
        self.pushButton_help.setObjectName(_fromUtf8("pushButton_help"))
        self.pushButton_help.clicked.connect(self.Help)
        self.label_4 = QtGui.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(10, 80, 131, 16))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.spinBox = QtGui.QSpinBox(self.frame)
        self.spinBox.setGeometry(QtCore.QRect(140, 80, 42, 22))
        self.spinBox.setObjectName(_fromUtf8("spinBox"))
        self.spinBox.setRange(0,10)
        self.toolButton = QtGui.QToolButton(self.frame)
        self.toolButton.setGeometry(QtCore.QRect(190, 80, 31, 21))
        self.toolButton.setObjectName(_fromUtf8("toolButton"))
        self.toolButton.clicked.connect(self.ip2)
        self.label_2 = QtGui.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(290, 80, 71, 16))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.lineEdit_upload = QtGui.QLineEdit(self.frame)
        self.lineEdit_upload.setGeometry(QtCore.QRect(260, 80, 21, 20))
        self.lineEdit_upload.setObjectName(_fromUtf8("lineEdit_upload"))
        self.lineEdit_rem = QtGui.QLineEdit(self.frame)
        self.lineEdit_rem.setGeometry(QtCore.QRect(260, 110, 21, 20))
        self.lineEdit_rem.setObjectName(_fromUtf8("lineEdit_rem"))
        self.label_5 = QtGui.QLabel(self.frame)
        self.label_5.setGeometry(QtCore.QRect(290, 110, 81, 16))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.lineEdit_upload.setText("0")
        self.lineEdit_rem.setText("0")
        
        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.spinBox, QtCore.SIGNAL(_fromUtf8("valueChanged(QString)")), self.lineEdit_rem.setText)
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), Dialog.deleteLater)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def ip1(self):
        name = QtGui.QFileDialog.getOpenFileName(None, 'Open Input File')
        name1 = str(name)
        self.lineEdit.setText(name1)
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
            
        self.stk = np.column_stack((NorArr))        #Takes the complete array as in input
        print self.stk
        

    def op(self):
        #self.OutputName = self.lineEdit.text()  [How to take input from a lineEdit. Always use '\ ']
        self.name_op = QtGui.QFileDialog.getSaveFileName(None, 'Browse a location to Save')
        self.lineEdit_3.setText(self.name_op)

    def run(self):
        t=np.transpose(self.stk)
        mul=np.dot(t,self.stk)
        from numpy.linalg import inv
        mul_inv=inv(mul)
        z=np.dot(mul_inv,t)
        x,y,w=self.im.shape
        arr=np.arange(1,w+1,dtype=np.float16)
        cimage=np.zeros((x,y,self.entry))                   #self.entry from the SpinBox                 
        for i in range(0,x):
                for j in range(0,y):
                        for k in range(0,w):
                                arr[k]=self.im[i,j,k]
                        arr_t=np.transpose(arr)
                        product=np.dot(z,arr_t)
                        for a in range(0,self.entry):
                                cimage[i,j,a]=product[a]
                progress = (i/x)*100
                f_progress = int(progress)
                final_progress = f_progress+1
                self.progressBar.setValue(int(final_progress))                 
        envi.save_image(str(self.name_op)+'.hdr',cimage,dtype=np.float32,force=True,ext=None,interleave="bil")
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
        Dialog.setWindowTitle(_translate("Dialog", "Linear Unmixing", None))
        self.label.setText(_translate("Dialog", "Input  Image", None))
        self.label_3.setText(_translate("Dialog", "Output Image", None))
        self.pushButton.setText(_translate("Dialog", "Run", None))
        self.pushButton_2.setText(_translate("Dialog", "Close", None))
        self.pushButton_3.setText(_translate("Dialog", "Browse", None))
        self.pushButton_4.setText(_translate("Dialog", "Save", None))
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
        
        

    

