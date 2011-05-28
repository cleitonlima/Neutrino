#!/usr/bin/ env python

#Neutrino Project
#por Cleiton Lima <cleitonlima@fedoraproject.org>

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


#Install OpenJDK
#
from os import environ
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

JAVA_OPEN = str("java-openjdk icedtea-web")

#Install OpenJDK
def install():
	base.pkg_install(JAVA_OPEN)
	
#Remove OpenJDK
def remove():
	base.pkg_remove(JAVA_OPEN)

OPENJDK_DESCRIPTION = str("The OpenJDK runtime environment.")