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
desktoptype = environ.get('DESKTOP_SESSION')
from api.neutrino import GBase
base = GBase()


def install():
	if path.isdir("/usr/share/icons/Faenza") == False:
		package = ["faenza-icon-theme"]
		base.pkg_install(package)
		

def install_dark():
	if path.isdir("/usr/share/icons/Faenza") == False:
		package = ["faenza-icon-theme"]
		base.pkg_install(package)

def remove ():
	package = ["faenza-icon-theme"]
	base.pkg_remove(package)

FAENZA_DESCRIPTION = str("Tema de ícones Faenza.")
FAENZAdark_DESCRIPTION = str("Tema de ícones Faenza, habilita a versão para temas escuros.")
