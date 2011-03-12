#!/usr/bin env python
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

def install():
	#Install Extra Fonts in repository
	base.pkg_install(FONTS)

	#Install Chkfont
	base.web_install(CHKFONT)

	#Install Microsoft Fonts
	base.web_install(MSTTFONT)