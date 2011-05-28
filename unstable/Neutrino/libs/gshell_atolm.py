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
from os import environ, path, getenv


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
	home = str(getenv("HOME"))
	paths = str("/.themes/")
	if path.isdir(home+paths+str("gs-atolm")) == True:
		base.gshell_theme_apply("gs-atolm")
	else:
		base.gshell_theme_install("http://cleitonlima.com.br/neutrino/packages/gs-atolm.zip", "gs-atolm.zip")
		base.gshell_theme_apply("gs-atolm")
		
gshell_elementary_DESCRIPTION = str("Tema Atolm para o Gnome-Shell, por half-left. Após atualizar o Gnome-Shell, será necessário reinstalar o tema para que ele volte a aparecer.")