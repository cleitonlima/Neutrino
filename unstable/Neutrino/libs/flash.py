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
#Adobe Flash Plugin Install

from os import chdir, path, system, environ
desktoptype = environ.get('DESKTOP_SESSION')
from api.neutrino import GBase
base = GBase()


FLASH = ["flash-plugin"]
GNASH = ["gnash-plugin", "gnash"]

def install(version):
	if version == "adobe":
		#Check Adobe's repositoy
		if path.isfile("/etc/yum.repos.d/adobe-linux-i386.repo") == False:
			base.web_install("http://cleitonlima.com.br/neutrino/packages/adobe-release-i386-1.0-1.noarch.rpm", "adobe-release-i386-1.0-1.noarch.rpm")
		#Install Flash Plugin from repo
		base.pkg_install(FLASH)
	elif version == "gnash":
		base.pkg_install(GNASH)

def remove (version):
	if version == "adobe":
		base.pkg_remove(FLASH)
	elif version == "gnash":
		base.pkg_remove(GNASH)
	
FLASH_DESCRIPTION = str("Adobe Flash Plugin 10.2.159.1 Suporte Completo: Mozilla SeaMonkey 1.0+, Firefox 1.5+, Mozilla 1.7.13+")
GNASH_DESCRIPTION = str("Opção de código aberto para substituir o Flash Plugin. Compatível com a versão 7, bom suporte a versão 8 e com suporte a versão 9 em desenvolvimento contínuo.")
