# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI_Final.ui'
#
# Created: Tue Jun 23 10:05:17 2015
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from Unmixing_Coeff import Ui_Dialog
from Simulation import Ui_SimDialog
from Help import Ui_HelpDialog
from Spectra import Ui_SpectraDialog
from OpenImage import Ui_RGBDialog1
from Open2 import Ui_RGBDialog2
from ZProf import Link

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
    window1 = None
    window2 = None
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(400, 10)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 400, 10))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuViewer = QtGui.QMenu(self.menubar)
        self.menuViewer.setObjectName(_fromUtf8("menuViewer"))
        self.menuSpectral = QtGui.QMenu(self.menubar)
        self.menuSpectral.setObjectName(_fromUtf8("menuSpectral"))
        self.menuUnmixing = QtGui.QMenu(self.menubar)
        self.menuUnmixing.setObjectName(_fromUtf8("menuUnmixing"))
        self.menuLinear = QtGui.QMenu(self.menuUnmixing)
        self.menuLinear.setObjectName(_fromUtf8("menuLinear"))
        self.menuData_Simulation = QtGui.QMenu(self.menubar)
        self.menuData_Simulation.setObjectName(_fromUtf8("menuData_Simulation"))
        self.menuHelp = QtGui.QMenu(self.menubar)
        self.menuHelp.setObjectName(_fromUtf8("menuHelp"))
        MainWindow.setMenuBar(self.menubar)
        self.actionOpen = QtGui.QAction(MainWindow)
        self.actionOpen.setObjectName(_fromUtf8("actionOpen"))
        self.actionOpen.triggered.connect(self.ImageOpen)
        self.actionNon_Linear = QtGui.QAction(MainWindow)
        self.actionNon_Linear.setObjectName(_fromUtf8("actionNon_Linear"))
        self.actionLeast_Square = QtGui.QAction(MainWindow)
        self.actionLeast_Square.setObjectName(_fromUtf8("actionLeast_Square"))
        self.actionLeast_Square.triggered.connect(self.LinearUnmixing)
        self.actionSpectral_library_Viewer = QtGui.QAction(MainWindow)
        self.actionSpectral_library_Viewer.setObjectName(_fromUtf8("actionSpectral_library_Viewer"))
        self.actionSpectral_library_Viewer.triggered.connect(self.SpectraLibraryViewer)
        self.actionSpectral_Library_Builder = QtGui.QAction(MainWindow)
        self.actionSpectral_Library_Builder.setObjectName(_fromUtf8("actionSpectral_Library_Builder"))
        self.actionSpectra_Normalization = QtGui.QAction(MainWindow)
        self.actionSpectra_Normalization.setObjectName(_fromUtf8("actionSpectra_Normalization"))
        self.actionMultispectral_to_Hyperspectral = QtGui.QAction(MainWindow)
        self.actionMultispectral_to_Hyperspectral.setObjectName(_fromUtf8("actionMultispectral_to_Hyperspectral"))
        self.actionMultispectral_to_Hyperspectral.triggered.connect(self.Simulation)
        self.actionAbout_Software = QtGui.QAction(MainWindow)
        self.actionAbout_Software.setObjectName(_fromUtf8("actionAbout_Software"))
        self.actionAbout_Software.triggered.connect(self.Help)
        self.menuViewer.addAction(self.actionOpen)
        self.menuSpectral.addAction(self.actionSpectral_library_Viewer)
        self.menuSpectral.addAction(self.actionSpectral_Library_Builder)
        self.menuSpectral.addAction(self.actionSpectra_Normalization)
        self.menuLinear.addAction(self.actionLeast_Square)
        self.menuUnmixing.addAction(self.menuLinear.menuAction())
        self.menuUnmixing.addAction(self.actionNon_Linear)
        self.menuData_Simulation.addAction(self.actionMultispectral_to_Hyperspectral)
        self.menuHelp.addAction(self.actionAbout_Software)
        self.menubar.addAction(self.menuViewer.menuAction())
        self.menubar.addAction(self.menuSpectral.menuAction())
        self.menubar.addAction(self.menuUnmixing.menuAction())
        self.menubar.addAction(self.menuData_Simulation.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        
        MainWindow.setWindowFlags(QtCore.Qt.WindowMinimizeButtonHint)       #To disable the Maximizing option
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "HyDaS", None))
        self.menuViewer.setTitle(_translate("MainWindow", "Viewer", None))
        self.menuSpectral.setTitle(_translate("MainWindow", "Spectral\n"
"", None))
        self.menuUnmixing.setTitle(_translate("MainWindow", "Unmixing\n"
"", None))
        self.menuLinear.setTitle(_translate("MainWindow", "Linear\n"
"", None))
        self.menuData_Simulation.setTitle(_translate("MainWindow", "Data Simulation\n"
"", None))
        self.menuHelp.setTitle(_translate("MainWindow", "Help\n"
"", None))
        self.actionNon_Linear.setText(_translate("MainWindow", "Non Linear\n"
"", None))
        self.actionLeast_Square.setText(_translate("MainWindow", "Least Square \n"
"", None))
        self.actionSpectral_library_Viewer.setText(_translate("MainWindow", "Spectral Library Viewer\n"
"", None))
        self.actionSpectral_Library_Builder.setText(_translate("MainWindow", "Spectral Library Builder\n"
"", None))
        self.actionSpectra_Normalization.setText(_translate("MainWindow", "Spectra Normalization\n"
"", None))
        self.actionOpen.setText(_translate("MainWindow", "Open\n"
"", None))
        self.actionMultispectral_to_Hyperspectral.setText(_translate("MainWindow", "Multispectral to Hyperspectral\n"
"", None))
        self.actionAbout_Software.setText(_translate("MainWindow", "About Software\n"
"", None))

    def ImageOpen(self):
        if Link.ActiveDisplays == 0:
            Ui_MainWindow.window1 = OpenImage1()    #.self is VERY VERY IMPORTANT
            Ui_MainWindow.window1.show()      #.self is VERY VERY IMPORTANT
            Link.ActiveOpenImage += 1
            Link.Open1 = 1
        elif Link.ActiveDisplays == 1 and Link.Open2 == 0:
            Ui_MainWindow.window2 = OpenImage2()    #.self is VERY VERY IMPORTANT
            Ui_MainWindow.window2.show()      #.self is VERY VERY IMPORTANT
            Link.ActiveOpenImage += 1
            Link.Open2 = 1
        elif Link.ActiveDisplays == 1 and Link.Open1 == 0:
            Ui_MainWindow.window1 = OpenImage1()    #.self is VERY VERY IMPORTANT
            Ui_MainWindow.window1.show()      #.self is VERY VERY IMPORTANT
            Link.ActiveOpenImage += 1
            Link.Open1 = 1
        else:
            print 'Max Number of Viewers Already Open'


    def SpectraLibraryViewer(self):
        self.window = Spectra_Library_Viewer()
        self.window.show()
        app.exec_()
        
    def LinearUnmixing(self):
        self.window = Linear_Unmixing()
        self.window.show()
        app.exec_()     #VERY VERY IMPORTANT

    def Simulation(self):
        self.window = Data_Simulation()
        self.window.show()
        app.exec_()

    def Help(self):
        self.window = Software_Help()
        self.window.show()
        app.exec_()

class OpenImage1 (QtGui.QDialog, Ui_RGBDialog1):
    def __init__(self, parent = None):
        QtGui.QMainWindow.__init__(self, parent)
        self.ui = Ui_RGBDialog1()
        self.ui.setupUi(self)
        self.ui.retranslateUi(self)

class OpenImage2(QtGui.QDialog, Ui_RGBDialog2):
    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self, parent)
        self.ui = Ui_RGBDialog2()
        self.ui.setupUi(self)
        self.ui.retranslateUi(self)

class Spectra_Library_Viewer (QtGui.QDialog, Ui_SpectraDialog):
    def __init__(self, parent = None):
        QtGui.QDialog.__init__(self, parent)
        self.ui = Ui_SpectraDialog()
        self.ui.setupUi(self)
        self.ui.retranslateUi(self)

class Linear_Unmixing (QtGui.QDialog, Ui_Dialog):
    def __init__(self, parent = None): 
        QtGui.QDialog.__init__(self, parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.retranslateUi(self)

class Data_Simulation (QtGui.QDialog, Ui_SimDialog):
    def __init__(self, parent = None):
        QtGui.QDialog.__init__(self, parent)
        self.ui = Ui_SimDialog()
        self.ui.setupUi(self)
        self.ui.retranslateUi(self)

class Software_Help (QtGui.QDialog, Ui_HelpDialog):
    def __init__(self, parent = None):
        QtGui.QDialog.__init__(self, parent)
        self.ui = Ui_HelpDialog()
        self.ui.setupUi(self)
        self.ui.retranslateUi(self)
