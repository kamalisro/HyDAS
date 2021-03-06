# -*- coding: utf-8 -*-
from PIL import Image
from PyQt4 import QtCore, QtGui
from ZProf import FileName2,Viewdef,Link
import PlotGraph2,PlotGraphLinked
from NewWin import ChangeValue
from FolderPaths import Path
from HelpDoc import Ui_HelpDialog
#from DisplayImage import Ui_DisplayWindow

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
    def mouseDoubleClickEvent(self,event):

        if Link.InfoWin == 0 and (Link.cursor2 == 1 or Link.linkcursor == 1):
            Link.InfoWin = 1
            #print 'InfoWin:',Link.InfoWin
            Ui_DisplayWindow.window = Labchange()
            Ui_DisplayWindow.window.show()

        (pixx,pixy) = (event.pos().x(),event.pos().y())
        if Link.LinkDisp == 0:
            name = FileName2.File2
            PlotGraph2.PG.plotGraph(name, pixx, pixy)
            return
        elif Link.LinkDisp == 1:
            PlotGraphLinked.PG.plotGraph(pixx,pixy)
            return

    def mousePressEvent(self, event):
        imagepath = str(Path.TempImagePath)
        Ui_DisplayWindow.labelmove.setGeometry(QtCore.QRect(event.pos().x(),event.pos().y()+27, 6, 6))
        if Link.cursor2 == 1:
            image = QtGui.QImage(imagepath+'\Image2.tif')
            (valx, valy) = (event.pos().x(), event.pos().y())
            color = QtGui.QColor.fromRgb(image.pixel(valx, valy))
            if color.isValid():
                rgbColor1 = '(' + str(color.red()) + ', ' + str(color.green()) + ', ' + str(color.blue()) + ')'
                PlotGraph2.PG.showinfo(valx, valy, rgbColor1)
            else:
                PlotGraph2.PG.showinfo(valx, valy)

        elif Link.linkcursor == 1:
            image = QtGui.QImage(imagepath+'\Image2.tif')
            (valx, valy) = (event.pos().x(), event.pos().y())
            color = QtGui.QColor.fromRgb(image.pixel(valx, valy))
            if color.isValid():
                rgbColor1 = '(' + str(color.red()) + ', ' + str(color.green()) + ', ' + str(color.blue()) + ')'
                PlotGraphLinked.PG.showinfo(valx, valy, rgbColor1)

            else:
                PlotGraphLinked.PG.showinfo(valx, valy)



        if Link.DynamicOverlay == 1:
            self.img = Image.open(imagepath+"\Image.tif")
            self.image = QtGui.QImage(imagepath+"\Image.tif")
            (x, y) = self.img.size
            Ui_DisplayWindow.label.setBackgroundRole(QtGui.QPalette.Base)
            Ui_DisplayWindow.label.setScaledContents(True)
            Ui_DisplayWindow.label.setGeometry(QtCore.QRect(0, 33, x, y))
            Ui_DisplayWindow.pixMap = QtGui.QPixmap(self.image)
            Ui_DisplayWindow.label.setPixmap(Ui_DisplayWindow.pixMap)


    def mouseReleaseEvent(self, QMouseEvent):
        if Link.DynamicOverlay == 1:
            imagepath = str(Path.TempImagePath)                     
            self.img = Image.open(imagepath+"\Image2.tif")
            self.image = QtGui.QImage(imagepath+"\Image2.tif")
            (x, y) = self.img.size
            Ui_DisplayWindow.label.setBackgroundRole(QtGui.QPalette.Base)
            Ui_DisplayWindow.label.setScaledContents(True)
            Ui_DisplayWindow.label.setGeometry(QtCore.QRect(0, 33, x, y))
            Ui_DisplayWindow.pixMap = QtGui.QPixmap(self.image)
            Ui_DisplayWindow.label.setPixmap(Ui_DisplayWindow.pixMap)

class Ui_DisplayWindow(object):
    label = None
    pixMap = None
    labelmove=None
    window=None
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

        #self.actionOpen_File = QtGui.QAction(MainWindow,shortcut="ctrl+O")
        #self.actionOpen_File.setObjectName(_fromUtf8("actionOpen_File"))
        #self.actionOpen_File.triggered.connect(self.open_file)
        #self.actionSave_File = QtGui.QAction(MainWindow)
        #self.actionSave_File.setObjectName(_fromUtf8("actionSave_File"))
        self.actionSave_As = QtGui.QAction(MainWindow,shortcut="ctrl+S")
        self.actionSave_As.setObjectName(_fromUtf8("actionSave_As"))
        self.actionSave_As.triggered.connect(self.saveas_file)
        self.menuHelp.triggered.connect(self.ViewHelp)
        self.actionExit = QtGui.QAction(MainWindow,shortcut="ctrl+Q")
        self.actionExit.setObjectName(_fromUtf8("actionExit"))
        self.actionExit.triggered.connect(MainWindow.close)
        self.actionHelp = QtGui.QAction(MainWindow,shortcut="ctrl+H")
        self.actionHelp.setObjectName(_fromUtf8("actionExit"))
        self.menuHelp.addAction(self.actionHelp)
        #self.menuFile.addAction(self.actionOpen_File)
        #self.menuFile.addAction(self.actionSave_File)
        self.menuFile.addAction(self.actionSave_As)
        self.menuFile.addAction(self.actionExit)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        iconpath = str(Path.Icons)
        imagepath = str(Path.TempImagePath)                         
        self.home = QtGui.QAction(QtGui.QIcon(iconpath+"\Home.png"), "Home", MainWindow)
        self.home.triggered.connect(self.get_home)
        self.ZoomIn = QtGui.QAction(QtGui.QIcon(iconpath+"\ZoomIn.png"), "Zoom In", MainWindow)
        self.ZoomIn.triggered.connect(self.zoomin)
        self.ZoomOut = QtGui.QAction(QtGui.QIcon(iconpath+"\ZoomOut.png"), "Zoom Out", MainWindow)
        self.ZoomOut.triggered.connect(self.zoomout)
        self.Cursor = QtGui.QAction(QtGui.QIcon(iconpath+"\Cursor.png"), "Cursor", MainWindow)
        self.Cursor.triggered.connect(self.cursr)
        self.ZProfile = QtGui.QAction(QtGui.QIcon(iconpath+"\Z.png"), "ZProfile", MainWindow)
        self.ZProfile.triggered.connect(self.z_profile)

        self.toolBar = QtGui.QToolBar(MainWindow)
        self.toolBar.addAction(self.home)
        self.toolBar.addAction(self.ZoomIn)
        self.toolBar.addAction(self.ZoomOut)
        self.toolBar.addAction(self.Cursor)
        #self.toolBar.addAction(self.ZoomPan)
        self.toolBar.addAction(self.ZProfile)

        self.img = Image.open(imagepath+"\Image2.tif")
        self.image = QtGui.QImage(imagepath+"\Image2.tif")
        (x,y) = self.img.size

        Ui_DisplayWindow.label = myLabel()
        Ui_DisplayWindow.label.setBackgroundRole(QtGui.QPalette.Base)
        Ui_DisplayWindow.label.setScaledContents(True)
        Ui_DisplayWindow.label.setCursor(QtGui.QCursor(QtCore.Qt.CrossCursor))
        Ui_DisplayWindow.label.setGeometry(QtCore.QRect(0, 33, x, y))

        self.scrollArea = QtGui.QScrollArea(self.centralwidget)
        self.scrollArea.setBackgroundRole(QtGui.QPalette.Dark)
        self.scrollArea.setWidget(Ui_DisplayWindow.label)
        self.scrollArea.setGeometry(QtCore.QRect(0, 33, x, y))
        
        Ui_DisplayWindow.pixMap = QtGui.QPixmap(self.image)
        Ui_DisplayWindow.label.setPixmap(Ui_DisplayWindow.pixMap)

        Ui_DisplayWindow.labelmove = QtGui.QLabel(self.centralwidget)
        Ui_DisplayWindow.labelmove.setGeometry(QtCore.QRect(120, 150, 6, 6))
        font = QtGui.QFont()
        font.setPointSize(5)
        palette= QtGui.QPalette()
        palette.setColor(QtGui.QPalette.Foreground,QtCore.Qt.red)
        Ui_DisplayWindow.labelmove.setPalette(palette)
        #font.setBold(True)
        font.setWeight(10)
        Ui_DisplayWindow.labelmove.setMouseTracking(True)
        Ui_DisplayWindow.labelmove.setFont(font)
        #Ui_DisplayWindow.labelmove.setCursor(QtGui.QCursor(QtCore.Qt.CrossCursor))
        Ui_DisplayWindow.labelmove.setObjectName(_fromUtf8("labelmove"))

        self.menubar.setGeometry(QtCore.QRect(0, 0, x, 20))
        self.toolBar.setGeometry(QtCore.QRect(0, 20, x, 33))
        MainWindow.resize(x, y+75)
        MainWindow.setMaximumSize(QtCore.QSize(x,y+75))
        self.scaleFactor = 1.0

        MainWindow.setWindowFlags(QtCore.Qt.WindowMinimizeButtonHint)       #To disable the Maximizing option
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def cursr(self):
        print "Curser Pressed"
        if Link.InfoWin == 0 and (Link.cursor2 == 0 and Link.linkcursor == 0):
            Link.InfoWin = 1
            Ui_DisplayWindow.window = Labchange()
            Ui_DisplayWindow.window.show()

        if Link.LinkDisp == 1 and Link.linkcursor == 0:
            Link.linkcursor = 1
            return
        elif Link.LinkDisp == 1 and Link.linkcursor == 1:
            Link.linkcursor = 0
            Ui_DisplayWindow.window.close()
            return
        if Link.cursor2 == 0 and Link.LinkDisp == 0:
            Link.cursor2 = 1
            return
        elif Link.cursor2 == 1 and Link.LinkDisp == 0:
            Link.cursor2 = 0
            Ui_DisplayWindow.window.close()
            return

    def saveas_file(self):
        filename= QtGui.QFileDialog.getSaveFileName(None,'Save File',QtCore.QDir.currentPath(),"TIFF Files (*.tif)")
        self.pixMap.save(filename)

    def ViewHelp(self):
        self.window = Software_Help()
        self.window.show()

    def zoomin(self):
        self.scaleImage(1.25)

    def zoomout(self):
        if self.scaleFactor>1:
            self.scaleImage(0.8)

        else:
            self.scaleImage(1.0)

    def get_home(self):
        while self.scaleFactor>1:
            self.scaleImage(0.8)

    def z_profile(self):
        if Link.LinkDisp == 1:
            Link.DispNo2 = 1
            PlotGraphLinked.PG.zprof2()
        else:
            PlotGraph2.PG.zprof()
            Viewdef.Zprof = 2


    def scaleImage(self,factor):
        self.scaleFactor *= factor
        self.label.resize(self.scaleFactor * self.label.pixmap().size())

        self.adjustScrollBar(self.scrollArea.horizontalScrollBar(), factor)
        self.adjustScrollBar(self.scrollArea.verticalScrollBar(), factor)

    def adjustScrollBar(self, scrollBar, factor):
        scrollBar.setValue(int(factor * scrollBar.value() + ((factor - 1) * scrollBar.pageStep()/2)))


    def close (self):
        self.exit()

    def closeEvent(self,event):
        if Link.LinkDisp == 1:
            QtGui.QMessageBox.information(self,"Warning","The Operation cannot be Performed...\nUnLink the Displays, then try again.")
            event.ignore()
            return

        reply= QtGui.QMessageBox.question(self,'Warning',
                                          "You are about to close this window!!",QtGui.QMessageBox.Yes | QtGui.QMessageBox.No,
                                          QtGui.QMessageBox.No)
        if reply== QtGui.QMessageBox.Yes:
            Link.ActiveDisplays -=1
            Link.Open2 = 0
            Link.cursor2 = 0
            Link.linkcursor = 0
            event.accept()
        else:
            event.ignore()


    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Viewer (2)", None))
        self.menuFile.setTitle(_translate("MainWindow", "File", None))
        self.menuHelp.setTitle(_translate("MainWindow", "Help", None))
        #self.actionOpen_File.setText(_translate("MainWindow", "Open File", None))
        #self.actionSave_File.setText(_translate("MainWindow", "Save File", None))
        self.actionSave_As.setText(_translate("MainWindow", "Save As", None))
        self.actionExit.setText(_translate("MainWindow", "Exit", None))
        self.actionHelp.setText(_translate("MainWindow", "About", None))

        Ui_DisplayWindow.labelmove.setText(_translate("MainWindow", "o", None))


class Labchange(QtGui.QDialog, ChangeValue):
    def __init__(self, parent = None):
        QtGui.QMainWindow.__init__(self, parent)
        self.ui = ChangeValue()
        self.ui.setupUi(self)
        self.ui.retranslateUi(self)


class Software_Help (QtGui.QDialog, Ui_HelpDialog):
    def __init__(self, parent = None):
        QtGui.QDialog.__init__(self, parent)
        self.ui = Ui_HelpDialog()
        self.ui.setupUi(self)
        self.ui.retranslateUi(self)         
