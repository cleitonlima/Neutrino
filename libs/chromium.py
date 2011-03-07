#!/usr/bin/ env python
# -*- coding: utf-8 -*-

#Neutrino Project

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


#por Cleiton Lima <cleitonlima@fedoraproject.org>
#por Rafael Gomes <rafaelgomes@techfree.com.br>
#Chromium Browser Install
#Must be executed as root

from os import chdir, path, system, environ
desktoptype = environ.get('DESKTOP_SESSION')
print desktoptype
if "gnome" in desktoptype :
	from api.base import GBase
	base = GBase()
elif "kde" in desktoptype:
	from api.base import KBase
	base = KBase()
else:
	pass
def install():
	#Adding Chromium Repo
	if path.isfile("/etc/yum.repos.d/fedora-chromium.repo") == False:
		chdir("/etc/yum.repos.d/")
		system("xterm -e beesu wget http://repos.fedorapeople.org/repos/spot/chromium/fedora-chromium.repo")
	else:
		pass
	chdir("/etc/yum.repos.d/")
	system("xterm -e beesu wget http://repos.fedorapeople.org/repos/spot/chromium/fedora-chromium.repo")
	#Install Chromium Browser
	base.pkg_install("chromium")
