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
#This Module Installs Faenza Icon Theme
#
from os import environ, path, remove
from dialog import *
from dialog_ok import *
from dialog_error import *

desktoptype = environ.get('DESKTOP_SESSION')
if "gnome" in desktoptype :
	from api.base import GBase
	base = GBase()
else:
	exit()


def install():
	file = open("/tmp/neutrino/text_var", "w")
	file.write("Deseja Instalar e Aplicar o\n Tema de Ícones Faenza?")
	file.close()
	app = QtGui.QApplication(sys.argv)
	ex = NoYes()
	ex.show()
	app.exec_()
	set = str(open("/tmp/neutrino/dialog_var").read())
	if set == 'ok':
		try:
			if path.isdir("/usr/share/icons/Faenza") == False:
				base.pkg_install("faenza-icon-theme")
				base.gsettings("icon-theme", "Faenza")
			else:
				base.gsettings("icon-theme", "Faenza")
		except:
			pass
		file = open("/tmp/neutrino/text_var", "w")
		file.write("Processo Concluído.")
		file.close()
		app1 = QtGui.QApplication(sys.argv)
		ex1 = Ok()
		ex1.show()
		app1.exec_()
	else:
		file = open("/tmp/neutrino/text_var", "w")
		file.write("Processo Cancelado.")
		file.close()
		app1 = QtGui.QApplication(sys.argv)
		ex1 = OkCancel()
		ex1.show()
		app1.exec_()
install()

remove("/tmp/neutrino/text_var")

FAENZA_DESCRIPTION = str("Faenza Icon Theme for Gnome.")