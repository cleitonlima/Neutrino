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

FONTS = str("aajohan-* adf-* aldusleaf-* allgeyer-* apa-new-* apanov-* artwiz-* beteckna-* bitstream-* bpg-* dejavu-* dustin-* ecolier-* gargi-* gdouros-* gfs-* gnu-free-* google-droid-* hartke-aurulent-* mgopen-* mona-* oflb-* yanone-* ghostscript-fonts xorg-x11-fonts* liberation-*")
CHKFONT = str("http://cleitonlima.com.br/neutrino/packages/chkfontpath-1.10.1-2.fc13.i686.rpm")
MSTTFONT = str("http://cleitonlima.com.br/neutrino/packages/msttcorefonts-2.0-2.noarch.rpm")

from os import environ
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
	#Install Extra Fonts in repository
	base.pkg_install(FONTS)

	#Install Chkfont
	base.web_install(CHKFONT, "chkfontpath-1.10.1-2.fc13.i686.rpm")

	#Install Microsoft Fonts
	base.web_install(MSTTFONT, "msttcorefonts-2.0-2.noarch.rpm")

FONTS_DESCRIPTION = str("Collection of high quality TrueType fonts, default in any MS Windows installation. These are also the main webfonts as specified in microsoft.com/typography\nThe fonts:\nAndale Mono, Arial, Arial Black, Comic, Courier New, Georgia, Impact, Lucida Sans, Lucida Console, Microsoft Sans Serif, Symbol, Tahoma, Times New Roman, Trebuchet, Verdana, Webdings, Wingdings ")