# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Spectra.ui'
#
# Created: Thu Jul 23 15:04:30 2015
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui


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

class Ui_SpectraDialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(376, 88)
        self.lineEdit = QtGui.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(110, 10, 251, 20))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.pushButtonLoad = QtGui.QPushButton(Dialog)
        self.pushButtonLoad.setGeometry(QtCore.QRect(115, 50, 75, 23))
        self.pushButtonLoad.setObjectName(_fromUtf8("pushButtonLoad"))
        self.pushButtonLoad.clicked.connect(self.Load)
        self.pushButtonCancel = QtGui.QPushButton(Dialog)
        self.pushButtonCancel.setGeometry(QtCore.QRect(205, 50, 75, 23))
        self.pushButtonCancel.setObjectName(_fromUtf8("pushButtonCancel"))
        self.pushButtonBrowse = QtGui.QPushButton(Dialog)
        self.pushButtonBrowse.setGeometry(QtCore.QRect(20, 10, 75, 23))
        self.pushButtonBrowse.setObjectName(_fromUtf8("pushButtonBrowse"))
        self.pushButtonBrowse.clicked.connect(self.Browse)

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.pushButtonCancel, QtCore.SIGNAL(_fromUtf8("clicked()")), Dialog.close)
        QtCore.QObject.connect(self.pushButtonLoad, QtCore.SIGNAL(_fromUtf8("clicked()")), Dialog.deleteLater)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Spectra Library Viewer", None))
        self.pushButtonLoad.setText(_translate("Dialog", "Load", None))
        self.pushButtonCancel.setText(_translate("Dialog", "Cancel", None))
        self.pushButtonBrowse.setText(_translate("Dialog", "Browse File", None))

    def Browse(self):
        name = QtGui.QFileDialog.getOpenFileName(None, 'Open File')
        self.fileBrowse = str(name)
        self.lineEdit.setText(self.fileBrowse)

    def Load(self):
        import numpy as np
        import pyqtgraph as pg
        
        x = []
        y = []
        file = open (self.fileBrowse, 'r')
        sep = file.read().split('\n')
        file.close()

        try:
            for p in sep:
                xAndy = p.split('\t')
                x.append(float(xAndy[0]))
                y.append(float(xAndy[1]))

            print (x)
            print (y)

            plotItem = pg.plot(title = "Spectra Visualisation")
            plotItem.setXRange(0,2400)
            plotItem.setLabel('bottom', text="Wavelength")
            plotItem.setLabel('left', text="Reflectance")
            plotItem.showAxis('bottom')
            plotItem.showAxis('left')
            plotItem.plot(x, y)

        except Exception,e:
            print e
        

    

