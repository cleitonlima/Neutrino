#!/usr/bin env python
# -*- coding: utf-8 -*-

#Project Neutrino
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
#This script will install extra fonts, present in the system and in others ways.
#

#Smooth-Inset Gnome-Shell Theme
from os import environ, path
from dialog import *
from dialog_ok import *
from dialog_error import *

desktoptype = environ.get('DESKTOP_SESSION')
if "gnome" in desktoptype :
	from api.base import GBase
	base = GBase()
elif "kde" in desktoptype:
	from api.base import KBase
	base = KBase()
else:
	pass

def install():
	if path.isdir("/usr/share/themes/gnome-shell/smooth") == True:
		file = open("/tmp/neutrino/text_var", "w")
		file.write("O Tema Smooth-Inset já está instalado.\n Deseja reinstalar?")
		file.close()
		app = QtGui.QApplication(sys.argv)
		ex = NoYes()
		ex.show()
		app.exec_()
		set = str(open("/tmp/neutrino/dialog_var").read())
		if set == 'ok':
			base.web_install("http://cleitonlima.com.br/neutrino/packages/gnome-shell-theme-smooth-inset-1.3-1.fc15.noarch.rpm", "gnome-shell-theme-smooth-inset-1.3-1.fc15.noarch.rpm")
			file = open("/tmp/neutrino/text_var", "w")
			file.write("Reinicie o Gnome-Shell para aplicar o tema. (ALT+F2 e digitar 'rt')")
			file.close()
			app1 = QtGui.QApplication(sys.argv)
			ex1 = Ok()
			ex1.show()
			app1.exec_()
		else:
			file = open("/tmp/neutrino/text_var", "w")
			file.write("O pacote já está instalado. Reinstalação Cancelada.")
			file.close()
			app2 = QtGui.QApplication(sys.argv)
			ex2 = OkCancel()
			ex2.show()
			app2.exec_()
	else:
		base.web_install("http://cleitonlima.com.br/neutrino/packages/gnome-shell-theme-smooth-inset-1.3-1.fc15.noarch.rpm", "gnome-shell-theme-smooth-inset-1.3-1.fc15.noarch.rpm")
		file = open("/tmp/neutrino/text_var", "w")
		file.write("Reinicie o Gnome-Shell para aplicar o tema. (ALT+F2 e digitar 'rt')")
		file.close()
		app3 = QtGui.QApplication(sys.argv)
		ex3 = Ok()
		ex3.show()
		app3.exec_()

install()

gshell_elementary_DESCRIPTION = str("Tema Smooth-Inset para o Gnome-Shell, por half-left. Após atualizar o Gnome-Shell, será necessário reinstalar o tema para que ele volte a aparecer.")