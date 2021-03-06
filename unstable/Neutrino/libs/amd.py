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
#Installation of AMD Cards' Proprietary driver

from os import chdir, path, system, environ
desktoptype = environ.get('DESKTOP_SESSION')
print desktoptype
from api.neutrino import GBase
base = GBase()

def install():
	#Check if repo RPMFusion already exists
	if path.isfile("/etc/yum.repos.d/rpmfusion-free.repo") == False:
		base.web_install(RPMFUSION_FREE, "rpmfusion-free-release-stable.noarch.rpm")
	elif path.isfile("/etc/yum.repos.d/rpmfusion-nonfree.repo") == False:
		base.web_install(RPMFUSION_NONFREE, "rpmfusion-nonfree-release-stable.noarch.rpm")
	
	#Install Catalyst Driver
	base.pkg_install("xorg-x11-drv-catalyst")

AMD_DESCRIPTION = str("Esse pacote fornece a versão mais recente do driver para placas de vídeo AMD.")
