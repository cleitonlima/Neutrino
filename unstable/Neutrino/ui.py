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
from libs import chromium, fonts, java, flash, codecs, nvidia, libreoffice, elementary, faenza, amd, Ssudo

class MainWindow(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
	
        self.setWindowTitle ("Neutrino Project")
	self.setObjectName("MainWindow")
        self.resize(691, 524)
	screen = QtGui.QDesktopWidget().screenGeometry()
        size =  self.geometry()
        self.move((screen.width()-size.width())/2, (screen.height()-size.height())/2)
	
	#MainWindow GridLayout
	#self.centralwidget = QtGui.QWidget(self)
        #self.centralwidget.setObjectName("centralwidget")
	#self.setCentralWidget(self.centralwidget)
	self.centralwidget = QtGui.QTabWidget(self)
	self.setCentralWidget(self.centralwidget)

	#The tab1 contains the list of applications
	tab1 = QtGui.QWidget(self)
	self.centralwidget.addTab(tab1, "Lista de Aplicativos")
	
	#First Tab Content
	self.gridLayout = QtGui.QGridLayout(tab1)
        self.gridLayout.setMargin(0)
        self.gridLayout.setObjectName("gridLayout")

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
	
	#Install button Icon
	icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("imgs/install.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
	
	#Execute button Icon
	icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("imgs/begin.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
	
	#Remove from list button Icon
	icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("imgs/clear.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)

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
	
	#Faenza Item
        item = QtGui.QListWidgetItem(self.listWidget)
        item.setIcon(icon_other)
        self.listWidget.item(14).setText(QtGui.QApplication.translate("MainWindow", "Tema de Ícones Faenza", None, QtGui.QApplication.UnicodeUTF8))
	
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
	
	#Add Install Button to Frame Internal Layout
        self.horizontalLayout.addWidget(self.install_bt)
	
	#Add Frame to MainWindow GridLayout
        self.gridLayout.addWidget(self.frame, 3, 0, 1, 1)
	
	self.progress = QtGui.QProgressBar(self.centralwidget)
	self.gridLayout.addWidget(self.progress, 4,0,1,1)
	self.progress.hide()
	
	#tab2 receive the list of tasks
	tab2 = QtGui.QWidget(self)
	self.centralwidget.addTab(tab2, "Lista de Tarefas")
	
	#tab2 Content
	#First Tab Content
	self.gridLayout2 = QtGui.QGridLayout(tab2)
        self.gridLayout2.setMargin(0)
        self.gridLayout2.setObjectName("gridLayout2")

	self.label = QtGui.QLabel(tab2)
	self.label.setText("Lista de Tarefas")
	self.gridLayout2.addWidget(self.label, 0,0,1,1)
	
	#ListWidget of Neutrino's tasks
        self.listWidget2 = QtGui.QListWidget(tab2)
        self.listWidget2.setIconSize(QtCore.QSize(32, 32))
        self.listWidget2.setObjectName("listWidget")

	#ListWidget gridLayout
	self.gridLayout2.addWidget(self.listWidget2, 1, 0, 1, 1)
	
	#Buttons Frame
	self.frame2 = QtGui.QFrame(tab2)
        self.frame2.setMinimumSize(QtCore.QSize(0, 50))
        self.frame2.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame2.setFrameShadow(QtGui.QFrame.Raised)
        self.frame2.setObjectName("frame")
        
	#Buttons Frame Internal Layout
	self.horizontalLayout2 = QtGui.QHBoxLayout(self.frame2)
        self.horizontalLayout2.setObjectName("horizontalLayout")
	
	#Uninstall Button
        self.rm = QtGui.QCommandLinkButton(self.frame2)
        self.rm.setMaximumSize(QtCore.QSize(45, 64))
        self.rm.setText("")
	self.rm.setIcon(icon6)
        self.rm.setIconSize(QtCore.QSize(32, 32))
        self.rm.setObjectName("Remove_item_from_list")
	self.rm.setToolTip(QtGui.QApplication.translate("MainWindow", "Remover Item Selecionado da Lista", None, QtGui.QApplication.UnicodeUTF8))
	#self.rm.setEnabled(False)
	
	#Add Remove Item Button to Frame Internal Layout
        self.horizontalLayout2.addWidget(self.rm)
        
	#Install Button
        self.execute = QtGui.QCommandLinkButton(self.frame2)
        self.execute.setMaximumSize(QtCore.QSize(45, 64))
        self.execute.setText("")
        self.execute.setIcon(icon5)
	self.execute.setIconSize(QtCore.QSize(32, 32))
	self.execute.setObjectName("execute_bt")
	self.execute.setToolTip(QtGui.QApplication.translate("MainWindow", "Executar as tarefas", None, QtGui.QApplication.UnicodeUTF8))
	#self.execute.setEnabled(False)
	
	#Add Install Button to Frame Internal Layout
        self.horizontalLayout2.addWidget(self.execute)
	
	#Add Frame to MainWindow GridLayout
        self.gridLayout2.addWidget(self.frame2, 3, 0, 1, 1)
	
	#Internal Functions
	def message(slot, text):
		QtGui.QMessageBox.information(self, str(slot),QtGui.QApplication.translate("MainWindow", str(text), None, QtGui.QApplication.UnicodeUTF8))
	
	def progress_show():
		message("Information", "Tarefa iniciada, clique em ok.")
		self.progress.show()
		self.progress.setRange(0,0)
	
	def progress_hide():
		message("Information", "Tarefa concluida, clique em ok.")
		self.progress.hide()
		
	def progress_error():
		message("Information", "Tarefa concluida com erros, veja o log em /tmp/neutrino/error.txt")
		self.progress.hide()
	
	tasks = []
	
	def task_add():
	#Add Item to the List
		row = str(self.listWidget.currentRow())
		if row == "0":
			self.listWidget2.addItem("Instalar driver Nvidia")
			tasks.append("nvidia")
			message("Information", "Tarefa adicionada a lista.")
		elif row == "1":
			self.listWidget2.addItem("Instalar Driver Nvidia 173")
			tasks.append("nvidia_173")
			message("Information", "Tarefa adicionada a lista.")
		elif row == "2":
			try:
				self.listWidget2.addItem("Instalar driver Nvidia")
				tasks.append("nvidia_96")
				message("Information", "Tarefa adicionada a lista.")
			except Exception, e:
				message("Error", "Ocorreu o seguinte erro: %s" % e)	
		elif row == "3":
			try:
				self.listWidget2.addItem("Instalar driver placa de video AMD")
				tasks.append("amd")
				message("Information", "Tarefa adicionada a lista.")			
			except Exception, e:
				message("Error", "Ocorreu o seguinte erro: %s" % e)
		elif row == "4":
			try:
				self.listWidget2.addItem("Instalar codecs proprietarios")
				tasks.append("codecs")
				message("Information", "Tarefa adicionada a lista.")
			except Exception, e:
				message("critical", "Ocorreu o seguinte erro: %s" % e)	
		elif row == "5":
			try:
				self.listWidget2.addItem("Instalar suite de escritorio LibreOffice")
				tasks.append("loffice")
				message("Information", "Tarefa adicionada a lista.")
			except Exception, e:
				message("Error", "Ocorreu o seguinte erro: %s" % e)	
		elif row == "6":
			try:
				self.listWidget2.addItem("Instalar Fontes Proprietarias e Nao Livres.")
				tasks.append("fonts")
				message("Information", "Tarefa adicionada a lista.")
			except Exception, e:
				message("Error", "Ocorreu o seguinte erro: %s" % e)	
		elif row == "7":
			try:
				self.listWidget2.addItem("Adicionar o usuario atual como administrador")
				tasks.append("root")
				message("Information", "Tarefa adicionada a lista.")
			except Exception, e:
				message("Error", "Ocorreu o seguinte erro: %s" % e)
		elif row == "8":
			try:
				self.listWidget2.addItem("Instalar o OpenJDK")
				tasks.append("openjdk")
				message("Information", "Tarefa adicionada a lista.")
			except Exception, e:
				message("Error", "Ocorreu o seguinte erro: %s" % e)	
		elif row == "9":
			try:
				self.listWidget2.addItem("Instalar o Oracle Java")
				tasks.append("ojava")
				message("Information", "Tarefa adicionada a lista.")			
			except Exception, e:
				message("Error", "Ocorreu o seguinte erro: %s" % e)
		elif row == "10":
			try:
				self.listWidget2.addItem("Instalar plugin Gnash")
				tasks.append("gnash")
				message("Information", "Tarefa adicionada a lista.")
			except Exception, e:
				message("Error", "Ocorreu o seguinte erro: %s" % e)
		elif row == "11":
			try:
				self.listWidget2.addItem("Instalar o Adobe Flash Plugin")
				tasks.append("flash")
				message("Information", "Tarefa adicionada a lista.")
			except Exception, e:
				message("Error", "Ocorreu o seguinte erro: %s" % e)	
		elif row == "12":
			try:
				self.listWidget2.addItem("Instalar navegador Chromium")
				tasks.append("chromium")
				message("Information", "Tarefa adicionada a lista.")
			except Exception, e:
				message("Error", "Ocorreu o seguinte erro: %s" % e)	
		elif row == "13":
			try:
				self.listWidget2.addItem("Instalar tema de icones Elementary")
				tasks.append("elementary")
				message("Information", "Tarefa adicionada a lista.")
			except Exception, e:
				message("Error", "Ocorreu o seguinte erro: %s" % e)
		elif row == "14":
			try:
				self.listWidget2.addItem("Instalar tema de icones Faenza")
				tasks.append("faenza")
				message("Information", "Tarefa adicionada a lista.")
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
		else:
			self.remove.setEnabled(False)
			
	def remove_fun():
		row = str(self.listWidget.currentRow())
		if row == "8":
			try:
				self.listWidget2.addItem("Remover o OpenJDK")
				tasks.append("openjdk_rm")
				message("Information", "Tarefa adicionada a lista.")
			except Exception, e:
				message("Error", "Ocorreu o seguinte erro: %s" % e)
		elif row == "10":
			try:
				self.listWidget2.addItem("Remover o Plugin Gnash")
				tasks.append("gnash_rm")
				message("Information", "Tarefa adicionada a lista.")			
			except Exception, e:
				message("Error", "Ocorreu o seguinte erro: %s" % e)
		elif row == "11":
			try:
				self.listWidget2.addItem("Remover o Flash Plugin")
				tasks.append("flash_rm")
				message("Information", "Tarefa adicionada a lista.")
			except Exception, e:
				message("Error", "Ocorreu o seguinte erro: %s" % e)
		elif row == "12":
			try:
				self.listWidget2.addItem("Remover o Navegador Chromium")
				tasks.append("chromium_rm")
				message("Information", "Tarefa adicionada a lista.")
			except Exception, e:
				message("Error", "Ocorreu o seguinte erro: %s" % e)
		elif row == "13":
			try:
				self.listWidget2.addItem("Remover o tema de icones Elementary")
				tasks.append("elementary_rm")
				message("Information", "Tarefa adicionada a lista.")
			except Exception, e:
				message("Error", "Ocorreu o seguinte erro: %s" % e)
		elif row == "14":
			try:
				self.listWidget2.addItem("Remover o tema de icones Faenza")
				tasks.append("faenza_rm")
				message("Information", "Tarefa adicionada a lista.")
			except Exception, e:
				message("Error", "Ocorreu o seguinte erro: %s" % e)
	
	#Execute Tasks Function
	def exec_tasks():
		row = 0
		message("Information", "Iniciando a tarefa. clique em OK.")
		try:
			for item in tasks:
				if item == "nvidia":
					row = row + 1
					nvidia.install("default")
				elif item == "nvidia_173":
					row = row + 1
					nvidia.install("173")
				elif item == "nvidia_96":
					row = row + 1
					nvidia.install("96")
				elif item == "amd":
					row = row + 1
					amd.install()
				elif item == "codecs":
					row = row + 1
					codecs.install()
				elif item == "loffice":
					row = row + 1
					libreoffice.install()
				elif item == "fonts":
					row = row + 1
					fonts.install()
				elif item == "root":
					row = row + 1
					Ssudo.install()
				elif item == "opendjk":
					row = row + 1
					java.install("openjdk")
				elif item == "opendjk_rm":
					row = row + 1
					java.remove("openjdk")
				elif item == "ojava":
					row = row + 1
					java.install("java")
				elif item == "gnash":
					row = row + 1
					flash.install("gnash")
				elif item == "gnash_rm":
					row = row + 1
					flash.remove("gnash")
				elif item == "flash":
					row = row + 1
					flash.install("flash")
				elif item == "flash_rm":
					row = row + 1
					flash.remove("flash")
				elif item == "chromium":
					row = row + 1
					chromium.install()
				elif item == "chromium_rm":
					row = row + 1
					chromium.remove()
				elif item == "elementary":
					row = row + 1
					elementary.install()
				elif item == "elementary_rm":
					row = row + 1
					elementary.remove()
				elif item == "faenza":
					row = row + 1
					faenza.install()
				elif item == "faenza_rm":
					row = row + 1
					faenza.remove()
				else:
					pass
		except Exception, e:
			message("Error", "Ocorreu o seguinte erro: %s" % e)
		for item in tasks:
			tasks
			tasks.remove(item)
		message("Information", "Tarefas Concluidas")
		self.listWidget2.clear()
		
	
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
			self.textEdit.setText(QtGui.QApplication.translate("Neutrino Project", Ssudo.SUDO_DESCRIPTION, None, QtGui.QApplication.UnicodeUTF8))
		elif row == "8":
			self.textEdit.clear()
			self.textEdit.setText(QtGui.QApplication.translate("Neutrino Project", java.OPENJDK_DESCRIPTION, None, QtGui.QApplication.UnicodeUTF8))
		elif row == "9":
			self.textEdit.clear()
			self.textEdit.setText(QtGui.QApplication.translate("Neutrino Project", java.JAVA_DESCRIPTION, None, QtGui.QApplication.UnicodeUTF8))
		elif row == "10":
			self.textEdit.clear()
			self.textEdit.setText(QtGui.QApplication.translate("Neutrino Project", flash.GNASH_DESCRIPTION, None, QtGui.QApplication.UnicodeUTF8))
		elif row == "11":
			self.textEdit.clear()
			self.textEdit.setText(QtGui.QApplication.translate("Neutrino Project", flash.FLASH_DESCRIPTION, None, QtGui.QApplication.UnicodeUTF8))
		elif row == "12":
			self.textEdit.clear()
			self.textEdit.setText(QtGui.QApplication.translate("Neutrino Project", chromium.CHROMIUM_DESCRIPTION, None, QtGui.QApplication.UnicodeUTF8))
		elif row == "13":
			self.textEdit.clear()
			self.textEdit.setText(QtGui.QApplication.translate("Neutrino Project", elementary.elementary_DESCRIPTION, None, QtGui.QApplication.UnicodeUTF8))
		elif row == "15":
			FAENZA_DESCRIPTION = str("Tema de Ícones Faenza, para o Gnome.")
			self.textEdit.clear()
			self.textEdit.setText(QtGui.QApplication.translate("Neutrino Project", faenza.FAENZA_DESCRIPTION, None, QtGui.QApplication.UnicodeUTF8))
		else:
			print "Ops..."
			
	#Signals and Slots
	
	self.connect(self.install_bt, QtCore.SIGNAL("clicked()"), task_add)
	self.connect(self.rm, QtCore.SIGNAL("clicked()"), self.listWidget2.clear)
	self.connect(self.execute, QtCore.SIGNAL("clicked()"), exec_tasks)
	self.connect(self.remove, QtCore.SIGNAL("clicked ()"), remove_fun)
	self.connect(self.listWidget, QtCore.SIGNAL("currentRowChanged (int)"), description)
	self.connect(self.listWidget, QtCore.SIGNAL("currentRowChanged (int)"), remove_enable)
	
app = QtGui.QApplication(sys.argv)
app.setStyle('plastique')
app.style()
main = MainWindow()
main.show()
sys.exit(app.exec_())
