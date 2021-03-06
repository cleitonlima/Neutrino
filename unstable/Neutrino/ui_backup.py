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

from os import environ, system, path
import sys
from PyQt4 import QtCore, QtGui
from libs import chromium, gnash, fonts, openjdk, flash, codecs, nvidia, libreoffice, elementary, faenza, amd
import threading

class MainWindow(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
	
        self.setWindowTitle ("Neutrino Project")
	self.setObjectName("MainWindow")
        self.resize(691, 524)
	screen = QtGui.QDesktopWidget().screenGeometry()
        size =  self.geometry()
        self.move((screen.width()-size.width())/2, (screen.height()-size.height())/2)
	
	self.thread = QtCore.QThread()
	self.thread = worker
	
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
	
	#AMD Driver Item
	item = QtGui.QListWidgetItem(self.listWidget)
        item.setIcon(icon_system)
	self.listWidget.item(3).setText(QtGui.QApplication.translate("MainWindow", "Driver AMD Catalyst", None, QtGui.QApplication.UnicodeUTF8))
	
	#Codecs Item
	item = QtGui.QListWidgetItem(self.listWidget)
        item.setIcon(icon_multimedia)
	self.listWidget.item(4).setText(QtGui.QApplication.translate("MainWindow", "Codecs", None, QtGui.QApplication.UnicodeUTF8))
	
	#LibreOffice Item
	item = QtGui.QListWidgetItem(self.listWidget)
        item.setIcon(icon_office)
	self.listWidget.item(5).setText(QtGui.QApplication.translate("MainWindow", "Suíte LibreOffice", None, QtGui.QApplication.UnicodeUTF8))
	
	#Font Install Item
	item = QtGui.QListWidgetItem(self.listWidget)
        item.setIcon(icon_system)
	self.listWidget.item(6).setText(QtGui.QApplication.translate("MainWindow", "Extra Fonts (MSFonts, etc)", None, QtGui.QApplication.UnicodeUTF8))
	
	#Sudo Setup Item
	item = QtGui.QListWidgetItem(self.listWidget)
        item.setIcon(icon_system)
	self.listWidget.item(7).setText(QtGui.QApplication.translate("MainWindow", "Setup Sudo Usage", None, QtGui.QApplication.UnicodeUTF8))
	
	#OpenJDK Item
	item = QtGui.QListWidgetItem(self.listWidget)
        item.setIcon(icon_system)
	self.listWidget.item(8).setText(QtGui.QApplication.translate("MainWindow", "OpenJDK", None, QtGui.QApplication.UnicodeUTF8))
	
	#Oracle Java Item
	item = QtGui.QListWidgetItem(self.listWidget)
        item.setIcon(icon_system)
	self.listWidget.item(9).setText(QtGui.QApplication.translate("MainWindow", "Java (JRE)", None, QtGui.QApplication.UnicodeUTF8))
	
	#Gnash Plugin Item
        item = QtGui.QListWidgetItem(self.listWidget)
        item.setIcon(icon_internet)
        self.listWidget.item(10).setText(QtGui.QApplication.translate("MainWindow", "Gnash Plugin", None, QtGui.QApplication.UnicodeUTF8))
	
	#Flash Plugin Item
        item = QtGui.QListWidgetItem(self.listWidget)
        item.setIcon(icon_internet)
        self.listWidget.item(11).setText(QtGui.QApplication.translate("MainWindow", "Flash Plugin", None, QtGui.QApplication.UnicodeUTF8))
	
	#Chromium Item
        item = QtGui.QListWidgetItem(self.listWidget)
        item.setIcon(icon_internet)
        self.listWidget.item(12).setText(QtGui.QApplication.translate("MainWindow", "Navegador Chromium", None, QtGui.QApplication.UnicodeUTF8))
	
	#Elementary Item
        item = QtGui.QListWidgetItem(self.listWidget)
        item.setIcon(icon_other)
        self.listWidget.item(13).setText(QtGui.QApplication.translate("MainWindow", "Tema de Ícones Elementary", None, QtGui.QApplication.UnicodeUTF8))
	
	#Elementary Mono Dark Item
        item = QtGui.QListWidgetItem(self.listWidget)
        item.setIcon(icon_other)
        self.listWidget.item(14).setText(QtGui.QApplication.translate("MainWindow", "Tema de Ícones Elementary Mono Dark", None, QtGui.QApplication.UnicodeUTF8))
	
	#Faenza Item
        item = QtGui.QListWidgetItem(self.listWidget)
        item.setIcon(icon_other)
        self.listWidget.item(15).setText(QtGui.QApplication.translate("MainWindow", "Tema de Ícones Faenza", None, QtGui.QApplication.UnicodeUTF8))
	
	#Faenza Dark Item
        item = QtGui.QListWidgetItem(self.listWidget)
        item.setIcon(icon_other)
        self.listWidget.item(16).setText(QtGui.QApplication.translate("MainWindow", "Tema de Ícones Faenza Dark", None, QtGui.QApplication.UnicodeUTF8))
	
	#GShell Elementary Item
        item = QtGui.QListWidgetItem(self.listWidget)
        item.setIcon(icon_other)
        self.listWidget.item(17).setText(QtGui.QApplication.translate("MainWindow", "Tema Elementary para o Gnome-Shell", None, QtGui.QApplication.UnicodeUTF8))
	
	#GShell Smooth-Inset Item
        item = QtGui.QListWidgetItem(self.listWidget)
        item.setIcon(icon_other)
        self.listWidget.item(18).setText(QtGui.QApplication.translate("MainWindow", "Tema Smooth-Inset para o Gnome-Shell", None, QtGui.QApplication.UnicodeUTF8))
	
	#GShell Atolm Item
        item = QtGui.QListWidgetItem(self.listWidget)
        item.setIcon(icon_other)
        self.listWidget.item(19).setText(QtGui.QApplication.translate("MainWindow", "Tema Atolm para o Gnome-Shell", None, QtGui.QApplication.UnicodeUTF8))
	
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
	#self.remove.setEnabled(False)
	
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
	
	self.progress = QtGui.QProgressBar(self.centralwidget)
	self.gridLayout.addWidget(self.progress, 4,0,1,1)
	self.progress.hide()
	
	#Internal Functions
	def message(slot, text):
		QtGui.QMessageBox.information(self, str(slot),QtGui.QApplication.translate("MainWindow", str(text), None, QtGui.QApplication.UnicodeUTF8))
	
	#Execute Tasks Function
	def install_fun():
		row = str(self.listWidget.currentRow())
		if row == "0":
			try:
				message("Information", "Iniciando a tarefa. clique em OK.")
				nvidia.install()
				message("Information", "Processo Concluído com Sucesso.")
			except Exception, e:
				message("Error", "Ocorreu o seguinte erro: %s" % e)	
		elif row == "1":
			try:
				message("Information", "Iniciando a tarefa. clique em OK.")
				nvidia.install_173()
				message("Information", "Processo Concluído com Sucesso.")
			except Exception, e:
				message("Error", "Ocorreu o seguinte erro: %s" % e)	
		elif row == "2":
			try:
				message("Information", "Iniciando a tarefa. clique em OK.")
				nvidia.install_96()
				message("Information", "Processo Concluído com Sucesso.")
			except Exception, e:
				message("Error", "Ocorreu o seguinte erro: %s" % e)	
		elif row == "3":
			try:
				message("Information", "Iniciando a tarefa. clique em OK.")
				amd.install()
				message("Information", "Processo Concluído com Sucesso.")
			except Exception, e:
				message("Error", "Ocorreu o seguinte erro: %s" % e)
		elif row == "4":
			try:
				message("information", "Iniciando a tarefa. Clique em Ok")
				codecs.install()
				message("information", "Processo Concluído com Sucesso.")
			except Exception, e:
				message("critical", "Ocorreu o seguinte erro: %s" % e)	
		elif row == "5":
			try:
				message("Information", "Iniciando a tarefa. clique em OK.")
				libreoffice.install()
				message("Information", "Processo Concluído com Sucesso.")
			except Exception, e:
				message("Error", "Ocorreu o seguinte erro: %s" % e)	
		elif row == "6":
			try:
				message("Information", "Iniciando a tarefa. clique em OK.")
				fonts.install()
				message("Information", "Processo Concluído com Sucesso.")
			except Exception, e:
				message("Error", "Ocorreu o seguinte erro: %s" % e)	
		elif row == "7":
			try:
				message("Information", "Iniciando a tarefa. clique em OK.")
				system("beesu python libs/Ssudo.py")
				message("Information", "Processo Concluído com Sucesso.")
			except Exception, e:
				message("Error", "Ocorreu o seguinte erro: %s" % e)
		elif row == "8":
			try:
				message("Information", "Iniciando a tarefa. clique em OK.")
				openjdk.install()
				message("Information", "Processo Concluído com Sucesso.")
			except Exception, e:
				message("Error", "Ocorreu o seguinte erro: %s" % e)	
		elif row == "9":
			try:
				message("Information", "Iniciando a tarefa. clique em OK.")
				system("beesu python libs/java.py")
				message("Information", "Processo Concluído com Sucesso.")
			except Exception, e:
				message("Error", "Ocorreu o seguinte erro: %s" % e)
		elif row == "10":
			try:
				message("Information", "Iniciando a tarefa. clique em OK.")
				gnash.install()
				message("Information", "Processo Concluído com Sucesso.")
			except Exception, e:
				message("Error", "Ocorreu o seguinte erro: %s" % e)
		elif row == "11":
			try:
				message("Information", "Iniciando a tarefa. clique em OK.")
				flash.install()
				message("Information", "Processo Concluído com Sucesso.")
			except Exception, e:
				message("Error", "Ocorreu o seguinte erro: %s" % e)	
		elif row == "12":
			try:
				message("Information", "Iniciando a tarefa. clique em OK.")
				chromium.install()
				message("Information", "Processo Concluído com Sucesso.")
			except Exception, e:
				message("Error", "Ocorreu o seguinte erro: %s" % e)	
		elif row == "13":
			try:
				message("Information", "Iniciando a tarefa. clique em OK.")
				elementary.install()
				message("Information", "Processo Concluído com Sucesso.")
			except Exception, e:
				message("Error", "Ocorreu o seguinte erro: %s" % e)
		elif row == "14":
			try:
				message("Information", "Iniciando a tarefa. clique em OK.")
				elementary.install_dark()
				message("Information", "Processo Concluído com Sucesso.")
			except Exception, e:
				message("Error", "Ocorreu o seguinte erro: %s" % e)					
		elif row == "15":
			try:
				message("Information", "Iniciando a tarefa. clique em OK.")
				faenza.install()
				message("Information", "Processo Concluído com Sucesso.")
			except Exception, e:
				message("Error", "Ocorreu o seguinte erro: %s" % e)
		elif row == "16":
			try:
				message("Information", "Iniciando a tarefa. clique em OK.")
				faenza.install_dark()
				message("Information", "Processo Concluído com Sucesso.")
			except Exception, e:
				message("Error", "Ocorreu o seguinte erro: %s" % e)
		elif row == "17":
			try:
				message("Information", "Iniciando a tarefa. clique em OK.")
				gshell_elementary.install()
				message("Information", "Processo Concluído com Sucesso.")
			except Exception, e:
				message("Error", "Ocorreu o seguinte erro: %s" % e)	
		elif row == "18":
			try:
				message("Information", "Iniciando a tarefa. Clique em Ok.")
				gshell_smooth.install()
				message("Information", "Processo Concluído com Sucesso.")
			except Exception, e:
				message("Error", "Ocorreu o seguinte erro: %s" % e)		
		elif row == "19":
			try:
				message("Information", "Iniciando a tarefa. clique em OK.")
				gshell_atolm.install()
				message("Information", "Processo Concluído com Sucesso.")
			except Exception, e:
				message("Error", "Ocorreu o seguinte erro: %s" % e)	
		else:
			pass
	
	def remove_enable():
		row = str(self.listWidget.currentRow())
		if row == "8":
			self.remove.setEnabled(True)
		elif row == "10":
			self.remove.setEnabled(True)
		elif row == "11":
			self.remove.setEnabled(True)
		elif row == "12":
			self.remove.setEnabled(True)
		elif row == "13":
			self.remove.setEnabled(True)
		elif row == "14":
			self.remove.setEnabled(True)
		elif row == "15":
			self.remove.setEnabled(True)
		elif row == "16":
			self.remove.setEnabled(True)
		else:
			self.remove.setEnabled(False)
			
	def remove_fun():
		row = str(self.listWidget.currentRow())
		if row == "8":
			try:
				message("Information", "Iniciando a tarefa. clique em OK.")
				openjdk.remove()
				message("Information", "Processo Concluído com Sucesso.")
			except Exception, e:
				message("Error", "Ocorreu o seguinte erro: %s" % e)
		elif row == "10":
			try:
				message("Information", "Iniciando a tarefa. clique em OK.")
				gnash.remove()
				message("Information", "Processo Concluído com Sucesso.")
			except Exception, e:
				message("Error", "Ocorreu o seguinte erro: %s" % e)
		elif row == "11":
			try:
				message("Information", "Iniciando a tarefa. clique em OK.")
				flash.remove()
				message("Information", "Processo Concluído com Sucesso.")
			except Exception, e:
				message("Error", "Ocorreu o seguinte erro: %s" % e)
		elif row == "12":
			try:
				message("Information", "Iniciando a tarefa. clique em OK.")
				chromium.remove()
				message("Information", "Processo Concluído com Sucesso.")
			except Exception, e:
				message("Error", "Ocorreu o seguinte erro: %s" % e)
		elif row == "13":
			try:
				message("Information", "Iniciando a tarefa. clique em OK.")
				elementary.remove()
				message("Information", "Processo Concluído com Sucesso.")
			except Exception, e:
				message("Error", "Ocorreu o seguinte erro: %s" % e)
		elif row == "14":
			try:
				message("Information", "Iniciando a tarefa. clique em OK.")
				elementary.remove()
				message("Information", "Processo Concluído com Sucesso.")
			except Exception, e:
				message("Error", "Ocorreu o seguinte erro: %s" % e)
		elif row == "15":
			try:
				message("Information", "Iniciando a tarefa. clique em OK.")
				faenza.remove()
				message("Information", "Processo Concluído com Sucesso.")
			except Exception, e:
				message("Error", "Ocorreu o seguinte erro: %s" % e)
		elif row == "16":
			try:
				message("Information", "Iniciando a tarefa. clique em OK.")
				faenza.remove()
				message("Information", "Processo Concluído com Sucesso.")
			except Exception, e:
				message("Error", "Ocorreu o seguinte erro: %s" % e)
	
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
			self.textEdit.setText(QtGui.QApplication.translate("Neutrino Project", amd.AMD_DESCRIPTION, None, QtGui.QApplication.UnicodeUTF8))
		elif row == "4":
			self.textEdit.clear()
			self.textEdit.setText(QtGui.QApplication.translate("Neutrino Project", codecs.CODEC_DESCRIPTION, None, QtGui.QApplication.UnicodeUTF8))
		elif row == "5":
			self.textEdit.clear()
			self.textEdit.setText(QtGui.QApplication.translate("Neutrino Project", libreoffice.LIBO_DESCRIPTION, None, QtGui.QApplication.UnicodeUTF8))
		elif row == "6":
			self.textEdit.clear()
			self.textEdit.setText(QtGui.QApplication.translate("Neutrino Project", fonts.FONTS_DESCRIPTION, None, QtGui.QApplication.UnicodeUTF8))
		elif row == "7":
			self.textEdit.clear()
			self.textEdit.setText(QtGui.QApplication.translate("Neutrino Project", "Configura o uso do Sudo no Fedora.", None, QtGui.QApplication.UnicodeUTF8))
		elif row == "8":
			self.textEdit.clear()
			self.textEdit.setText(QtGui.QApplication.translate("Neutrino Project", openjdk.OPENJDK_DESCRIPTION, None, QtGui.QApplication.UnicodeUTF8))
		elif row == "9":
			JAVA_DESCRIPTION = str("O JRE consiste no Java Virtual Machine (JVM), nas classes centrais e bibliotecas de suporte da plataforma Java. O JRE representa a parte de tempo de execução do software Java, que é tudo de que você precisa para executá-lo em um navegador da Web.")
			self.textEdit.clear()
			self.textEdit.setText(QtGui.QApplication.translate("Neutrino Project", JAVA_DESCRIPTION, None, QtGui.QApplication.UnicodeUTF8))
		elif row == "10":
			self.textEdit.clear()
			self.textEdit.setText(QtGui.QApplication.translate("Neutrino Project", gnash.GNASH_DESCRIPTION, None, QtGui.QApplication.UnicodeUTF8))
		elif row == "11":
			self.textEdit.clear()
			self.textEdit.setText(QtGui.QApplication.translate("Neutrino Project", flash.FLASH_DESCRIPTION, None, QtGui.QApplication.UnicodeUTF8))
		elif row == "12":
			self.textEdit.clear()
			self.textEdit.setText(QtGui.QApplication.translate("Neutrino Project", chromium.CHROMIUM_DESCRIPTION, None, QtGui.QApplication.UnicodeUTF8))
		elif row == "13":
			self.textEdit.clear()
			self.textEdit.setText(QtGui.QApplication.translate("Neutrino Project", elementary.elementary_DESCRIPTION, None, QtGui.QApplication.UnicodeUTF8))
		elif row == "14":
			self.textEdit.clear()
			self.textEdit.setText(QtGui.QApplication.translate("Neutrino Project", elementary.elementarydark_DESCRIPTION, None, QtGui.QApplication.UnicodeUTF8))
		elif row == "15":
			FAENZA_DESCRIPTION = str("Tema de Ícones Faenza, para o Gnome.")
			self.textEdit.clear()
			self.textEdit.setText(QtGui.QApplication.translate("Neutrino Project", faenza.FAENZA_DESCRIPTION, None, QtGui.QApplication.UnicodeUTF8))
		elif row == "16":
			FAENZA_DESCRIPTION = str("Tema de Ícones Faenza, para o Gnome.")
			self.textEdit.clear()
			self.textEdit.setText(QtGui.QApplication.translate("Neutrino Project", faenza.FAENZAdark_DESCRIPTION, None, QtGui.QApplication.UnicodeUTF8))
		elif row == "17":
			GShell_elementary_DESCRIPTION = str("Tema Elementary para o Gnome-Shell, por Half-Left")
			self.textEdit.clear()
			self.textEdit.setText(QtGui.QApplication.translate("Neutrino Project", GShell_elementary_DESCRIPTION, None, QtGui.QApplication.UnicodeUTF8))
		elif row == "18":
			GShell_smooth_DESCRIPTION = str("Tema Smooth-Inset para o Gnome-Shell, por Half-Left")
			self.textEdit.clear()
			self.textEdit.setText(QtGui.QApplication.translate("Neutrino Project", gshell_smooth.gshell_smooth_DESCRIPTION, None, QtGui.QApplication.UnicodeUTF8))
		elif row == "19":
			GShell_atolm_DESCRIPTION = str("Tema Atolm para o Gnome-Shell, por Half-Left")
			self.textEdit.clear()
			self.textEdit.setText(QtGui.QApplication.translate("Neutrino Project", GShell_atolm_DESCRIPTION, None, QtGui.QApplication.UnicodeUTF8))

		else:
			print "Ops..."
			
	#Signals and Slots
	
	self.connect(self.install_bt, QtCore.SIGNAL("clicked()"), install_fun)
	self.connect(self.remove, QtCore.SIGNAL("clicked()"), remove_fun)
	self.connect(self.listWidget, QtCore.SIGNAL("currentRowChanged (int)"), description)
	self.connect(self.listWidget, QtCore.SIGNAL("currentRowChanged (int)"), remove_enable)
	
app = QtGui.QApplication(sys.argv)
app.setStyle('plastique')
app.style()
main = MainWindow()
main.show()
sys.exit(app.exec_())
