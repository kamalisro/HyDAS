# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'RGB.ui'
#
# Created: Sat Jul 04 08:33:12 2015
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

import os
from PyQt4 import QtCore, QtGui
from Display3 import Ui_DisplayWindow
from spectral import *
from PIL import Image
import numpy as np
import os

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

class Ui_RGBDialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(520, 285)
        self.pushButton = QtGui.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(180, 240, 75, 23))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton_2 = QtGui.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(270, 240, 75, 23))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.groupBox = QtGui.QGroupBox(Dialog)
        self.groupBox.setGeometry(QtCore.QRect(20, 70, 231, 151))
        self.groupBox.setTitle(_fromUtf8(""))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.widget = QtGui.QWidget(self.groupBox)
        self.widget.setGeometry(QtCore.QRect(0, 0, 231, 141))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.radioButton = QtGui.QRadioButton(self.widget)
        self.radioButton.setGeometry(QtCore.QRect(50, 20, 82, 17))
        self.radioButton.setObjectName(_fromUtf8("radioButton"))
        self.radioButton.toggled.connect(self.RGB)
        self.label_3 = QtGui.QLabel(self.widget)
        self.label_3.setGeometry(QtCore.QRect(10, 110, 41, 21))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.lineEdit = QtGui.QLineEdit(self.widget)
        self.lineEdit.setGeometry(QtCore.QRect(20, 50, 161, 21))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.toolButton_3 = QtGui.QToolButton(self.widget)
        self.toolButton_3.setGeometry(QtCore.QRect(190, 110, 25, 19))
        self.toolButton_3.setObjectName(_fromUtf8("toolButton_3"))  
        self.label = QtGui.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(10, 50, 41, 20))
        self.label.setObjectName(_fromUtf8("label"))
        self.lineEdit_2 = QtGui.QLineEdit(self.widget)
        self.lineEdit_2.setGeometry(QtCore.QRect(20, 80, 161, 21))
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.lineEdit_3 = QtGui.QLineEdit(self.widget)
        self.lineEdit_3.setGeometry(QtCore.QRect(20, 110, 161, 21))
        self.lineEdit_3.setObjectName(_fromUtf8("lineEdit_3"))
        self.toolButton_2 = QtGui.QToolButton(self.widget)
        self.toolButton_2.setGeometry(QtCore.QRect(190, 80, 25, 19))
        self.toolButton_2.setObjectName(_fromUtf8("toolButton_2"))
        self.toolButton = QtGui.QToolButton(self.widget)
        self.toolButton.setGeometry(QtCore.QRect(190, 50, 25, 19))
        self.toolButton.setObjectName(_fromUtf8("toolButton"))
        self.label_2 = QtGui.QLabel(self.widget)
        self.label_2.setGeometry(QtCore.QRect(10, 80, 41, 21))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.line_3 = QtGui.QFrame(self.widget)
        self.line_3.setGeometry(QtCore.QRect(-17, 0, 20, 161))
        self.line_3.setFrameShape(QtGui.QFrame.VLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName(_fromUtf8("line_3"))
        self.groupBox_2 = QtGui.QGroupBox(Dialog)
        self.groupBox_2.setGeometry(QtCore.QRect(270, 70, 231, 151))
        self.groupBox_2.setTitle(_fromUtf8(""))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.widget_2 = QtGui.QWidget(self.groupBox_2)
        self.widget_2.setGeometry(QtCore.QRect(0, 0, 231, 151))
        self.widget_2.setObjectName(_fromUtf8("widget_2"))
        self.toolButton_4 = QtGui.QToolButton(self.widget_2)
        self.toolButton_4.setGeometry(QtCore.QRect(190, 50, 25, 19))
        self.toolButton_4.setObjectName(_fromUtf8("toolButton_4"))
        self.lineEdit_4 = QtGui.QLineEdit(self.widget_2)
        self.lineEdit_4.setGeometry(QtCore.QRect(20, 50, 161, 21))
        self.lineEdit_4.setObjectName(_fromUtf8("lineEdit_4"))
        self.radioButton_2 = QtGui.QRadioButton(self.widget_2)
        self.radioButton_2.setGeometry(QtCore.QRect(50, 20, 82, 17))
        self.radioButton_2.setObjectName(_fromUtf8("radioButton_2"))
        self.radioButton_2.toggled.connect(self.Grey)
        self.groupBox_3 = QtGui.QGroupBox(Dialog)
        self.groupBox_3.setGeometry(QtCore.QRect(40, 20, 441, 41))
        self.groupBox_3.setTitle(_fromUtf8(""))
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.pushButton_3 = QtGui.QPushButton(self.groupBox_3)
        self.pushButton_3.setGeometry(QtCore.QRect(10, 10, 81, 23))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.pushButton_3.clicked.connect(self.browse)
        self.lineEdit_5 = QtGui.QLineEdit(self.groupBox_3)
        self.lineEdit_5.setGeometry(QtCore.QRect(100, 10, 331, 20))
        self.lineEdit_5.setObjectName(_fromUtf8("lineEdit_5"))

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.pushButton_2, QtCore.SIGNAL(_fromUtf8("clicked()")), Dialog.close)
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), Dialog.deleteLater)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def browse(self):
        name = QtGui.QFileDialog.getOpenFileName(None, 'Open File')
        self.lineEdit_5.setText(str(name))
        self.img = open_image(str(name))
        self.img.__class__
        (self.height, self.width, self.band) = self.img.shape

        arr = self.img.load()
        arr.__class__
        zero = arr[0][0][0]
        factor = 7.5/zero
        
        x = 1
        while x<(self.band+1):
            bd = factor*arr[:,:,x-1] 
            while bd[0][x-1]>10 or bd[0][x-1]<-10:
                bd = bd/1.2
            self.final_image = bd.astype(np.uint8)
            image_display = Image.fromarray(self.final_image)
            image_display.save("C:\Users\Varun\Desktop\HyDaS\Temp"+str(x)+".tif")
            x = x+1

    def RGB(self,enabled):
        if enabled:
            self.toolButton.clicked.connect(self.R)
            self.toolButton_2.clicked.connect(self.G)
            self.toolButton_3.clicked.connect(self.B)
            self.pushButton.clicked.connect(self.load1)

    def Grey(self,enabled):
        if enabled:
            self.toolButton_4.clicked.connect(self.GS)
            self.pushButton.clicked.connect(self.load2)

    def GS(self):
        name = QtGui.QFileDialog.getOpenFileName(None, 'Select Band', "C:\Users\Varun\Desktop\HyDaS\Temp")
        name1 = str(name)
        self.lineEdit_4.setText(" Band_"+name1[-6]+name1[-5])
        im2 = Image.open(str(name))
        self.Grey = np.array(im2)

    def R(self):
        name = QtGui.QFileDialog.getOpenFileName(None, 'Select Band', "C:\Users\Varun\Desktop\HyDaS\Temp")
        name1 = str(name)
        self.lineEdit.setText(" Band_"+name1[-6]+name1[-5])
        im = Image.open(str(name))
        self.band1 = np.array(im)

    def G(self):
        name = QtGui.QFileDialog.getOpenFileName(None, 'Select Band', "C:\Users\Varun\Desktop\HyDaS\Temp")
        name1 = str(name)
        self.lineEdit_2.setText(" Band_"+name1[-6]+name1[-5])
        im = Image.open(str(name))
        self.band2 = np.array(im)

    def B(self):
        name = QtGui.QFileDialog.getOpenFileName(None, 'Select Band', "C:\Users\Varun\Desktop\HyDaS\Temp")
        name1 = str(name)
        self.lineEdit_3.setText(" Band_"+name1[-6]+name1[-5])
        im = Image.open(str(name))
        self.band3 = np.array(im)
                
    def load1(self):
        combine = np.dstack((self.band1, self.band2, self.band3))
        final_image = combine.astype(np.uint8)
        self.image_display = Image.fromarray(final_image)
        self.image_display.save("C:\Users\Varun\Desktop\HyDaS\Temp\Image3.tif")
        x = 1
        while x<(self.band+1):
            os.remove("C:\Users\Varun\Desktop\HyDaS\Temp"+str(x)+".tif")
            x = x+1
        self.window = DisplayWindow()
        self.window.show()
        app.exec_()
        
    def load2(self):
        self.GreyIm = Image.fromarray(self.Grey)
        self.GreyIm.save("C:\Users\Varun\Desktop\HyDaS\Temp\Image3.tif")
        x = 1
        while x<(self.band+1):
            os.remove("C:\Users\Varun\Desktop\HyDaS\Temp"+str(x)+".tif")
            x = x+1
        self.window = DisplayWindow()
        self.window.show()
        app.exec_()
        
    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Open Image", None))
        self.pushButton.setText(_translate("Dialog", "Load", None))
        self.pushButton_2.setText(_translate("Dialog", "Cancel", None))
        self.radioButton.setText(_translate("Dialog", "RGB", None))
        self.label_3.setText(_translate("Dialog", "B", None))
        self.toolButton_3.setText(_translate("Dialog", "+", None))
        self.label.setText(_translate("Dialog", "R", None))
        self.toolButton_2.setText(_translate("Dialog", "+", None))
        self.toolButton.setText(_translate("Dialog", "+", None))
        self.label_2.setText(_translate("Dialog", "G", None))
        self.toolButton_4.setText(_translate("Dialog", "+", None))
        self.radioButton_2.setText(_translate("Dialog", "Grey Scale", None))
        self.pushButton_3.setText(_translate("Dialog", "Browse Image", None))

class DisplayWindow (QtGui.QMainWindow, Ui_DisplayWindow):
    def __init__(self, parent = None): 
        QtGui.QDialog.__init__(self, parent)
        self.ui = Ui_DisplayWindow()
        self.ui.setupUi(self)
        self.ui.retranslateUi(self)
