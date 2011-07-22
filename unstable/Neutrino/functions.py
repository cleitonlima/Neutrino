#!/usr/bin/ env python
# -*- coding: utf-8 -*-

#Neutrino Project
#Por Cleiton Lima <cleitonlima@fedoraproject.org>

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


#
#This Module Installs Elementary Icon Theme
#
	tasks = []
	
	def task_add():
	#Add Item to the List
		row = str(self.listWidget.currentRow())
		if row == "0":
			self.listWidget2.addItem("Instalar driver Nvidia")
			tasks.append("nvidia")
		elif row == "1":
			self.listWidget2.addItem("Instalar Driver Nvidia 173")
			tasks.append("nvidia_173")
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
				package = ['gnash', 'gnash-plugin']
				self.pkg_ins.deps(package)
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
				package = ['elementary-icon-theme']
				self.pkg_ins.install(package)
			except Exception, e:
				message("Error", "Ocorreu o seguinte erro: %s" % e)
		elif row == "14":
			try:
				package = ['elementary-icon-theme']
				self.pkg_ins.install(package)
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
	
	#Execute Tasks Function
	def exec_tasks():
		row = 0
		for item in tasks:
			if item == "nvidia":
				print "nvidia"
				row = row + 1
				print row
			elif item == "nvidia_173":
				print "nvidia 173"
				row = row + 1
				print row
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
				package = ['gnash', 'gnash-plugin']
				self.pkg_rm.remove(package)			
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
	