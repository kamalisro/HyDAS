
from PyQt4 import QtCore, QtGui
import sys
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

class ChangeValue(QtGui.QWidget):
    valueLabel=''
    def __init__(self):
        QtGui.QWidget.__init__(self)
        self.setupUi(self)
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(300, 500)
        MainWindow.move(20,20)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        ChangeValue.valueLabel = QtGui.QLabel(self.centralwidget)
        ChangeValue.valueLabel.setGeometry(QtCore.QRect(10, 20, 270,300))
        font = QtGui.QFont()
        #font.setFamily(_fromUtf8("Lucida Calligraphy"))
        font.setPointSize(8)
        ChangeValue.valueLabel.setFont(font)
        ChangeValue.valueLabel.setObjectName(_fromUtf8("valueLabel"))
        #MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 300, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        #MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        #MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Cursor Values", None))
        ChangeValue.valueLabel.setText(_translate("MainWindow", "", None))

    def closeEvent(self, QCloseEvent):
        Link.InfoWin = 0
