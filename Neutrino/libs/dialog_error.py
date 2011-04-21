#!/usr/bin env python
# -*- coding: utf-8 -*-

#Projeto Neutrino
#Neutrino's User Interface
#Cleiton Lima <cleitonlima@fedoraproject.org>

#This file is part of Neutrino Project.

#    Neutrino is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.

#    Neutrino is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.

#    You should have received a copy of the GNU General Public License
#    along with Neutrino.  If not, see <http://www.gnu.org/licenses/>.


import sys
from PyQt4 import QtCore, QtGui

class OkCancel(QtGui.QWidget):
	def __init__(self):
		super(OkCancel, self).__init__()
        
		self.initUI()
        
	def initUI(self):
		screen = QtGui.QDesktopWidget().screenGeometry()
		size =  self.geometry()
		self.move((screen.width()-size.width())/2, (screen.height()-size.height())/2)
		file = open("/tmp/neutrino/text_var").read()
		self.setWindowTitle("Test")
		self.gridLayout = QtGui.QGridLayout(self)
		self.gridLayout.setObjectName("gridLayout")
		self.label = QtGui.QLabel(self)
		self.label.setText("")
		self.label.setPixmap(QtGui.QPixmap("imgs/dialog-error.png"))
		self.label.setAlignment(QtCore.Qt.AlignCenter)
		self.label.setObjectName("label")
		self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
		self.label_2 = QtGui.QLabel(self)
		self.label_2.setObjectName("label_2")
		self.label_2.setText(QtGui.QApplication.translate("Neutrino Project", file, None, QtGui.QApplication.UnicodeUTF8))
		self.gridLayout.addWidget(self.label_2, 0, 1, 1, 1)
		self.buttonBox = QtGui.QDialogButtonBox(self)
		self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
		self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Ok)
		self.buttonBox.setObjectName("buttonBox")
		self.gridLayout.addWidget(self.buttonBox, 1, 0, 1, 2)
		
		def mimimi ():
			ok = open("/tmp/neutrino/dialog_var", 'w')
			ok.write("ok")
			ok.close()
			self.close()
	
		def mimimi2():
			ok = open("/tmp/neutrino/dialog_var", 'w')
			ok.write("Cancel")
			ok.close()
			self.close()
	
		QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), mimimi)
		QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), mimimi2)
 