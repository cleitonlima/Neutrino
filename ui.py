#!/usr/bin env python
# -*- coding: utf-8 -*-

#Projeto Neutrino
#Neutrino's User Interface
#Cleiton Lima <cleitonlima@fedoraproject.org>
#License: GPLv3

import sys
from PyQt4 import QtCore, QtGui
#from libs.gallium3d import *

class MainWindow(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)

	#MainWindow specifications (title, objectname and size)
	self.setWindowTitle(QtGui.QApplication.translate("Neutrino Project", "Neutrino Project", None, QtGui.QApplication.UnicodeUTF8))
        self.setObjectName("MainWindow")
        self.resize(691, 524)
	
	#MainWindow GridLayout
	self.centralwidget = QtGui.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setMargin(0)
        self.gridLayout.setObjectName("gridLayout")
	self.setCentralWidget(self.centralwidget)
	
	#ListWidget of Neutrino's Functions
        self.listWidget = QtGui.QListWidget(self.centralwidget)
        self.listWidget.setIconSize(QtCore.QSize(32, 32))
        self.listWidget.setObjectName("listWidget")
	
	#ListWidget gridLayout
	self.gridLayout.addWidget(self.listWidget, 0, 0, 1, 1)

	#App Icons
	
	#Nvidia and Nouveau Icon
	#icon = QtGui.QIcon()
	#icon.addPixmap(QtGui.QPixmap("imgs/nvidia.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
	
	#Adobe Flash Plugin Icon
        #icon1 = QtGui.QIcon()
        #icon1.addPixmap(QtGui.QPixmap("imgs/flash.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
	
	#Remove button Icon
	icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("imgs/remove.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
	
	#Add button Icon
	icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("imgs/add.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
	
	#Execute button Icon
	icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("imgs/install.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)

	#Nvidia Driver Item
	#item = QtGui.QListWidgetItem(self.listWidget)
        #item.setIcon(icon)
	#self.listWidget.item(0).setText(QtGui.QApplication.translate("MainWindow", "Driver Nvidia", None, QtGui.QApplication.UnicodeUTF8))
	
	#Adobe Flash Plugin Item
        #item = QtGui.QListWidgetItem(self.listWidget)
        #item.setIcon(icon1)
        #self.listWidget.item(1).setText(QtGui.QApplication.translate("MainWindow", "Adobe Flash Plugin", None, QtGui.QApplication.UnicodeUTF8))
	
	#TextEdit
	self.textEdit = QtGui.QTextEdit(self.centralwidget)
        self.textEdit.setMaximumSize(QtCore.QSize(16777215, 100))
        self.textEdit.setObjectName("textEdit")
	self.textEdit.setReadOnly(True)
        self.gridLayout.addWidget(self.textEdit, 1, 0, 1, 1)
        
	#Buttons Frame
	self.frame = QtGui.QFrame(self.centralwidget)
        self.frame.setMinimumSize(QtCore.QSize(0, 50))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName("frame")
        
	#Buttons Frame Internal Layout
	self.horizontalLayout = QtGui.QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName("horizontalLayout")
	
	#Remove Item Button
        self.remove = QtGui.QCommandLinkButton(self.frame)
        self.remove.setMaximumSize(QtCore.QSize(45, 64))
        self.remove.setText("")
	self.remove.setIcon(icon2)
        self.remove.setIconSize(QtCore.QSize(32, 32))
        self.remove.setObjectName("commandLinkButton")
	self.remove.setToolTip(QtGui.QApplication.translate("MainWindow", "Remover tarefa da lista", None, QtGui.QApplication.UnicodeUTF8))
        self.remove.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+-", None, QtGui.QApplication.UnicodeUTF8))
	
	#Add Remove Item Button to Frame Internal Layout
        self.horizontalLayout.addWidget(self.remove)
        
	#Add Item Button
	self.ad_bt = QtGui.QCommandLinkButton(self.frame)
        self.ad_bt.setMaximumSize(QtCore.QSize(45, 64))
        self.ad_bt.setText("")
        self.ad_bt.setIcon(icon3)
        self.ad_bt.setIconSize(QtCore.QSize(32, 32))
        self.ad_bt.setObjectName("ad_bt")
	self.ad_bt.setToolTip(QtGui.QApplication.translate("MainWindow", "Adicionar Tarefa a lista", None, QtGui.QApplication.UnicodeUTF8))
        self.ad_bt.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl++", None, QtGui.QApplication.UnicodeUTF8))
	
	#Insert Add Item Button to Frame Internal Layout
        self.horizontalLayout.addWidget(self.ad_bt)
	
	#Install Button
        self.install_bt = QtGui.QCommandLinkButton(self.frame)
        self.install_bt.setMaximumSize(QtCore.QSize(45, 64))
        self.install_bt.setText("")
        self.install_bt.setIcon(icon4)
        self.install_bt.setIconSize(QtCore.QSize(32, 32))
        self.install_bt.setObjectName("install_bt")
	self.install_bt.setToolTip(QtGui.QApplication.translate("MainWindow", "Executar tarefas", None, QtGui.QApplication.UnicodeUTF8))
        self.install_bt.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+E", None, QtGui.QApplication.UnicodeUTF8))
	
	#Add Install Button to Frame Internal Layout
        self.horizontalLayout.addWidget(self.install_bt)
	
	#Add Frame to MainWindow GridLayout
        self.gridLayout.addWidget(self.frame, 3, 0, 1, 1)
	
	#DockWidget to Show ListWidget with todo items
        self.dockWidget = QtGui.QDockWidget(self)
        self.dockWidget.setMinimumSize(QtCore.QSize(150, 127))
        self.dockWidget.setFeatures(QtGui.QDockWidget.DockWidgetClosable)
        self.dockWidget.setObjectName("dockWidget_2")
	self.dockWidget.setVisible(False)
        self.dockWidgetContents = QtGui.QWidget()
        self.dockWidgetContents.setObjectName("dockWidgetContents_2")
	self.dockWidget.setWidget(self.dockWidgetContents)
        self.addDockWidget(QtCore.Qt.DockWidgetArea(2), self.dockWidget)
	
	#DockWidget Internal GridLayout
	self.gridLayout_2 = QtGui.QGridLayout(self.dockWidgetContents)
        self.gridLayout_2.setMargin(0)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        
	#ListWidget with todo items
	self.todo = QtGui.QListWidget(self.dockWidgetContents)
        self.todo.setObjectName("listWidget_2")
        self.gridLayout_2.addWidget(self.todo, 0, 0, 1, 1)
	
	#Internal Functions
	def add_task():
		self.dockWidget.setVisible(True)
		self.todo.addItem("First Task")
	
	#Signals and Slots
	
	self.connect(self.ad_bt, QtCore.SIGNAL("clicked()"), add_task)

app = QtGui.QApplication(sys.argv)
main = MainWindow()
main.show()
sys.exit(app.exec_())