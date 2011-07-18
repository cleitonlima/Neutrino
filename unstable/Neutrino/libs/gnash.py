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
#This module will install Gnash, opensource alternative to Adobe Flash
#
from os import environ
from api.neutrino import GBase
base = GBase()

package = ["gnash-plugin", "gnash"]

def install():
	base.pkg_install(package)
	
def remove():
	background = pkg_remove(package)
	background.start()
	
GNASH_DESCRIPTION = str("Opção de código aberto para substituir o Flash Plugin. Compatível com a versão 7, bom suporte a versão 8 e com suporte a versão 9 em desenvolvimento contínuo.")
