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

class Example(QtGui.QWidget):
  
    def __init__(self):
        super(Example, self).__init__()
        
        self.initUI()
        
    def initUI(self):
	
	self.setWindowTitle("Test")
	self.gridLayout = QtGui.QGridLayout(self)
	self.gridLayout.setMargin(2)
	self.textEdit = QtGui.QTextEdit(self)
	self.gridLayout.addWidget(self.textEdit, 0, 0, 1, 1)
	
	self.hlayout = QtGui.QHBoxLayout(self)
	self.ok = QtGui.QPushButton(self)
	self.ok.setText("Ok")
	self.hlayout.addWidget(self.ok)
	
	self.cancel = QtGui.QPushButton(self)
	self.cancel.setText("Cancelar")
	self.hlayout.addWidget(self.cancel)
	self.gridLayout.addLayout(self.hlayout, 1,0,1,1)
	
	def mimimi ():
		print "mimimi"
	
	self.connect(self.ok, QtCore.SIGNAL("clicked()"), mimimi)
	
if __name__ == '__main__':
  
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    ex.show()
    app.exec_()