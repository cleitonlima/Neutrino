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
#This module will install LibreOffice Suite.
#
from os import environ, system, remove
import urllib2
desktoptype = environ.get('DESKTOP_SESSION')
from api.neutrino import GBase
base = GBase()

def install():
	base.pkg_install("libreoffice-calc libreoffice-writer libreoffice-impress libreoffice-langpack-pt-br libreoffice-pdfimporter")
	
	#Install CoGrOO extension for Writer
	u = urllib2.urlopen('http://cleitonlima.com.br/neutrino/packages/CoGrOO-AddOn-3.1.0-bin.oxt')
	localFile = open('/tmp/neutrino/CoGrOO-AddOn-3.1.0-bin.oxt', 'w')
	localFile.write(u.read())
	localFile.close()
	system("beesu xterm -e unopkg add --shared /tmp/neutrino/CoGrOO-AddOn-3.1.0-bin.oxt")
	remove("/tmp/neutrino/CoGrOO-AddOn-3.1.0-bin.oxt")

LIBO_DESCRIPTION = str("Suíte de escritório de código aberto, compatível com formatos do MS Office e outros formatos abertos, como o ODF.")
