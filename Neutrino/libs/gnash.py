#!/usr/bin/ env python

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
#This module will install Gnash, opensource alternative to Adobe Flash
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

GNASH = str("gnash-plugin")

def install():
	base.pkg_install("gnash gnash-plugin")

def remove():
	base.pkg_remove("gnash gnash-plugin")
	
GNASH_DESCRIPTION = str("Gnash is capable of reading up to SWF v9 files and op-codes, but primarily supports SWF v7, with better SWF v8 and v9 support under heavy development. Gnash includes initial parser support for SWF v8 and v9.")