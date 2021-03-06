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
from os import environ, path, remove
desktoptype = environ.get('DESKTOP_SESSION')
from api.neutrino import GBase
base = GBase()



def install():
	if path.isdir("/usr/share/icons/elementary") == False:
		package = ['elementary-icon-theme']
		base.pkg_install(package)
		base.gsettings("icon-theme", "elementary")
	else:
		base.gsettings("icon-theme", "elementary")

def install_dark():
	if path.isdir("/usr/share/icons/elementary") == False:
		package = ['elementary-icon-theme']
		base.pkg_install(package)
		base.gsettings("icon-theme", "elementary")
	else:
		base.gsettings("icon-theme", "elementary")

def remove():
	if path.isdir("/usr/share/icons/elementary") == True:
		package = ['elementary-icon-theme']
		base.pkg_remove(package)
		base.gsettings("icon-theme", "Fedora")
	else:
		pass

elementary_DESCRIPTION = str("Tema de ícones Elementary para Gnome.")
elementarydark_DESCRIPTION = str("Tema de ícones Elementary para Gnome.")
