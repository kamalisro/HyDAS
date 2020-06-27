# -*- coding: utf-8 -*-

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

class Ui_HelpDialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(722, 494)
        self.textBrowser = QtGui.QTextBrowser(Dialog)
        self.textBrowser.setGeometry(QtCore.QRect(0, 0, 721, 591))
        self.textBrowser.setObjectName(_fromUtf8("textBrowser"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Help", None))
        self.textBrowser.setHtml(_translate("Dialog", '''<!DOCTYPE html><html><head></head><body style='text-align:justify;margin-right: 20px;margin-left: 20px;'><h1 style='text-align:center;color: blue;'>Remote Sensing Dataset Viewer</h1><h3 style='text-decoration: underline;color: brown'>About Viewer:</h3><p style='text-align: justify;'>This viewer can be used to visualize the Remote Sensing DataSets. The Viewer can be used to view both Mutispectraal as well as Hyperspectral Images (in .hdr format).<br>The Viewer has been made using Open Source tools like PyQt4, Spectral Python(SyPy), PyQt Graph(Python), Matplotlib(Python), Image(Python) to study the spectral imaging and perform operations on the same.<br>Using this Viewer the spectral image can be opened in either Greyscale or RGB format.<br>The Viewer has the folowing options in the Menubar and Toolbar respectively.<br>Menu Bar:<ul><li>File</li><li>Tools</li><li>Help</li></ul><br>Tool Bar:<ul><li>Home</li><li>Zoom In</li><li>Zoom Out</li><li>Cursor</li><li>Z-Profile</li></ul><br></p><h3 style='text-decoration: underline;color:brown'>Functionality:</h3><p style='text-align: justify;'>The different functions of the Viewer are described below:<br><br><b>Opening a file:</b><ul>From the Home Screen Window:<br>Click : 'Remote Sensing Datasets Viewer' > 'Open File'<br>A new Window(Open Image) will open up<br><br>Click : 'Browse Image' Button <br>Locate the File(.hdr) and select the required file.<br><br>Select the required option from CheckBox(Either RGB or Grey Scale). Click on the plus(+) sign/signs to get the required bands.<br>Click 'Load' Button to load the required Combination or a single as required.<br>Click 'Cancel' to close the window.<br></ul><br><br><b>The Viewer Window will open up.</b><br><b>To open another Image perform the same procedure.</b><br><br><h4 style='text-decoration: underline; color:red;'>The Viewer Window</h4><b>The Viwer with the fuctionality is described below:</b><br><br><b>Menu Bar:</b><ul><li>File<ul><li>The File has two options:<br>1. 'Save as' : to save the file combination opened.<br>2. 'Exit' : to exit from the Viewer.</li></ul></li><li>Tools<ul><li>Tools has an Option : 'Link' which furter has two more option:<br>1. 'Link Display' : It will work if two Viewers are opened simultaneously.Linking displays also activates the Dynamic Overlay option. The Liinking being done is Pixel-wise Linking.<br>2. 'Dynamic Overlay On' : This will work only if the Displays are Linked. This functionality temporarily overlays the current image with the image in the Image other viewer when either of the viewer is clicked in Linked state.This feature can be disabled from 'Tools>Link>Dynamic Overlay Off' Option.</li></ul></li><li>Help<ul><li>Open up the Help Document Window.</li></ul></li></ul><br><br><b>Tool Bar:</b><ul><li>Home:<ul><li>Resizes the Image to Original Size if the image is Zoomed in.</li></ul></li><li>Zoom In<ul><li>Zooms in the current image for detailed view.</li></ul></li><li>Zoom Out<ul><li>Zooms out the current Zoomed Image.</li></ul></li><li>Cursor<ul><li>This will open up the 'Cursor Values'. The 'Cursor Values' window displays the following Information when the image is clicked once:<ul><li>Clicked Pixel location</li><li>Geographical Coordinates of the Point in Meters</li><li>Geographical Coordinates of the Point in Degree, Minute and Seconds</li></ul>If the Linked Display feature is on then the 'Cursor Values' window will the Cursor location Information for both the Viewers at the same corresponding Pixel.<br>The Cusor is pressed once to activate the 'Cursor Values' window. Press Cursor twice to deactivate the Windowk. If the 'Cursor Values' window is closed explicitly then it can be reopened by double clicking the Viewer(Until the cursor is not pressed the second time).</li></ul></li><li>ZProfile<ul><li>This will open up the 'Z-Profile' window. The 'Z-Profile' window plots a graph for reflectance values versus Wavelength when the image is double Clicked. Clicking the Zprofile Icon second time opens up another 'Z-Profile' window to compare graph among two or more pixels. Multiple graph Windows can be opened simultaneously.<br>If the Linked Display feature is on as well as the 'Z-Profile' window is opened for both the Viewers then on the two 'Z-Profile' windows, Z-Profile for same pixel location for both Image Viewers is Plotted.<br></li></ul></li></ul></p></body></html>''', None))

