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

from os import environ, system
import sys
from PyQt4 import QtCore, QtGui
from libs import chromium, gnash, fonts, openjdk, flash, codecs, nvidia

class MainWindow(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)

	#MainWindow specifications (title, objectname and size)
	#self.setWindowTitle(QtGui.QApplication.translate("Neutrino Project", "Neutrino Project", None, QtGui.QApplication.UnicodeUTF8))
        self.setWindowTitle ("Neutrino Project")
	self.setObjectName("MainWindow")
        self.resize(691, 524)
	screen = QtGui.QDesktopWidget().screenGeometry()
        size =  self.geometry()
        self.move((screen.width()-size.width())/2, (screen.height()-size.height())/2)
	
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
	
	#General System Tools an programs Icon
	icon_system = QtGui.QIcon()
	icon_system.addPixmap(QtGui.QPixmap("imgs/applications-system.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
	
	#General Internet Tools an Programs Icon
	icon_internet = QtGui.QIcon()
        icon_internet.addPixmap(QtGui.QPixmap("imgs/applications-internet.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
	
	#General Office Tools an Programs Icon
	icon_office = QtGui.QIcon()
        icon_office.addPixmap(QtGui.QPixmap("imgs/applications-office.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
	
	#General Multimedia Tools an Programs Icon
	icon_multimedia = QtGui.QIcon()
        icon_multimedia.addPixmap(QtGui.QPixmap("imgs/applications-multimedia.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
	
	#General Games Icon
	icon_games = QtGui.QIcon()
        icon_games.addPixmap(QtGui.QPixmap("imgs/applications-games.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
	
	#General Icon
	icon_other = QtGui.QIcon()
        icon_other.addPixmap(QtGui.QPixmap("imgs/applications-other.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
	
	#Remove button Icon
	icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("imgs/uninstall.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
	
	#Execute button Icon
	icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("imgs/install.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)

	#Nvidia Driver Item
	item = QtGui.QListWidgetItem(self.listWidget)
        item.setIcon(icon_system)
	self.listWidget.item(0).setText(QtGui.QApplication.translate("MainWindow", "Driver Nvidia", None, QtGui.QApplication.UnicodeUTF8))
	
	#Nvidia 173 Driver Item
	item = QtGui.QListWidgetItem(self.listWidget)
        item.setIcon(icon_system)
	self.listWidget.item(1).setText(QtGui.QApplication.translate("MainWindow", "Driver Nvidia 173xx", None, QtGui.QApplication.UnicodeUTF8))
	
	#Nvidia 96 Driver Item
	item = QtGui.QListWidgetItem(self.listWidget)
        item.setIcon(icon_system)
	self.listWidget.item(2).setText(QtGui.QApplication.translate("MainWindow", "Driver Nvidia 96xx", None, QtGui.QApplication.UnicodeUTF8))
	
	#Codecs Item
	item = QtGui.QListWidgetItem(self.listWidget)
        item.setIcon(icon_multimedia)
	self.listWidget.item(3).setText(QtGui.QApplication.translate("MainWindow", "Codecs", None, QtGui.QApplication.UnicodeUTF8))
	
	#LibreOffice Item
	item = QtGui.QListWidgetItem(self.listWidget)
        item.setIcon(icon_office)
	self.listWidget.item(4).setText(QtGui.QApplication.translate("MainWindow", "Suíte LibreOffice", None, QtGui.QApplication.UnicodeUTF8))
	
	#Font Install Item
	item = QtGui.QListWidgetItem(self.listWidget)
        item.setIcon(icon_system)
	self.listWidget.item(5).setText(QtGui.QApplication.translate("MainWindow", "Extra Fonts (MSFonts, etc)", None, QtGui.QApplication.UnicodeUTF8))
	
	#Sudo Setup Item
	item = QtGui.QListWidgetItem(self.listWidget)
        item.setIcon(icon_system)
	self.listWidget.item(6).setText(QtGui.QApplication.translate("MainWindow", "Setup Sudo Usage", None, QtGui.QApplication.UnicodeUTF8))
	
	#OpenJDK Item
	item = QtGui.QListWidgetItem(self.listWidget)
        item.setIcon(icon_system)
	self.listWidget.item(7).setText(QtGui.QApplication.translate("MainWindow", "OpenJDK", None, QtGui.QApplication.UnicodeUTF8))
	
	#Oracle Java Item
	item = QtGui.QListWidgetItem(self.listWidget)
        item.setIcon(icon_system)
	self.listWidget.item(8).setText(QtGui.QApplication.translate("MainWindow", "Java (JRE)", None, QtGui.QApplication.UnicodeUTF8))
	
	#Gnash Plugin Item
        item = QtGui.QListWidgetItem(self.listWidget)
        item.setIcon(icon_internet)
        self.listWidget.item(9).setText(QtGui.QApplication.translate("MainWindow", "Gnash Plugin", None, QtGui.QApplication.UnicodeUTF8))
	
	#Flash Plugin Item
        item = QtGui.QListWidgetItem(self.listWidget)
        item.setIcon(icon_internet)
        self.listWidget.item(10).setText(QtGui.QApplication.translate("MainWindow", "Flash Plugin", None, QtGui.QApplication.UnicodeUTF8))
	
	#Chromium Item
        item = QtGui.QListWidgetItem(self.listWidget)
        item.setIcon(icon_internet)
        self.listWidget.item(11).setText(QtGui.QApplication.translate("MainWindow", "Navegador Chromium", None, QtGui.QApplication.UnicodeUTF8))
	
	#Elementary Item
        item = QtGui.QListWidgetItem(self.listWidget)
        item.setIcon(icon_other)
        self.listWidget.item(12).setText(QtGui.QApplication.translate("MainWindow", "Tema de Ícones Elementary", None, QtGui.QApplication.UnicodeUTF8))
	
	#Faenza Item
        item = QtGui.QListWidgetItem(self.listWidget)
        item.setIcon(icon_other)
        self.listWidget.item(13).setText(QtGui.QApplication.translate("MainWindow", "Tema de Ícones Faenza", None, QtGui.QApplication.UnicodeUTF8))
	
	#GShell Elementary Item
        item = QtGui.QListWidgetItem(self.listWidget)
        item.setIcon(icon_other)
        self.listWidget.item(14).setText(QtGui.QApplication.translate("MainWindow", "Tema Elementary para o Gnome-Shell", None, QtGui.QApplication.UnicodeUTF8))
	
	#GShell Smooth-Inset Item
        item = QtGui.QListWidgetItem(self.listWidget)
        item.setIcon(icon_other)
        self.listWidget.item(15).setText(QtGui.QApplication.translate("MainWindow", "Tema Smooth-Inset para o Gnome-Shell", None, QtGui.QApplication.UnicodeUTF8))
	
	#GShell Atolm Item
        item = QtGui.QListWidgetItem(self.listWidget)
        item.setIcon(icon_other)
        self.listWidget.item(16).setText(QtGui.QApplication.translate("MainWindow", "Tema Atolm para o Gnome-Shell", None, QtGui.QApplication.UnicodeUTF8))
	
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
	
	#Uninstall Button
        self.remove = QtGui.QCommandLinkButton(self.frame)
        self.remove.setMaximumSize(QtCore.QSize(45, 64))
        self.remove.setText("")
	self.remove.setIcon(icon2)
        self.remove.setIconSize(QtCore.QSize(32, 32))
        self.remove.setObjectName("commandLinkButton")
	self.remove.setToolTip(QtGui.QApplication.translate("MainWindow", "Uninstall Selected Program", None, QtGui.QApplication.UnicodeUTF8))
        self.remove.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+-", None, QtGui.QApplication.UnicodeUTF8))
	self.remove.setEnabled(False);
	
	#Add Remove Item Button to Frame Internal Layout
        self.horizontalLayout.addWidget(self.remove)
        
	#Install Button
        self.install_bt = QtGui.QCommandLinkButton(self.frame)
        self.install_bt.setMaximumSize(QtCore.QSize(45, 64))
        self.install_bt.setText("")
        self.install_bt.setIcon(icon4)
        self.install_bt.setIconSize(QtCore.QSize(32, 32))
        self.install_bt.setObjectName("install_bt")
	self.install_bt.setToolTip(QtGui.QApplication.translate("MainWindow", "Install Selected Program", None, QtGui.QApplication.UnicodeUTF8))
        self.install_bt.setShortcut(QtGui.QApplication.translate("MainWindow", "Ctrl+E", None, QtGui.QApplication.UnicodeUTF8))
	
	#Add Install Button to Frame Internal Layout
        self.horizontalLayout.addWidget(self.install_bt)
	
	#Add Frame to MainWindow GridLayout
        self.gridLayout.addWidget(self.frame, 3, 0, 1, 1)
	
	#Internal Functions
	
	#Execute Tasks Function
	def install_fun():
		row = str(self.listWidget.currentRow())
		if row == "0":
			nvidia.install()
		elif row == "1":
			nvidia.install_173()
		elif row == "2":
			nvidia.install_96()
		elif row == "3":
			codecs.install()
		elif row == "4":
			libreoffice.install()
		elif row == "5":
			fonts.install()
		elif row == "6":
			system("beesu python libs/Ssudo.py")
		elif row == "7":
			openjdk.install()
		elif row == "8":
			system("beesu python libs/java.py")
		elif row == "9":
			gnash.install()
		elif row == "10":
			flash.install()
		elif row == "11":
			flash.install()
		elif row == "12":
			system("python libs/elementary.py")
		elif row == "13":
			system("python libs/faenza.py")
		elif row == "14":
			system("python libs/gshell_elementary.py")
		elif row == "15":
			system("python libs/gshell_smooth.py")
		elif row == "16":
			system("python libs/gshell_atolm.py")
		else:
			pass
	
	def description ():
		row = str(self.listWidget.currentRow())
		if row == "0":
			self.textEdit.setText(QtGui.QApplication.translate("Neutrino Project", nvidia.NVIDIA_DESCRIPTION, None, QtGui.QApplication.UnicodeUTF8))
		elif row == "1":
			self.textEdit.clear()
			self.textEdit.setText(QtGui.QApplication.translate("Neutrino Project", nvidia.NVIDIA_173_DESCRIPTION, None, QtGui.QApplication.UnicodeUTF8))
		elif row == "2":
			self.textEdit.clear()
			self.textEdit.setText(QtGui.QApplication.translate("Neutrino Project", nvidia.NVIDIA_96_DESCRIPTION, None, QtGui.QApplication.UnicodeUTF8))
		elif row == "3":
			self.textEdit.clear()
			self.textEdit.setText(QtGui.QApplication.translate("Neutrino Project", codecs.CODEC_DESCRIPTION, None, QtGui.QApplication.UnicodeUTF8))
		elif row == "4":
			self.textEdit.clear()
			self.textEdit.setText(QtGui.QApplication.translate("Neutrino Project", libreoffice.LIBO_DESCRIPTION, None, QtGui.QApplication.UnicodeUTF8))
		elif row == "5":
			self.textEdit.clear()
			self.textEdit.setText(QtGui.QApplication.translate("Neutrino Project", fonts.FONTS_DESCRIPTION, None, QtGui.QApplication.UnicodeUTF8))
		elif row == "6":
			self.textEdit.clear()
			self.textEdit.setText(QtGui.QApplication.translate("Neutrino Project", "Setup Sudo Usage in Fedora", None, QtGui.QApplication.UnicodeUTF8))
		elif row == "7":
			self.textEdit.clear()
			self.textEdit.setText(QtGui.QApplication.translate("Neutrino Project", openjdk.OPENJDK_DESCRIPTION, None, QtGui.QApplication.UnicodeUTF8))
		elif row == "8":
			JAVA_DESCRIPTION = str("The Java Platform Standard Edition Runtime Environment (JRE) contains everything necessary to run applets and applications designed for the java platform. This includes the Java virtual machine, plus the Java platform classes and supporting files.")
			self.textEdit.clear()
			self.textEdit.setText(QtGui.QApplication.translate("Neutrino Project", JAVA_DESCRIPTION, None, QtGui.QApplication.UnicodeUTF8))
		elif row == "9":
			self.textEdit.clear()
			self.textEdit.setText(QtGui.QApplication.translate("Neutrino Project", gnash.GNASH_DESCRIPTION, None, QtGui.QApplication.UnicodeUTF8))
		elif row == "10":
			self.textEdit.clear()
			self.textEdit.setText(QtGui.QApplication.translate("Neutrino Project", flash.FLASH_DESCRIPTION, None, QtGui.QApplication.UnicodeUTF8))
		elif row == "11":
			self.textEdit.clear()
			self.textEdit.setText(QtGui.QApplication.translate("Neutrino Project", chromium.FLASH_DESCRIPTION, None, QtGui.QApplication.UnicodeUTF8))
		elif row == "12":
			ELEMENTARY_DESCRIPTION = str("Tema de Ícones Elementary, para o Gnome.")
			self.textEdit.clear()
			self.textEdit.setText(QtGui.QApplication.translate("Neutrino Project", ELEMENTARY_DESCRIPTION, None, QtGui.QApplication.UnicodeUTF8))
		elif row == "13":
			FAENZA_DESCRIPTION = str("Tema de Ícones Faenza, para o Gnome.")
			self.textEdit.clear()
			self.textEdit.setText(QtGui.QApplication.translate("Neutrino Project", FAENZA_DESCRIPTION, None, QtGui.QApplication.UnicodeUTF8))
		elif row == "14":
			GShell_elementary_DESCRIPTION = str("Tema Elementary para o Gnome-Shell, por Half-Left")
			self.textEdit.clear()
			self.textEdit.setText(QtGui.QApplication.translate("Neutrino Project", GShell_elementary_DESCRIPTION, None, QtGui.QApplication.UnicodeUTF8))
		elif row == "15":
			GShell_smooth_DESCRIPTION = str("Tema Smooth-Inset para o Gnome-Shell, por Half-Left")
			self.textEdit.clear()
			self.textEdit.setText(QtGui.QApplication.translate("Neutrino Project", GShell_smooth_DESCRIPTION, None, QtGui.QApplication.UnicodeUTF8))
		elif row == "16":
			GShell_atolm_DESCRIPTION = str("Tema Atolm para o Gnome-Shell, por Half-Left")
			self.textEdit.clear()
			self.textEdit.setText(QtGui.QApplication.translate("Neutrino Project", GShell_atolm_DESCRIPTION, None, QtGui.QApplication.UnicodeUTF8))

		else:
			print "Ops..."
			
	#Signals and Slots
	
	self.connect(self.install_bt, QtCore.SIGNAL("clicked()"), install_fun)
	self.connect(self.listWidget, QtCore.SIGNAL("currentRowChanged (int)"), description)
	
app = QtGui.QApplication(sys.argv)
main = MainWindow()
main.show()
sys.exit(app.exec_())
