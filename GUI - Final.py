import sys
from PyQt4 import QtGui, QtCore
from GUI_Final import *

class MyForm (QtGui.QMainWindow):
	def __init__(self, parent=None): 
		QtGui.QMainWindow.__init__(self, parent)
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)
		self.ui.retranslateUi(self)
		
if __name__ == "__main__":
	app = QtGui.QApplication(sys.argv) 
	myapp = MyForm()
	myapp.show()
	sys.exit(app.exec_())
