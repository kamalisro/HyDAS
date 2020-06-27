# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'File.ui'
#
# Created: Tue Jun 23 09:41:06 2015
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PIL import Image
from PyQt4 import QtCore, QtGui
import sys

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

    

class myLabel(QtGui.QLabel):
    def mousePressEvent(self,event):
        image = QtGui.QImage("C:\Users\Varun\Desktop\HyDaS\Temp\Image3.tif")
    
        (valx,valy) = (event.pos().x(),event.pos().y())
        color = QtGui.QColor.fromRgb(image.pixel(valx,valy))
        if color.isValid():
            rgbColor = '('+str(color.red())+', '+str(color.green())+', '+str(color.blue())+')'
            QtGui.QMessageBox.information(self,
				  "Cursor Location",
				  "Pixel Position = (" + str( event.pos().x() ) +  ", " + str( event.pos().y() )+ ")\t\nRGB Value = " + rgbColor)
             
        else:
            QtGui.QMessageBox.information(self,
				  "Cursor Location",
				  "Pixel Position = (" + str( event.pos().x() ) + ', ' + str( event.pos().y() )+ ")\t\nInvalid Color") 

class Ui_DisplayWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuHelp = QtGui.QMenu(self.menubar)
        self.menuHelp.setObjectName(_fromUtf8("menuHelp"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionOpen_File = QtGui.QAction(MainWindow)
        self.actionOpen_File.setObjectName(_fromUtf8("actionOpen_File"))
        self.actionOpen_File.triggered.connect(self.open_file)
        self.actionSave_File = QtGui.QAction(MainWindow)
        self.actionSave_File.setObjectName(_fromUtf8("actionSave_File"))
        self.actionSave_As = QtGui.QAction(MainWindow)
        self.actionSave_As.setObjectName(_fromUtf8("actionSave_As"))
        self.actionSave_As.triggered.connect(self.save_file)
        self.actionExit = QtGui.QAction(MainWindow)
        self.actionExit.setObjectName(_fromUtf8("actionExit"))
        self.actionExit.triggered.connect(MainWindow.close)
        self.actionHelp = QtGui.QAction(MainWindow)
        self.actionHelp.setObjectName(_fromUtf8("actionExit"))
        self.menuHelp.addAction(self.actionHelp)
        self.menuFile.addAction(self.actionOpen_File)
        self.menuFile.addAction(self.actionSave_File)
        self.menuFile.addAction(self.actionSave_As)
        self.menuFile.addAction(self.actionExit)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.ZoomIn = QtGui.QAction(QtGui.QIcon("C:\Users\Varun\Desktop\HyDaS\GUI Final Codes\Icons\ZoomIn.png"), "Zoom In", MainWindow)
        self.ZoomIn.triggered.connect(self.zoomin)
        self.ZoomOut = QtGui.QAction(QtGui.QIcon("C:\Users\Varun\Desktop\HyDaS\GUI Final Codes\Icons\ZoomOut.png"), "Zoom Out", MainWindow)
        self.ZoomOut.triggered.connect(self.zoomout)
        self.Cursor = QtGui.QAction(QtGui.QIcon("C:\Users\Varun\Desktop\HyDaS\GUI Final Codes\Icons\Cursor.png"), "Cursor", MainWindow)
        self.Cursor.triggered.connect(self.cursr)
        #self.Pan = QtGui.QAction(QtGui.QIcon("C:\Users\Public\Pictures\Sample Pictures\Pan.png"), "Pan", MainWindow)
        self.toolBar = QtGui.QToolBar(MainWindow)
        self.toolBar.addAction(self.ZoomIn)
        self.toolBar.addAction(self.ZoomOut)
        self.toolBar.addAction(self.Cursor)
        #self.toolBar.addAction(self.ZoomPan)
        self.img = Image.open("C:\Users\Varun\Desktop\HyDaS\Temp\Image3.tif")
        self.image = QtGui.QImage("C:\Users\Varun\Desktop\HyDaS\Temp\Image3.tif")
        (x,y) = self.img.size

        self.label = myLabel()
        self.label.setBackgroundRole(QtGui.QPalette.Base)
        self.label.setScaledContents(True)
        self.label.setGeometry(QtCore.QRect(0, 33, x, y))

        self.scrollArea = QtGui.QScrollArea(self.centralwidget)
        self.scrollArea.setBackgroundRole(QtGui.QPalette.Dark)
        self.scrollArea.setWidget(self.label)
        self.scrollArea.setGeometry(QtCore.QRect(0, 33, x, y))
        
        self.pixMap = QtGui.QPixmap(self.image)
        self.label.setPixmap(self.pixMap)

        self.menubar.setGeometry(QtCore.QRect(0, 0, x, 20))
        self.toolBar.setGeometry(QtCore.QRect(0, 20, x, 33))
        MainWindow.resize(x, y+75)
        self.scaleFactor = 1.0

        MainWindow.setWindowFlags(QtCore.Qt.WindowMinimizeButtonHint)       #To disable the Maximizing option
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def cursr(self):
        print "hi"

    def save_file (self):
        name = QtGui.QFileDialog.getSaveFileName(None, 'Save File')      
        
    def open_file (self):
        print "Hi!"

    def zoomin(self):
        self.scaleImage(1.25)

    def zoomout(self):
        if self.scaleFactor>1:
            self.scaleImage(0.8)

        else:
            self.scaleImage(1.0)

    def scaleImage(self,factor):
        self.scaleFactor *= factor
        self.label.resize(self.scaleFactor * self.label.pixmap().size())

        self.adjustScrollBar(self.scrollArea.horizontalScrollBar(), factor)
        self.adjustScrollBar(self.scrollArea.verticalScrollBar(), factor)

    def adjustScrollBar(self, scrollBar, factor):
        scrollBar.setValue(int(factor * scrollBar.value() + ((factor - 1) * scrollBar.pageStep()/2)))


    def close (self):
        self.exit()   

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Viewer (3)", None))
        self.menuFile.setTitle(_translate("MainWindow", "File", None))
        self.menuHelp.setTitle(_translate("MainWindow", "Help", None))
        self.actionOpen_File.setText(_translate("MainWindow", "Open File", None))
        self.actionSave_File.setText(_translate("MainWindow", "Save File", None))
        self.actionSave_As.setText(_translate("MainWindow", "Save As", None))
        self.actionExit.setText(_translate("MainWindow", "Exit", None))
        self.actionHelp.setText(_translate("MainWindow", "About", None))
