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

from api.base import *


def font_install():
	#Install Extra Fonts in repository
	pkg_install(FONTS)

	#Install Chkfont
	web_install(CHKFONT)

	#Install Microsoft Fonts
	web_install(MSTTFONT)