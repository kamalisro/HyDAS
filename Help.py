# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Help.ui'
#
# Created: Thu Jul 09 11:29:35 2015
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

class Ui_HelpDialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(722, 591)
        self.textBrowser = QtGui.QTextBrowser(Dialog)
        self.textBrowser.setGeometry(QtCore.QRect(0, 0, 721, 591))
        self.textBrowser.setObjectName(_fromUtf8("textBrowser"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.textBrowser.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Times New Roman,serif\'; font-size:16pt; font-weight:600; color:#aa0000;\">About Software:</span><span style=\" font-size:8pt; color:#aa0000;\"> </span></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Times New Roman,serif\'; font-size:12pt;\">This software has been developed to convert Multispectral image into Hyperspectral image. First, Unmixing Coeffient output file is generated using linear Unmixing which is then utilized as an input file for data simulation. Finally, for validation of the obtained Hyperspectral image, the concept of correlation is applied.</span><span style=\" font-size:12pt;\"> </span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"><br /></p>\n"
"<p style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Times New Roman,serif\'; font-size:16pt; font-weight:600; color:#aa0000;\">Multispectral Image:</span></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Times New Roman,serif\'; font-size:12pt;\">Multispectral images are the main type of images acquired by remote sensing (RS) radiometers. Multispectral imagery generally refers to 3 to 10 bands of data that are represented in pixels. Each band is   acquired using a remote sensing radiometer. Each band of the image may be displayed one band at a time as a grey scale image, or in combination of three bands at a time as a colour composite image. Colour composite image display combines three primary colours (red, green and blue) in various proportions producing different colours of the visible spectrum.</span><span style=\" font-size:12pt;\"> </span></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Symbol\'; font-size:12pt;\">·  </span><span style=\" font-family:\'Times New Roman,serif\'; font-size:12pt; font-weight:600;\">True colour composite:</span><span style=\" font-family:\'Times New Roman,serif\'; font-size:12pt;\">  If Multispectral image consists of the three visual primary colour bands (red, green, blue).</span><span style=\" font-size:12pt;\"> </span></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Symbol\'; font-size:12pt;\">·  </span><span style=\" font-family:\'Times New Roman,serif\'; font-size:12pt; font-weight:600;\">False Colour Composite:</span><span style=\" font-family:\'Times New Roman,serif\'; font-size:12pt;\"> The display colour assignment for any band of a multispectral image can be done in an entirely arbitrary manner. In this case, the colour of a target in the displayed image does not have any resemblance to its actual colour.</span><span style=\" font-size:12pt;\"> </span></p>\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Times New Roman,serif\'; font-size:16pt; font-weight:600; color:#aa0000;\">Hyperspectral Image:</span><span style=\" font-size:16pt; color:#aa0000;\"> </span></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Times New Roman,serif\'; font-size:12pt;\">Hyperspectral imaging, like other spectral imaging, collects and processes information from across the electromagnetic spectrum. Hyperspectral imaging creates a large number of images from contiguous regions of the electromagnetic spectrum. This increases sampling of the spectrum (versus multispectral data) and greatly increases the amount of information available to a researcher.</span><span style=\" font-size:12pt;\"> </span></p>\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Times New Roman,serif\'; font-size:16pt; font-weight:600; color:#aa0000;\">Linear Unmixing:</span><span style=\" font-size:16pt; color:#aa0000;\"> </span></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Times New Roman,serif\'; font-size:8pt;\"> </span><span style=\" font-family:\'Times New Roman,serif\'; font-size:12pt;\">Linear Spectral Unmixing determines the relative abundances of materials (urban, vegetation, water etc.) that are depicted in an image. The reflectance at each pixel of the image is assumed to be a linear combination of the reflectance of each material present within the pixel.</span><span style=\" font-size:12pt;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Times New Roman,serif\'; font-size:14pt; font-weight:600;\">Steps:</span><span style=\" font-size:14pt;\"> </span></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Times New Roman,serif\'; font-size:12pt;\">1. From the software’s main menu bar, select Unmixing&gt; Linear &gt; Least Square. A new dialog box appears.</span><span style=\" font-size:12pt;\"> </span></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Times New Roman,serif\'; font-size:12pt;\">2.</span><span style=\" font-family:\'Times New Roman\'; font-size:12pt;\"> </span><span style=\" font-family:\'Times New Roman,serif\'; font-size:12pt;\">Click on Browse and select a MRS image in .hdr format as an input file.</span><span style=\" font-size:12pt;\"> </span></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Times New Roman,serif\'; font-size:12pt;\">3.</span><span style=\" font-family:\'Times New Roman\'; font-size:12pt;\"> </span><span style=\" font-family:\'Times New Roman,serif\'; font-size:12pt;\">Normalized MRS spectra are obtained from ENVI or any other similar software. For Input Normalized Spectra, first select the number of spectra using SpinBox, followed by clicking on ‘+’ ToolButton to upload the respective ASCII files. </span></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Times New Roman,serif\'; font-size:12pt;\">4. At least three normalized spectra (urban, water, vegetation) should be given as input and the maximum shouldn’t exceed the number of bands in the input MRS image.</span><span style=\" font-size:12pt;\"> </span></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Times New Roman,serif\'; font-size:12pt;\">5.</span><span style=\" font-family:\'Times New Roman\'; font-size:12pt;\"> </span><span style=\" font-family:\'Times New Roman,serif\'; font-size:12pt;\">To make the job easier for the user, the dialog box displays the number of spectra files uploaded along with the number of files remaining.</span><span style=\" font-size:12pt;\"> </span></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Times New Roman,serif\'; font-size:12pt;\">6.</span><span style=\" font-family:\'Times New Roman\'; font-size:12pt;\"> </span><span style=\" font-family:\'Times New Roman,serif\'; font-size:12pt;\">Click on ‘Run’ for generating the corresponding Unmixing Coefficients output file in .hdr format.   </span></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Times New Roman,serif\'; font-size:12pt;\">7.</span><span style=\" font-family:\'Times New Roman\'; font-size:12pt;\"> </span><span style=\" font-family:\'Times New Roman,serif\'; font-size:12pt;\">Click on ‘Save’ to select the location to save the output file.</span><span style=\" font-family:\'Times New Roman,serif\'; font-size:8pt;\"> </span></p>\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Times New Roman,serif\'; font-size:8pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Times New Roman,serif\'; font-size:16pt; font-weight:600; color:#aa0000;\">Data Simulation</span><a name=\"_GoBack\"></a><span style=\" font-size:16pt; color:#aa0000;\"> </span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Times New Roman,serif\'; font-size:14pt; font-weight:600;\">Steps:</span><span style=\" font-size:8pt;\"> </span></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Times New Roman,serif\'; font-size:12pt;\">1. From the Software main menu bar, select Data Simulation &gt; Multispectral to Hyperspectral; this opens up a new dialog box. </span></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Times New Roman,serif\'; font-size:12pt;\">2. Click on Browse and select the output file generated by Linear Unmixing as the required input file.</span><span style=\" font-size:12pt;\"> </span></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Times New Roman,serif\'; font-size:12pt;\">3. Normalized HRS spectra are obtained from ENVI or any other similar software. For Input Normalized Spectra, first select the number of spectra using SpinBox, followed by clicking on ‘+’ ToolButton to upload the respective ASCII files. </span></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Times New Roman,serif\'; font-size:12pt;\">4. At least three normalized spectra (urban, water, vegetation) should be given as input and the maximum shouldn’t exceed the number of bands in the input MRS image in Unmixing module.</span><span style=\" font-size:12pt;\"> </span></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Times New Roman,serif\'; font-size:12pt;\">5.</span><span style=\" font-family:\'Times New Roman\'; font-size:12pt;\"> </span><span style=\" font-family:\'Times New Roman,serif\'; font-size:12pt;\">To make the job easier for the user, the dialog box displays the number of spectra files uploaded along with the number of files remaining.</span><span style=\" font-size:12pt;\"> </span></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Times New Roman,serif\'; font-size:12pt;\">6. Click on ‘Run’ for generating the Hyperspectral image.</span><span style=\" font-size:12pt;\"> </span></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Times New Roman,serif\'; font-size:12pt;\">7. Click on ‘Save’ to select the location to save the output image file in .hdr format.</span><span style=\" font-size:12pt;\"> </span></p>\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"><br /></p></body></html>", None))
